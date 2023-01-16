import time
from random import randint
import os

#... your definition of log decorator...
def log(funct):
	def deco(*args, **kwargs):
		t_zero = time.clock_gettime(time.CLOCK_REALTIME)
		ret = funct(*args, **kwargs)
		t_one = time.clock_gettime(time.CLOCK_REALTIME)
		t_format = t_one - t_zero
		if (t_format > 0.001):
			t_format = f"exec-time = {t_format:.3f} s"
		else:
			t_format = f"exec-time = {round(t_format * 1000, 3):.3f} ms"
		os.system(f"echo \"({os.environ.get('USER', '$USER is empty')}) Running: {funct.__name__.replace('_', ' ').title():15s}[ {t_format} ]\" >> machine.log")
		return ret
	
	return (deco)


class CoffeeMachine():
	water_level = 100
	
	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False
	# start_machine = log(start_machine)
	
	@log
	def boil_water(self):
		return "boiling..."
	# boil_water = log(boil_water)
	
	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")
	# make_coffee = log(make_coffee)
	
	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")
	# add_water = log(add_water)




if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)


