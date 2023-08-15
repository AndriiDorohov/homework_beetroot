# Task 3
# TV controller
# Create a simple prototype of a TV controller in Python.
# It’ll use the following commands:

# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that
# the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel
# is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current
# channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string
# 'name' and returns "Yes", if the channel N or 'name' exists in the list,
# or "No" - in the other case.


# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.

# '''
# CHANNELS = ["BBC", "Discovery", "TV1000"]
#  class TVController:
# pass
# controller = TVController(CHANNELS)
# controller.first_channel() == "BBC"
# controller.last_channel() == "TV1000"
# controller.turn_channel(1) == "BBC"
# controller.next_channel() == "Discovery"
# controller.previous_channel() == "BBC"
# controller.current_channel() == "BBC"
# controller.is_exist(4) == "No"
# controller.is_exist("BBC") == "Yes"
# '''

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
	def __init__(self, channels: list) -> None:
		self.channels = channels

	def first_channel(self) -> str:
		return self.channels[0]

	def last_channel(self) -> str:
		return self.channels[-1]

	def turn_channel(self, num: int) -> str:
		self.num = num - 1
		return self.channels[self.num]

	def next_channel(self) -> str:
		if self.num + 1 == len(self.channels):
			return self.channels[0]
		else:
			return self.channels[self.num + 1]

	def previous_channel(self) -> str:
		return self.channels[self.num - 1]

	def current_channel(self) -> str:
		return self.channels[self.num]

	def is_exist(self, cur_num) -> str:
		if type(cur_num) == int:
				return "Yes" if len(self.channels) > cur_num else "No"
		elif type(cur_num) == str:
				return "Yes" if cur_num in self.channels else "No"

controller = TVController(CHANNELS)
print(f"First channel:      {controller.first_channel()}")
print(f"Last channel:       {controller.last_channel()}")
print(f"Turn channel:       {controller.turn_channel(1)}")
print(f"Next channel:       {controller.next_channel()}")
print(f"Pervios channel:    {controller.previous_channel()}")
print(f"Current channel:    {controller.current_channel()}")
print(f"Exist 4 channel:    {controller.is_exist(4)}")
print(f"Exist BBC channel:  {controller.is_exist('BBC')}")

print(f"Current channel:    {controller.turn_channel(3)}")
print(f"Next channel:       {controller.next_channel()}")
