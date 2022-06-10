import openai

class Robot:
	"""
	This is the agent. It will receive NL instructions from the user and then perform actions in the environment.
	"""
	API_KEY = "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"
	openai.api_key = API_KEY

	def __init__(self, state):
		API_KEY = "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"
		openai.api_key = API_KEY

		self.prompt = state

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
		print("PROMPT: ",self.prompt)
		print(response)
		self.action= response['choices'][0]['text']

	def get_instruction(self):
		task = input("Please specify a task: ")
		self.prompt = f"The following are steps to {task}: \n1."
	def propose_action(self):
		while True:
			self.call_api()
			user_in = input(f"{self.action} -- type enter to try again / x to terminate: ")
			if user_in == 'x':
				break


if __name__ == '__main__':
	robot = Robot()
