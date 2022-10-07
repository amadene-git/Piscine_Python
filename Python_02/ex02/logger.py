import time
from random import randint
import os

def deco(cl):
	print("ut")
	return cl

# @deco
class a():
	def __init__(self) -> None:
		print("salut")
		pass
a = deco(a)

l = a()
l = a()

#... your definition of log decorator...
def log(function):
	def 
	print(function.__name__)
	os.system(f'echo "{os.environ["USER"]} {function.__name__}" >> machine.log')
	return function

class CoffeeMachine():
	water_level = 100
	
	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."
	
	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")
	
	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	print("************************")
	machine = CoffeeMachine()
	# print("************************")
	for i in range(0, 5):
		# print("************************")
		machine.make_coffee()
		# print("************************")
	
	print("************************")
	machine.make_coffee()
	print("************************")
	machine.add_water(70)