# API_KEY = "4fmIjFPuqvAuM1ZAP0g5T3BlbkFJi51AxBpNK8MYAG482mIg" # TODO: don't make this public
import grammar
import openai
import random
from secrets import secrets
from robot import Robot

class Environment:
	"""
	This is the text environment that interacts with the user and the robot.

	It should initialize the robot and act as a sort of narrator/DM. If the the goal is to simulate an agent in a physical environment, then we may wish to populate this text environment with objects that the robot can perceive and interact with.


	"""


	def __init__(self):

		openai.api_key = secrets.API_KEY

		print("initializing environment...", end=" ")
		room = random.choice(grammar.ROOMS)
		room_objects = random.sample(grammar.OBJECTS[room], 4)
		floor_objects = random.sample(grammar.OBJECTS['floor'], 4)
		object1 = random.choice(grammar.OBJECTS[room]) #TODO: get rid of duplicates
		object2 = random.choice(grammar.OBJECTS[room])
		object3 = random.choice(grammar.OBJECTS[room])
		object4 = random.choice(grammar.OBJECTS[room])
		object5 = random.choice(grammar.OBJECTS['floor'])
		object6 = random.choice(grammar.OBJECTS['floor'])
		object7 = random.choice(grammar.OBJECTS['floor'])
		object8 = random.choice(grammar.OBJECTS['floor'])
		self.state = f"You are in the {room}. You look around and see a {room_objects[0]}, a {room_objects[1]}, a {room_objects[2]} and a {room_objects[3]}. There is a {floor_objects[0]}, {floor_objects[1]}, {floor_objects[2]}, and {floor_objects[3]} on the floor. \n"
		print("done \n \n")
		print(self.state)


if __name__ == '__main__':
	env = Environment()
	robot = Robot(env.state)
	while True:
		robot.get_instruction()
		proposed_action = robot.propose_action()
		while True:
			user_in = input("Do you wish to provide feedback? (y/n/prompt) ")
			if user_in == 'prompt':
				print('\n *****************************************')
				print(robot.prompt)
				print('\n *****************************************')
			elif user_in == 'y':
				robot.get_feedback()
				robot.propose_action()
			else:
				break
		print('\n \n', env.state)
		user_in = input('Press enter to provide another task or type exit to terminate: ')
		if user_in == 'exit':
			break
