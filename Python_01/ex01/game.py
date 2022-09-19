import sys

class GotCharacter:
	def __init__(self, first_name: str, is_alive = True):
		self.is_alive = is_alive
		self.first_name = first_name



class Stark(GotCharacter):
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"

	def print_house_words(self):
		print(self.house_words)
	def die(self):
		self.is_alive = False


class Griffondor(GotCharacter):
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Potter"
		self.house_words = "100 points to Griffodor"

	def print_house_words(self):
		print(self.house_words)
	def die(self):
		self.is_alive = False

class Hobbits(GotCharacter):
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Sacquet"
		self.house_words = "In a hole in the ground there lived a hobbit."

	def print_house_words(self):
		print(self.house_words)
	def die(self):
		self.is_alive = False


arya = Stark("Arya")
print(arya.__dict__)
arya.print_house_words()
print(arya.is_alive)
arya.die()
print(arya.is_alive)


harry = Griffondor("Harry")
print(harry.__dict__)
harry.print_house_words()
print(harry.is_alive)
harry.die()
print(harry.is_alive)

frodo = Hobbits("Frodo")
print(frodo.__dict__)
frodo.print_house_words()
print(frodo.is_alive)
frodo.die()
print(frodo.is_alive)