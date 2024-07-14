from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from ursina.window import *
from ursinanetworking import *
import threading
import os
import sys
from math import *
import time
import json

FalseTrued = True
TrueFalsed = False

app = Ursina()
player = FirstPersonController()
spawn_position = player.position #get spawn position
pycr_version = "Pynecraft 0.1.1_beta1"
HB = HealthBar(bar_color=color.red, scale=(0.6, 0.05), max_value=20)
HB.position = (-.6,-.35,0)
#SB = HealthBar(bar_color=color.lime, scale=(0.6, 0.05), max_value=10)
#SB.position = (0,-.35,0)
ra_texture = load_texture('assets/rs/images/ra2')
sky_day_texture = load_texture('assets/rs/images/skybox_day.png')
sky_night_texture = load_texture('assets/rs/images/skybox_night.png')
arm_texture = load_texture('assets/rs/images/arm_texture.png')
nothing_texture = load_texture('invalid/directory/for/put/nothing')
cross_cursor = load_texture('assets/rs/images/cursor')
invisible = load_texture('assets/rs/images/nothing')
grass_texture = load_texture('assets/rs/images/grass_block.png')
stone_texture = load_texture('assets/rs/images/stone_block.png')
brick_texture = load_texture('assets/rs/images/brick_block.png')
dirt_texture = load_texture('assets/rs/images/dirt_block.png')
bedrock_texture = load_texture('assets/rs/images/bedrock_block.png')
glass_texture = load_texture('assets/rs/images/glass_block.png')
basic_wood_texture = load_texture('assets/rs/images/basic_wood_block')
basic_wood_planks_texture = load_texture('assets/rs/images/basic_wood_planks_block')
error_texture = load_texture('assets/rs/images/error_debug_block')
water_texture = load_texture('assets/rs/images/water_block')
pycr_logo_texture = load_texture('assets/rs/images/pycr_logo.png')
punch_sound = Audio('assets/rs/sounds/punch_sound',loop = False, autoplay = False)
glass_sound = Audio('assets/rs/sounds/glass_sound',loop = False, autoplay = False)
boss1_sound = Audio('assets/rs/sounds/boss1', loop = True, autoplay = True)
kill_sound = Audio('assets/rs/sounds/kill', loop = False, autoplay = False)
crash_sound = Audio('assets/rs/sounds/kill', loop = True, autoplay = False)
block_pick = 1
block_texture = grass_texture
sky_texture = sky_night_texture
global escmenuenabled
escmenuenabled = False
global isplayerkilled
isplayerkilled = False
global retb
retb = False
global cameraposition
cameraposition = "normal"
window.fps_counter.enabled = True
window.exit_button.visible = False
window.title = pycr_version
window.icon = 'game_assets/icon.ico'
window.borderless = False
window.show_cursor = False
camera.z -= 5
gravity = 1

#render_distance = 25
render_distance = 10
fullscreen = True
basic_win_size = window.size
camera_pos = "normal"
previous_pla_pos = player.position

ip = sys.argv[1]
client = UrsinaNetworkingClient(ip, 28123)
username = sys.argv[2]
username_text = Text(text=username, position=(player.x, player.y + 2, player.z), scale=2)

def send_player_coordinates(client):
	time.sleep(5)
	client.send_message("get_player_coordinates", f"{username}:{player.position}")
@client.event
def MakeServerBlock(Content):
	action = Content["action"]
	block_name = Content["block"]
	position = Content["position"]
	block_class = block_classes[block_name]
	print(f"Recieved Block: action:{action}, block:{block_class}, position:{position}")
	print(f"Action Value : {repr(action)}")
	print(f"Fake Action Value : {action}")
	if action == "place":
		Voxel = block_class(position = position)
		all_blocks.append(Voxel)
		print("Creating Block")
	if action == "casse":
		for block in all_blocks:
			if isinstance(block, block_class) and block.position == position:
				all_blocks.remove(block)
				block.enabled = False

		
@client.event
def onConnectionError(Reason):
	print(f"NET_CONN_ERROR:{Reason}")
@client.event
def onConnectionEtablished():
	print("Connected to the server")
@client.event
def ser_mes(Content):
	print(f"Server send: {Content}")
def process_net_events():
	while True:
		client.process_net_events()
		time.sleep(0.1)
net_thread = threading.Thread(target=process_net_events)
net_thread.start()

def crash():
	def loop():
		time.sleep(3)
		crash_sound.play()
		time.sleep(3)
		crash_sound.play()
		time.sleep(1)
		crash_sound.play()
		time.sleep(0.5)
		crash_sound.play()
		loop()
	loop()
	time.sleep(20)
	application.quit

def kill():
	global isplayerkilled
	global respawnb
	global quitb
	isplayerkilled = True
	if isplayerkilled == True:	
		execatonce = False
		player.enabled = False
		quitb=Button(text="Quit The Game", color=color.lime, text_color=color.gray, scale=.25, position=(.0,-.2))
		quitb.tooltip=Tooltip("Click here for quit the game")
		quitb.on_click = application.quit
		respawnb=Button(text="Respawn", color=color.lime, text_color=color.gray, scale=.25, position=(.0,.2))
		respawnb.tooltip=Tooltip("Click here for respawn")
		respawnb.on_click = respawn
		kill_sound.play()
	
def damage(power):
	HB.value = HB.value - power
	
def heal(power):
	HB.value = HB.value + power

def sprint_damage(power):
	SB.value = SB.value - power
	
def sprint_heal(power):
	SB.value = SB.value + d
	
def returntogame():
	global escmenuenabled
	player.enabled = True
	escmenuenabled = False
	retb = True
	destroy(escmenuquitb)
	destroy(escmenuretb)
	
def respawn():
	global isplayerkilled
	global quitb
	global respawnb
	player.enabled = True
	HB.value = 20
	isplayerkilled = False
	destroy(quitb)
	destroy(respawnb)
	player.position = spawn_position
	  
def update():
	global block_pick
	global previous_pla_pos
	
	current_position = player.position
	dis_distance = distance(current_position, previous_pla_pos)
	if dis_distance >= 5:
		#send_player_coordinates(client)
		previous_pla_pos = current_position
	
	if len(sys.argv) > 1:
		if sys.argv[1] == "--noboss":
			print("No Boss,OK")
		if sys.argv[1] == "--boss":
			move_entity(speed=1.5, knowback=False, gravity=-1)
			move_entity(e1=mra, speed=2, gravity=-1)
	
	if HB.value == 0:
		kill()

	if player.enabled == True:
		if held_keys['left mouse']:
			lefthand.active()
		else:
			lefthand.passive()
		if held_keys['right mouse']:
			righthand.active()
		else:
			righthand.passive()
	
	if held_keys['1']: block_pick = 1
	if held_keys['2']: block_pick = 2
	if held_keys['3']: block_pick = 3
	if held_keys['4']: block_pick = 4
	if held_keys['5']: block_pick = 5
	if held_keys['6']: block_pick = 6
	if held_keys['7']: block_pick = 7
	if held_keys['8']: block_pick = 8
	if held_keys['9']: block_pick = 9
#mob	
#set mob to an acronyme for move_entity
#mob code
class Inventory(Entity):
	def __init__(self):
		super().__init__()
		self.slots = []
		self.selected_slot = 0
		for i in range(9):
			slot = Entity(parent=self, model='quad', color=color.gray, position=(i, 0, 0),  scale=10, texture='assets/rs/images/slot.png')
			self.slots.append(slot)
			print(self.slots)
			self.show_inventory()
		self.update_selected_slot()

	def update_selected_slot(self):
		for i, slot in enumerate(self.slots):
			if i == self.selected_slot:
				slot.color = color.white
			else:
				slot.color = color.gray

	def input(self, key):
		if key.isdigit():
			index = int(key) - 1
			if index < len(self.slots):
				self.selected_slot = index
				self.update_selected_slot()
				
class RickAstley(Entity):
	def __init__(self, position = (0,3,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/rs/objects/default_obj',
			texture = ra_texture,
			scale = 10,
			collider = "box")
ra = RickAstley(position=(0, -10, 0))
boss1_sound.play()			

class MiniRickAsltey(Entity):
	def __init__(self, position = ra.position):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/rs/objects/default_obj',
			texture = ra_texture,
			scale = 2.75,
			collider = "box")
mra = MiniRickAsltey()
			
#show player
class CameraPlayer(Entity):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/rs/objects/default_obj',
			scale = player.scale,
			texture = invisible)
	def update(self):
		caplpos = player.position + Vec3(0, player.height, 0)
		self.position = caplpos
		self.rotation = player.rotation
		
#blocks	
deactivated_blocks = []
all_blocks = []
prev_player_position = player.position
refresh_rate = render_distance / 2

class grass_block(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/rs/objects/block',
			origin_y = 0.5,
			texture = grass_texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			highlight_color = color.lime,
			scale = 0.5,
			collider = 'box')
		all_blocks.append(self)
		self.block_type = 'grass_block'
				
	def update(self):
		global prev_player_position
		if player.position is None or distance(player.position, prev_player_position) > refresh_rate:
			prev_player_position = player.position
			for block in all_blocks:
				dist = distance(block.position, player.position)
				if dist < render_distance:
					if block.position in deactivated_blocks:
						deactivated_blocks.remove(block.position)
					block.visible = True
					block.ignore = False
					block.enabled = True
				else:
					if block.position not in deactivated_blocks:
						deactivated_blocks.append(block.position)
					block.visible = False
					block.ignore = True
					block.enabled = False
	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':
				if player.enabled == True:
					punch_sound.play()
					if block_pick == 1: block_texture = grass_block; block_mltp = "grass_block"
					if block_pick == 2: block_texture = stone_block; block_mltp = "stone_block"
					if block_pick == 3: block_texture = brick_block; block_mltp = "brick_block"
					if block_pick == 4: block_texture = dirt_block; block_mltp = "dirt_block"
					if block_pick == 5: block_texture = bedrock_block; block_mltp = "bedrock_block"
					if block_pick == 6: block_texture = glass_block; block_mltp = "glass_block"
					if block_pick == 7: block_texture = basic_wood_block; block_mltp = "basic_wood_block"
					if block_pick == 8: block_texture = basic_wood_planks_block; block_mltp = "basic_wood_planks_block"
					block = block_texture(position = self.position + mouse.normal)
					client.send_message("BlockUpdate", {"action": "place", "block": block_mltp, "position": self.position + mouse.normal})
					print("sended Block Update")
			if key == 'left mouse down':
				if player.enabled == True:
					punch_sound.play()
					client.send_message("BlockUpdate", {"action": "casse", "block": self.block_type, "position": self.position})
					destroy(self)
					all_blocks.remove(self)

class stone_block(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/rs/objects/block',
			origin_y = 0.5,
			texture = stone_texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			highlight_color = color.lime,
			scale = 0.5,
			collider = 'box')
		all_blocks.append(self)
		self.block_type = 'stone_block'
				
	def update(self):
		global prev_player_position
		if player.position is None or distance(player.position, prev_player_position) > refresh_rate:
			prev_player_position = player.position
			for block in all_blocks:
				dist = distance(block.position, player.position)
				if dist < render_distance:
					if block.position in deactivated_blocks:
						deactivated_blocks.remove(block.position)
					block.visible = True
					block.ignore = False
					block.enabled = True
				else:
					if block.position not in deactivated_blocks:
						deactivated_blocks.append(block.position)
					block.visible = False
					block.ignore = True
					block.enabled = False
	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':
				if player.enabled == True:
					punch_sound.play()
					if block_pick == 1: block_texture = grass_block; block_mltp = "grass_block"
					if block_pick == 2: block_texture = stone_block; block_mltp = "stone_block"
					if block_pick == 3: block_texture = brick_block; block_mltp = "brick_block"
					if block_pick == 4: block_texture = dirt_block; block_mltp = "dirt_block"
					if block_pick == 5: block_texture = bedrock_block; block_mltp = "bedrock_block"
					if block_pick == 6: block_texture = glass_block; block_mltp = "glass_block"
					if block_pick == 7: block_texture = basic_wood_block; block_mltp = "basic_wood_block"
					if block_pick == 8: block_texture = basic_wood_planks_block; block_mltp = "basic_wood_planks_block"
					block = block_texture(position = self.position + mouse.normal)
					client.send_message("BlockUpdate", {"action": "place", "block": block_mltp, "position": self.position + mouse.normal})
					print("sended Block Update")
			if key == 'left mouse down':
				if player.enabled == True:
					punch_sound.play()
					client.send_message("BlockUpdate", {"action": "casse", "block": self.block_type, "position": self.position})
					destroy(self)
					all_blocks.remove(self)

class brick_block(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/rs/objects/block',
			origin_y = 0.5,
			texture = brick_texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			highlight_color = color.lime,
			scale = 0.5,
			collider = 'box')
		all_blocks.append(self)
		self.block_type = 'brick_block'
				
	def update(self):
		global prev_player_position
		if player.position is None or distance(player.position, prev_player_position) > refresh_rate:
			prev_player_position = player.position
			for block in all_blocks:
				dist = distance(block.position, player.position)
				if dist < render_distance:
					if block.position in deactivated_blocks:
						deactivated_blocks.remove(block.position)
					block.visible = True
					block.ignore = False
					block.enabled = True
				else:
					if block.position not in deactivated_blocks:
						deactivated_blocks.append(block.position)
					block.visible = False
					block.ignore = True
					block.enabled = False
	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':
				if player.enabled == True:
					punch_sound.play()
					if block_pick == 1: block_texture = grass_block; block_mltp = "grass_block"
					if block_pick == 2: block_texture = stone_block; block_mltp = "stone_block"
					if block_pick == 3: block_texture = brick_block; block_mltp = "brick_block"
					if block_pick == 4: block_texture = dirt_block; block_mltp = "dirt_block"
					if block_pick == 5: block_texture = bedrock_block; block_mltp = "bedrock_block"
					if block_pick == 6: block_texture = glass_block; block_mltp = "glass_block"
					if block_pick == 7: block_texture = basic_wood_block; block_mltp = "basic_wood_block"
					if block_pick == 8: block_texture = basic_wood_planks_block; block_mltp = "basic_wood_planks_block"
					block = block_texture(position = self.position + mouse.normal)
					client.send_message("BlockUpdate", {"action": "place", "block": block_mltp, "position": self.position + mouse.normal})
					print("sended Block Update")
			if key == 'left mouse down':
				if player.enabled == True:
					punch_sound.play()
					client.send_message("BlockUpdate", {"action": "casse", "block": self.block_type, "position": self.position})
					destroy(self)
					all_blocks.remove(self)

class dirt_block(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/rs/objects/block',
			origin_y = 0.5,
			texture = dirt_texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			highlight_color = color.lime,
			scale = 0.5,
			collider = 'box')
		all_blocks.append(self)
		self.block_type = 'dirt_block'
				
	def update(self):
		global prev_player_position
		if player.position is None or distance(player.position, prev_player_position) > refresh_rate:
			prev_player_position = player.position
			for block in all_blocks:
				dist = distance(block.position, player.position)
				if dist < render_distance:
					if block.position in deactivated_blocks:
						deactivated_blocks.remove(block.position)
					block.visible = True
					block.ignore = False
					block.enabled = True
				else:
					if block.position not in deactivated_blocks:
						deactivated_blocks.append(block.position)
					block.visible = False
					block.ignore = True
					block.enabled = False
	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':
				if player.enabled == True:
					punch_sound.play()
					if block_pick == 1: block_texture = grass_block; block_mltp = "grass_block"
					if block_pick == 2: block_texture = stone_block; block_mltp = "stone_block"
					if block_pick == 3: block_texture = brick_block; block_mltp = "brick_block"
					if block_pick == 4: block_texture = dirt_block; block_mltp = "dirt_block"
					if block_pick == 5: block_texture = bedrock_block; block_mltp = "bedrock_block"
					if block_pick == 6: block_texture = glass_block; block_mltp = "glass_block"
					if block_pick == 7: block_texture = basic_wood_block; block_mltp = "basic_wood_block"
					if block_pick == 8: block_texture = basic_wood_planks_block; block_mltp = "basic_wood_planks_block"
					block = block_texture(position = self.position + mouse.normal)
					client.send_message("BlockUpdate", {"action": "place", "block": block_mltp, "position": self.position + mouse.normal})
					print("sended Block Update")
			if key == 'left mouse down':
				if player.enabled == True:
					punch_sound.play()
					client.send_message("BlockUpdate", {"action": "casse", "block": self.block_type, "position": self.position})
					destroy(self)
					all_blocks.remove(self)

class bedrock_block(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/rs/objects/block',
			origin_y = 0.5,
			texture = bedrock_texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			highlight_color = color.lime,
			scale = 0.5,
			collider = 'box')
		all_blocks.append(self)
		self.block_type = 'bedrock_block'
				
	def update(self):
		global prev_player_position
		if player.position is None or distance(player.position, prev_player_position) > refresh_rate:
			prev_player_position = player.position
			for block in all_blocks:
				dist = distance(block.position, player.position)
				if dist < render_distance:
					if block.position in deactivated_blocks:
						deactivated_blocks.remove(block.position)
					block.visible = True
					block.ignore = False
					block.enabled = True
				else:
					if block.position not in deactivated_blocks:
						deactivated_blocks.append(block.position)
					block.visible = False
					block.ignore = True
					block.enabled = False
	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':
				if player.enabled == True:
					punch_sound.play()
					if block_pick == 1: block_texture = grass_block
					if block_pick == 2: block_texture = stone_block
					if block_pick == 3: block_texture = brick_block
					if block_pick == 4: block_texture = dirt_block
					if block_pick == 5: block_texture = bedrock_block
					if block_pick == 6: block_texture = glass_block
					if block_pick == 7: block_texture = basic_wood_block
					if block_pick == 8: block_texture = basic_wood_planks_block
					block = block_texture(position = self.position + mouse.normal)
					client.send_message("BlockUpdate", {"action": "place", "block": block_texture, "position": self.position + mouse.normal})
			if key == 'left mouse down':
				if player.enabled == True:
					punch_sound.play()

class glass_block(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/rs/objects/block',
			origin_y = 0.5,
			texture = glass_texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			highlight_color = color.lime,
			scale = 0.5,
			collider = 'box')
		all_blocks.append(self)
		self.block_type = 'glass_block'
				
	def update(self):
		global prev_player_position
		if player.position is None or distance(player.position, prev_player_position) > refresh_rate:
			prev_player_position = player.position
			for block in all_blocks:
				dist = distance(block.position, player.position)
				if dist < render_distance:
					if block.position in deactivated_blocks:
						deactivated_blocks.remove(block.position)
					block.visible = True
					block.ignore = False
					block.enabled = True
				else:
					if block.position not in deactivated_blocks:
						deactivated_blocks.append(block.position)
					block.visible = False
					block.ignore = True
					block.enabled = False
	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':
				if player.enabled == True:
					punch_sound.play()
					if block_pick == 1: block_texture = grass_block; block_mltp = "grass_block"
					if block_pick == 2: block_texture = stone_block; block_mltp = "stone_block"
					if block_pick == 3: block_texture = brick_block; block_mltp = "brick_block"
					if block_pick == 4: block_texture = dirt_block; block_mltp = "dirt_block"
					if block_pick == 5: block_texture = bedrock_block; block_mltp = "bedrock_block"
					if block_pick == 6: block_texture = glass_block; block_mltp = "glass_block"
					if block_pick == 7: block_texture = basic_wood_block; block_mltp = "basic_wood_block"
					if block_pick == 8: block_texture = basic_wood_planks_block; block_mltp = "basic_wood_planks_block"
					block = block_texture(position = self.position + mouse.normal)
					client.send_message("BlockUpdate", {"action": "place", "block": block_mltp, "position": self.position + mouse.normal})
					print("sended Block Update")
			if key == 'left mouse down':
				if player.enabled == True:
					punch_sound.play()
					client.send_message("BlockUpdate", {"action": "casse", "block": self.block_type, "position": self.position})
					destroy(self)
					all_blocks.remove(self)

class basic_wood_block(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/rs/objects/block',
			origin_y = 0.5,
			texture = basic_wood_texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			highlight_color = color.lime,
			scale = 0.5,
			collider = 'box')
		all_blocks.append(self)
		self.block_type = 'basic_wood_block'
				
	def update(self):
		global prev_player_position
		if player.position is None or distance(player.position, prev_player_position) > refresh_rate:
			prev_player_position = player.position
			for block in all_blocks:
				dist = distance(block.position, player.position)
				if dist < render_distance:
					if block.position in deactivated_blocks:
						deactivated_blocks.remove(block.position)
					block.visible = True
					block.ignore = False
					block.enabled = True
				else:
					if block.position not in deactivated_blocks:
						deactivated_blocks.append(block.position)
					block.visible = False
					block.ignore = True
					block.enabled = False
	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':
				if player.enabled == True:
					punch_sound.play()
					if block_pick == 1: block_texture = grass_block; block_mltp = "grass_block"
					if block_pick == 2: block_texture = stone_block; block_mltp = "stone_block"
					if block_pick == 3: block_texture = brick_block; block_mltp = "brick_block"
					if block_pick == 4: block_texture = dirt_block; block_mltp = "dirt_block"
					if block_pick == 5: block_texture = bedrock_block; block_mltp = "bedrock_block"
					if block_pick == 6: block_texture = glass_block; block_mltp = "glass_block"
					if block_pick == 7: block_texture = basic_wood_block; block_mltp = "basic_wood_block"
					if block_pick == 8: block_texture = basic_wood_planks_block; block_mltp = "basic_wood_planks_block"
					block = block_texture(position = self.position + mouse.normal)
					client.send_message("BlockUpdate", {"action": "place", "block": block_mltp, "position": self.position + mouse.normal})
					print("sended Block Update")
			if key == 'left mouse down':
				if player.enabled == True:
					punch_sound.play()
					client.send_message("BlockUpdate", {"action": "casse", "block": self.block_type, "position": self.position})
					destroy(self)
					all_blocks.remove(self)

class basic_wood_planks_block(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/rs/objects/block',
			origin_y = 0.5,
			texture = basic_wood_planks_texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			highlight_color = color.lime,
			scale = 0.5,
			collider = 'box')
		all_blocks.append(self)
		self.block_type = 'basic_wood_planks_block'
				
	def update(self):
		global prev_player_position
		if player.position is None or distance(player.position, prev_player_position) > refresh_rate:
			prev_player_position = player.position
			for block in all_blocks:
				dist = distance(block.position, player.position)
				if dist < render_distance:
					if block.position in deactivated_blocks:
						deactivated_blocks.remove(block.position)
					block.visible = True
					block.ignore = False
					block.enabled = True
				else:
					if block.position not in deactivated_blocks:
						deactivated_blocks.append(block.position)
					block.visible = False
					block.ignore = True
					block.enabled = False
	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':
				if player.enabled == True:
					punch_sound.play()
					if block_pick == 1: block_texture = grass_block; block_mltp = "grass_block"
					if block_pick == 2: block_texture = stone_block; block_mltp = "stone_block"
					if block_pick == 3: block_texture = brick_block; block_mltp = "brick_block"
					if block_pick == 4: block_texture = dirt_block; block_mltp = "dirt_block"
					if block_pick == 5: block_texture = bedrock_block; block_mltp = "bedrock_block"
					if block_pick == 6: block_texture = glass_block; block_mltp = "glass_block"
					if block_pick == 7: block_texture = basic_wood_block; block_mltp = "basic_wood_block"
					if block_pick == 8: block_texture = basic_wood_planks_block; block_mltp = "basic_wood_planks_block"
					block = block_texture(position = self.position + mouse.normal)
					client.send_message("BlockUpdate", {"action": "place", "block": block_mltp, "position": self.position + mouse.normal})
					print("sended Block Update")
			if key == 'left mouse down':
				if player.enabled == True:
					punch_sound.play()
					client.send_message("BlockUpdate", {"action": "casse", "block": self.block_type, "position": self.position})
					destroy(self)
					all_blocks.remove(self)

block_classes = {'grass_block': grass_block, 'stone_block': stone_block, 'brick_block': brick_block, 'dirt_block': dirt_block, 'bedrock_block': bedrock_block, 'glass_block': glass_block, 'basic_wood_block': basic_wood_block, 'basic_wood_planks_block': basic_wood_planks_block}

def save_world():
	with open('../../worlds/{}/world.pcw'.format(worldname), 'w') as file:
		for voxel in all_blocks:
			file.write(f'{voxel.position}:{voxel}\n')
@client.event
def load_world(world_data_json):
	world_data = json.loads(world_data_json)
	for position_str, texture in world_data.items():
		position = tuple(map(int, position_str.strip('()').split(', ')))
		loadworldblock = block_classes[texture]
		voxel = loadworldblock(position=position)
		print("World Loaded!!!")

#EscMenu
def input(key):
	global fullscreen
	global camera_pos
	if key == 'escape':
		if isplayerkilled == False:
			global escmenuenabled
			global escmenuquitb
			global escmenuretb
			global retb
			if escmenuenabled == False:
				player.enabled = False
				escmenuenabled = True
				escmenuquitb=Button(text="Quit The Game", color=color.lime, text_color=color.gray, scale=.25, position=(.0,-.2))
				escmenuquitb.tooltip=Tooltip("Click here for quit the game")
				escmenuquitb.on_click = application.quit
				escmenuretb=Button(text="Return to The Game", color=color.lime, text_color=color.gray, scale=.25, position=(.0,.2))
				escmenuretb.tooltip=Tooltip("Click here for return to the game")
				escmenuretb.on_click = returntogame
				escmenuenabled = True
			else:
				player.enabled = True
				retb = True
				escmenuenabled = False
				destroy(escmenuquitb)
				destroy(escmenuretb)
	if key == 'b':
		crash()	
	if key == 'c':
		if camera_pos == "normal":
			camera_pos = "before"
			camera.position = player.position + Vec3(0, 0, -2)
		else:
			camera_pos = "normal"
			camera.position = player.position
	if key == 'y':
		save_world()
	if key == 'x':
		load_world()
	if key == 'f11':
		if fullscreen:
			window.fullscreen = False
			fullscreen = False
			window.size = (800,600)
			print("Disabled Fullscreen")
		else:
			window.fullscreen = True
			fullscreen = True
			print("Enabled Fullscreen")

#Sky
class Sky(Entity):
	def __init__(self):
		super().__init__(
		parent = scene,
		model = 'sphere',
		texture = sky_texture,
		scale = 150,
		double_sided = True)
	def update(self):
		self.position = player.position
#Hand
class RightHand(Entity):
	def __init__(self):
		super().__init__(
		parent = camera.ui,
		model = 'assets/rs/objects/arm',
		texture = arm_texture,
		scale = 0.2,
		rotation = Vec3(150,-10,0),
		position = Vec2(0.4,-0.6))
		
	def active(self):
		self.position = Vec2(0.3,-0.5)
		
	def passive(self):
		self.position = Vec2(0.4,-0.6)
		
class LeftHand(Entity):
	def __init__(self):
		super().__init__(
		parent = camera.ui,
		model = 'assets/rs/objects/arm',
		texture = arm_texture,
		scale = 0.2,
		rotation = Vec3(150,10,0),
		position = Vec2(-0.4,-0.6))
	def active(self):
		self.position = Vec2(-0.3, -0.5)
	def passive(self):
		self.position = Vec2(-0.4,-0.6)
			
def move_entity(e1=ra, e2=player, speed=1.5, gravity=-0.1, y_velocity=0, power=1, isdamaging=True, knowback=True, collisions=True):
	if player.enabled == True:
		direction = (e2.position - e1.position).normalized()
		distance = (e2.position - e1.position).length()
		e1.rotation_y = atan2(direction.x, direction.z) * 180 / pi
		if distance > 1:
			e1.position += direction + Vec3(0, gravity, 0)* speed * time.dt
		if distance < 1:
			if isdamaging == True:
				damage(power)
				if knowback == True:
					e1.position = e1.position + Vec3(1, 0.5, 1)
		if collisions == True:
			hit_info = e1.intersects()
			if hit_info.hit:
				e1.position = e1.position + Vec3(0, 0.1, 0)
				print("AAAH, BBBBBBBh")
	
camera.position = player.position
camera.rotation = player.rotation
		
sky = Sky()
righthand = RightHand()
lefthand = LeftHand()
capl = CameraPlayer()


time.sleep(5)
app.run()
