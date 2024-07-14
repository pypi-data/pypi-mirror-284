# Import game-related Objects
from ursina import Vec3, Vec2, camera, scene, mouse, distance
# Import Widget-related Objects
from ursina import Entity, Button, window, destroy
# Import Resources-related Objects
from ursina import Audio, color, load_texture
# Import FirstPersonController
from ursina.prefabs.first_person_controller import FirstPersonController

# Import math-related Objects
from math import atan2
import time
from ursina import random, pi

# Import Pynecraft Widgets
from ...UI.button import PyneButton
from ...UI.bar import PyneBar
from ...other.quit import PyneQuit

class Pynecraft:
    def __init__(self, menu_manager, world:str, username:str):
        self.menu_manager = menu_manager

        global player
        player = FirstPersonController()
        spawn_position = player.position #get spawn position
        global HB
        HB = PyneBar(color=color.red, ySize=.05, xSize=.6, yPos=-.35, xPos=-.6, max_value=20)
        sky_day_texture = load_texture('assets/rs/images/skybox_day.png')
        sky_night_texture = load_texture('assets/rs/images/skybox_night.png')
        punch_sound = Audio('assets/rs/sounds/punch_sound',loop = False, autoplay = False)
        glass_sound = Audio('assets/rs/sounds/glass_sound',loop = False, autoplay = False)
        boss1_sound = Audio('assets/rs/sounds/boss1', loop = True, autoplay = True)
        kill_sound = Audio('assets/rs/sounds/kill', loop = False, autoplay = False)
        crash_sound = Audio('assets/rs/sounds/kill', loop = True, autoplay = False)
        global block_pick
        block_pick = 1
        #sky_texture = sky_night_texture
        sky_texture = sky_day_texture
        global escmenuenabled
        escmenuenabled = False
        global isplayerkilled
        isplayerkilled = False
        global retb
        retb = False
        global cameraposition
        cameraposition = "normal"

        #render_distance = 25
        render_distance = 6

        worldname = world

        global kill
        def kill():
            global isplayerkilled
            global respawnb
            global quitb
            isplayerkilled = True
            if isplayerkilled == True:
                player.enabled = False
                quitb = PyneButton(text="Quit The Game", xPos=.0, yPos=-.1, ySize=.07, xSize=.4, onClick=PyneQuit, tooltip="Click here to quit the game")
                respawnb = PyneButton(text="Respawn", xPos=.0, yPos=.1, ySize=.07, xSize=.4, onClick=respawn, tooltip="Click here to respawn")
                kill_sound.play()
            
        def damage(power):
            HB.set_value(HB.get_value() - power)
            
        def heal(power):
            HB.set_value(HB.get_value() + power)
        
        global returntogame
        def returntogame():
            global escmenuenabled
            player.enabled = True
            escmenuenabled = False
            retb = True
            escmenuquitb.killMe()
            escmenuretb.killMe()
            saveworldbtn.killMe()
        
        global respawn
        def respawn():
            global isplayerkilled
            global quitb
            global respawnb
            player.enabled = True
            HB.set_value(HB.get_max_value())
            isplayerkilled = False
            quitb.killMe()
            respawnb.killMe()
            player.position = spawn_position
            
        
        #mob    
        #set mob to an acronyme for move_entity
        #mob code
        class RickAstley(Entity):
            def __init__(self, position = (0,3,0)):
                super().__init__(
                    parent = scene,
                    position = position,
                    model = 'assets/rs/objects/default_obj',
                    texture = 'assets/rs/images/ra2',
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
                    texture = 'assets/rs/images/ra2',
                    scale = 2.75,
                    collider = "box")
        mra = MiniRickAsltey()
                
        class Cursor(Entity):
            def __init__(self):
                super().__init__(
                    parent = camera.ui,
                    position = (0, 0),
                    texture = 'assets/rs/images/cursor.png',
                    model = 'quad',
                    scale = 32 / (window.aspect_ratio * 600),
                    color = color.white
                )
                self.always_on_top_setter(True)
            def update(self):
                if (player.enabled):
                    self.position_setter((0,0))
                else:
                    self.position_setter((mouse.x, mouse.y))
                    mouse.visible = False
        
        global cursor
        cursor = Cursor()

        #blocks    
        deactivated_blocks = []
        all_blocks = []
        global prev_player_position
        prev_player_position = player.position
        refresh_rate = render_distance / 2

        # Base Block class
        class Block(Button):
            def __init__(self, texture, position=(0, 0, 0)):
                super().__init__(
                    parent=scene,
                    position=position,
                    model='assets/rs/objects/block',
                    origin_y=0.5,
                    texture=texture,
                    color=color.color(0, 0, random.uniform(0.9, 1)),
                    #highlight_color=color.lime,
                    #highlight_color=color.rgba(255,255,255,.5),
                    highlight_color=color.white,
                    scale=0.5,
                    collider='box'
                )
                self.block_texture = texture
                self.is_destroyed = False  # Add a flag to track if the block is destroyed
                all_blocks.append(self)

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
                            block.visible = True
                            block.ignore = True
                            block.enabled = True

            def input(self, key):
                if self.hovered:
                    if key == 'right mouse down' and player.enabled:
                        self.play_create_sound()
                        if block_pick == 1: block_texture = GrassBlock
                        if block_pick == 2: block_texture = StoneBlock
                        if block_pick == 3: block_texture = BrickBlock
                        if block_pick == 4: block_texture = DirtBlock
                        if block_pick == 5: block_texture = BedrockBlock
                        if block_pick == 6: block_texture = GlassBlock
                        if block_pick == 7: block_texture = BasicWoodBlock
                        if block_pick == 8: block_texture = BasicWoodBlockPlanks
                        block = block_texture(position = self.position + mouse.normal)
                    elif key == 'left mouse down' and player.enabled:
                        self.play_destroy_sound()
                        self.on_destroy()
            
            def play_create_sound(self):
                punch_sound.play()
            
            def play_destroy_sound(self):
                punch_sound.play()

            def on_destroy(self):
                if self.is_destroyed:
                    pass # The block is already destroyed
                else:
                    self.is_destroyed = True
                    destroy(self)

                    all_blocks.remove(self)

        # Specific block types
        class GrassBlock(Block):
            def __init__(self, position=(0, 0, 0)):
                super().__init__(texture='assets/rs/images/grass_block.png', position=position)

        class StoneBlock(Block):
            def __init__(self, position=(0, 0, 0)):
                super().__init__(texture='assets/rs/images/stone_block.png', position=position)

        class BrickBlock(Block):
            def __init__(self, position=(0, 0, 0)):
                super().__init__(texture='assets/rs/images/brick_block.png', position=position)

        class DirtBlock(Block):
            def __init__(self, position=(0, 0, 0)):
                super().__init__(texture='assets/rs/images/dirt_block.png', position=position)

        class BedrockBlock(Block):
            def __init__(self, position=(0, 0, 0)):
                super().__init__(texture='assets/rs/images/bedrock_block.png', position=position)
            
            def on_destroy(self):
                # Bedrock can't be destroyed
                pass

        class GlassBlock(Block):
            def __init__(self, position=(0, 0, 0)):
                super().__init__(texture='assets/rs/images/glass_block.png', position=position)
            
            def play_destroy_sound(self):
                # Play glass destroying sound
                glass_sound.play()

        class BasicWoodBlock(Block):
            def __init__(self, position=(0, 0, 0)):
                super().__init__(texture='assets/rs/images/basic_wood_block.png', position=position)

        class BasicWoodBlockPlanks(Block):
            def __init__(self, position=(0, 0, 0)):
                super().__init__(texture='assets/rs/images/basic_wood_planks_block.png', position=position)

        global save_world
        def save_world():
            with open('{}/world.pcw'.format(worldname), 'w') as file:
                for i, voxel in enumerate(all_blocks, 1):
                    file.write(f'{voxel.position}:{type(voxel).__name__}\n')
                    saveworldbtn.button.text = "Finished saving world"

        def load_world():
            block_classes = {'GrassBlock': GrassBlock, 'StoneBlock': StoneBlock, 'BrickBlock': BrickBlock, 'DirtBlock': DirtBlock, 'BedrockBlock': BedrockBlock, 'GlassBlock': GlassBlock, 'BasicWoodBlock': BasicWoodBlock, 'BasicWoodBlockPlanks': BasicWoodBlockPlanks}
            try :
                with open('{}/world.pcw'.format(worldname), 'r') as file:
                    lines = file.readlines()
                    line_id = 0
                    for line in lines:
                        line_id = line_id + 1
                        total_lines = len(open('{}/world.pcw'.format(worldname), 'r').readlines())
                        print((line_id * 100) / total_lines)
                        line = line.strip()
                        if line:
                            position, texture = line.split(':')
                            position = tuple(map(int, position.replace('Vec3(', '').replace(')', '').split(',')))
                            loadworldblock = block_classes[texture]
                            voxel = loadworldblock(position=position)
            except FileNotFoundError :
                """ print("startng world resetting...")
                default_world = open('worlds/default/world.pcw', "r")
                open('{}/world.pcw'.format(worldname), "w").writelines(default_world)
                load_world() """
                print("world.pcw not found in your world.")
                PyneQuit(1)

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
                texture = 'assets/rs/images/arm_texture.png',
                scale = 0.2,
                rotation = Vec3(150,-10,0))
                
            def active(self):
                self.position = Vec2(0.4,-0.5)
                
            def passive(self):
                self.position = Vec2(0.5,-0.6)
                
        class LeftHand(Entity):
            def __init__(self):
                super().__init__(
                parent = camera.ui,
                model = 'assets/rs/objects/arm',
                texture = 'assets/rs/images/arm_texture.png',
                scale = 0.2,
                rotation = Vec3(150,10,0))
            def active(self):
                self.position = Vec2(-0.4 + self.scale_x_getter(), -0.5)
            def passive(self):
                self.position = Vec2(-0.5 + self.scale_x_getter() ,-0.6)
                ## Why does I add a +self.scale_x_getter() ?
                ## Because the origin of 3D model is at right top, so to left hand I need to add the width of the object to be centered
                
                
        load_world()
 
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
        global righthand
        righthand = RightHand()
        global lefthand
        lefthand = LeftHand()

    def update(self):
            global block_pick
            if HB.get_value() == 0 and isplayerkilled == False:
                kill()

            player.cursor.disable()
    
    def input(self, key):
            global block_pick
            global fullscreen
            global camera_pos
            if key == 'escape':
                if isplayerkilled == False:
                    global escmenuenabled
                    global escmenuquitb
                    global escmenuretb
                    global saveworldbtn
                    global saveworldbtn
                    global retb
                    if escmenuenabled == False:
                        player.enabled = False
                        escmenuenabled = True
                        saveworldbtn = PyneButton(text="Save World", xPos=.0, yPos=.15, ySize=.07, xSize=.4, onClick=save_world, tooltip="Click here to save world")
                        escmenuretb = PyneButton(text="Return to The Game", xPos=.0, yPos=0, ySize=.07, xSize=.4, onClick=returntogame, tooltip="Click here to return to the game")
                        escmenuquitb = PyneButton(text="Quit The Game", xPos=.0, yPos=-.15, ySize=.07, xSize=.4, onClick=PyneQuit, tooltip="Click here to quit the game")
                        escmenuenabled = True
                    else:
                        player.enabled = True
                        retb = True
                        escmenuenabled = False
                        escmenuquitb.killMe()
                        escmenuretb.killMe()
                        saveworldbtn.killMe()
            if key == 'b':
                PyneQuit()
            if key == 'r':
                respawn()
            if key == 'k':
                kill()

            if key == "1": block_pick = 1
            if key == "2": block_pick = 2
            if key == "3": block_pick = 3
            if key == "4": block_pick = 4
            if key == "5": block_pick = 5
            if key == "6": block_pick = 6
            if key == "7": block_pick = 7
            if key == "8": block_pick = 8

            if key == "left mouse down" and player.enabled:
                lefthand.active()
            else:
                lefthand.passive()
            
            if key == "right mouse down" and player.enabled:
                righthand.active()
            else:
                righthand.passive()
    
    def show(self):
        pass
    
    def hide(self):
        pass

    def killMe(self):
        pass