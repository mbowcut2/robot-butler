# API_KEY = "4fmIjFPuqvAuM1ZAP0g5T3BlbkFJi51AxBpNK8MYAG482mIg" # TODO: don't make this public
import grammar
import openai
import random
from robot import Robot

class Environment:
	"""
	This is the text environment that interacts with the user and the robot.

	It should initialize the robot and act as a sort of narrator/DM. If the the goal is to simulate an agent in a physical environment, then we may wish to populate this text environment with objects that the robot can perceive and interact with.


	"""


	def __init__(self):
		API_KEY = "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"
		openai.api_key = API_KEY

		print("initializing environment...", end=" ")
		room = random.choice(grammar.ROOMS)
		object1 = random.choice(grammar.OBJECTS)
		object2 = random.choice(grammar.OBJECTS)
		object3 = random.choice(grammar.UNUSUAL_OBJECTS)
		self.state = f"You are in the {room}. You look around and see a {object1} a {object2} and a {object3}. \n"
		print("done")
		print(self.state)


if __name__ == '__main__':
	env = Environment()
	robot = Robot(env.state)
	robot.get_instruction()
	proposed_action = robot.propose_action()
