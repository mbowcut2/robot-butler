import openai
import secrets

class Robot:
	"""
	This is the agent. It will receive NL instructions from the user and then perform actions in the environment.
	"""
	API_KEY = "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"
	openai.api_key = API_KEY

	def __init__(self, state):
		API_KEY = secrets.secrets.API_KEY
		openai.api_key = API_KEY

		self.prompt = ""
		self.task = ""
		self.state = state

	def call_api(self):
		response = openai.Completion.create(
			engine="text-davinci-002",
			prompt=self.prompt,
			temperature=0.7,
			max_tokens=256,
			top_p=1,
			best_of=1,
			frequency_penalty=0,
			presence_penalty=0
			)
		verbose = False
		if verbose:
			print("PROMPT: ",self.prompt)
			print(response)
		self.action= response['choices'][0]['text']

	def get_instruction(self):
		self.prompt = self.state
		self.task = input("Please specify a task: ")
		self.prompt += f"The following are steps to {self.task}:"
	def get_feedback(self):
		feedback = input("Please provide feedback: ")
		self.prompt += f"\n{feedback} so to {self.task} you should:" #TODO: we might want to append this to state? Not sure what that will be in the future.
	def propose_action(self):
		while True:
			self.call_api()
			user_in = input(f"{self.action} -- type enter to try again / y to proceed: ")
			if user_in == 'y':
				self.prompt += self.action + '\n'
				break


if __name__ == '__main__':
	robot = Robot()
