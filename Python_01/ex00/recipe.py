import sys
from typing import List

def print_error(message: str):
	print(message, file=sys.stderr)
	quit()


class Recipe:
	def __init__(self, name: str, cooking_lvl: int, cooking_time: int, recipe_type: str, ingredients = [str], description: str=""):
		
		if (len(name) == 0):
			print_error("Error Recipe: no name given")
		self.name = name						#(str)		name of the recipe,
		
		if (cooking_lvl < 1 or cooking_lvl > 5):
			print_error("Error creating Recipe '{}': cooking_lvl is not between 1 and 5".format(name))
		self.cooking_lvl = cooking_lvl			#(int):		range from 1 to 5,
		
		if (cooking_time < 0):
			print_error("Error creating Recipe '{}' : cooking_time cannot be negative value".format(name))
		self.cooking_time = cooking_time		#(int):		in minutes (no negative numbers),
		
		if (len(ingredients) == 0):
			print_error("Error creating Recipe '{}' : no ingredients given".format(name))
		for i in ingredients:
			if (len(i) == 0):
				print_error("Error creating Recipe '{}' : ingredients is not valid".format(name))
		self.ingredients = ingredients			#(list):	list of all ingredients each represented by a string,
		
		self.description = description			#(str):		description of the recipe,
		
		if (not recipe_type in ["starter", "lunch", "dessert"]):
			print_error("Error creating Recipe '{}' : recipe type can only be starter, lunch or dessert".format(name))
		self.recipe_type = recipe_type			#(str):		can be "starter", "lunch" or "dessert"

	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt =	"\tRecipe name: {}\n"\
				"\tCooking lvl: {}\n"\
				"\tcooking time: {} minutes\n"\
				"\tIngredients: {}\n"\
				"\tRecipe type: {}\n"\
				"\tDescription: '{}'".format\
								   (self.name,
									self.cooking_lvl,
									self.cooking_time, 
									self.ingredients,
									self.recipe_type,
									self.description)
				
		"""Your code here"""
		return txt