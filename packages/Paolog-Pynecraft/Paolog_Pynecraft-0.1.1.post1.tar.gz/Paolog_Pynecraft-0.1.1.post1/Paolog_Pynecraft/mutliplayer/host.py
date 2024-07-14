from ursinanetworking import *
import threading
import sys
import json
running = True

world = sys.argv[1]

server = UrsinaNetworkingServer("localhost", 28123)

print("Welcome to Pynecraft Server Console.")
print("Type ser_help() for help")
def get_world_data(world):
	print("Getting World Data")
	world_data = {}
	with open('{}/world.pcw'.format(world), 'r') as file:
		lines = file.readlines()
		for line in lines:
			line = line.strip()
			if line:
				position, texture = line.split(':')
				position = tuple(map(int, position.replace('Vec3(', '').replace(')', '').split(',')))
				world_data[str(position)] = texture
	return world_data

@server.event
def BlockUpdate(client, Content):
	action = Content["action"]
	block = Content["block"]
	position = Content["position"]
	print(f"Recieved block from {client}: action:{action}, block:{block}, position:{position}")
	server.broadcast("MakeServerBlock", {"action": action, "block": block, "position": position})
	print(block)
@server.event
def onClientConnected(client):
	print(f"{client} connected")
	world_data = get_world_data(world)
	client.send_message("load_world", json.dumps(world_data))
@server.event
def get_player_coordinates(client, Content):
	print(Content)
def process_net_events():
	while running:
		server.process_net_events()
		time.sleep(0.1)
net_thread = threading.Thread(target=process_net_events)
net_thread.start()

def stop_server():
	global running
	print("Shutting Down Server")
	for client in server.clients:
		client.disconnect()
	server.socket.close()
	running = False
	net_thread.join()
	quit()
	exit()
def ser_help():
	print("Pynecraft Server Console(PSC) Help:")
	print("In PSC, you can execute command, and you can execute python script")
	print("Avaiable Command:")
	print("stop_server; ser_help")
	#print("Command to put: disconnect_client; ban_client; kick_client; ")
	print("Good python command for your server:")
	print("client.send_message(DEF, MESSAGE): for send message to a client")
	print("server.broadcast(DEF, MESSAGE): for send message to all client")

def process_command(command):
	if command == "crash":
		my_command()
	else:
		try:
			result = eval(command)
			print(result)
		except:
			try:
				exec(command)
			except Exception as e:
				print(f"Error: {e}")
	
while True:
	command = input("$> ")
	process_command(command)