class GotCharacter:
	'''A class representing the GoT's characters. But I prefer Harry Potter and LotR.'''
	def __init__(self, first_name=None, is_alive = True):
		self.first_name = first_name
		self.is_alive = is_alive



class Stark(GotCharacter):
	'''A class representing the Stark family. Or when bad things happen to good people.'''
	
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"

	def print_house_words(self):
		print(self.house_words)
	def die(self):
		self.is_alive = False


class Gryffindor(GotCharacter):
	'''A class representing the Griffindor house. Or the most privileged house of Hogwarts.'''
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Potter"
		self.house_words = "100 points to Gryffindor"

	def print_house_words(self):
		print(self.house_words)
	def die(self):
		self.is_alive = False

class Hobbits(GotCharacter):
	'''A class representing the Hobbit race. Or people with hairy feet'''
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Sacquet"
		self.house_words = "In a hole in the ground there lived a hobbit. Or the most powerfull race !!!"

	def print_house_words(self):
		print(self.house_words)
	def die(self):
		self.is_alive = False
