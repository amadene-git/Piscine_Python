import sys
from typing import List

def print_error(message: str):
	print(message, file=sys.stderr)
	# quit()


class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
	
		if (not isinstance(name, str) or len(name) == 0):
			print_error("Error creating Recipe: bad name")
		self.name = name						#(str)		name of the recipe,
	
		if (not isinstance(cooking_lvl, int) or cooking_lvl < 1 or cooking_lvl > 5):
			print_error("Error creating Recipe '{}': bad cooking_lvl".format(name))
		self.cooking_lvl = cooking_lvl			#(int):		range from 1 to 5,
	
		if (not isinstance(cooking_time, int) or cooking_time < 0):
			print_error("Error creating Recipe '{}' : bad cooking_time".format(name))
		self.cooking_time = cooking_time		#(int):		in minutes (no negative numbers),

		if (not isinstance(ingredients, list) or len(ingredients) == 0):
			print_error("Error creating Recipe '{}' : bad ingredients".format(name))
		for i in ingredients:
			if (not isinstance(i, str) or len(i) == 0):
				print_error("Error creating Recipe '{}' : ingredients is not valid".format(name))
		self.ingredients = ingredients			#(list):	list of all ingredients each represented by a string,

		if not isinstance(description, str):
			print_error("Error creating Recipe '{}' : bad description".format(name))
		self.description = description			#(str):		description of the recipe,

		if (not isinstance(recipe_type, str) or not recipe_type in ["starter", "lunch", "dessert"]):
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