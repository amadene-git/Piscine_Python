import sys
from datetime import datetime
from typing import List
from recipe import Recipe
from recipe import print_error

class Book:
	
	def __init__(self, name: str):
		self.name = name			#name (str): name of the book,
		self.creation_date: datetime = datetime.now() 	#creation_date (datetime): the creation date,
		self.last_update = self.creation_date	#last_update (datetime): the date of the last update,
		self.recipes_list = {} 	#recipes_list (dict): a dictionnary with 3 keys: "starter", "lunch", "dessert".
		self.recipes_list["lunch"] = 	[]
		self.recipes_list["dessert"] = 	[]
		self.recipes_list["starter"] = 	[]


	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name \texttt{name} and returns the instance"""
		if not isinstance(name, str):
			print_error(f"Error {self.name} get_recipe_by_name(): name given is not a string")
		

		for i in self.recipes_list.values():
			for j in i:
				if j.name == name:
					print(j)
					return j

		print("Sorry, there is no recipe named {} in the {} Book".format(name, self.name))

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		if (not isinstance(recipe_type, str) or not recipe_type in ["dessert", "lunch", "starter"]):
			print_error("Error get_recipes_by_types(): bad recipe_type")
		
		if (len(self.recipes_list[recipe_type]) == 0):
			print(f"No {recipe_type} recipe in {self.name}")
			return
		print(f'{recipe_type}: ')
		for i in self.recipes_list[recipe_type]:
			print(i, "\n")

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		if (not isinstance(recipe, Recipe)):
			print(f"Error add_recipe() bad recipe type given")
		
		self.recipes_list[recipe.recipe_type].append(recipe)
		self.last_update = datetime.now()


	def __str__(self):
		txt = f"Book name : {self.name}\n"
		txt += f"creation date: {self.creation_date}\n"
		txt += f"last update:   {self.last_update}\n"
		for key, value in self.recipes_list.items():
			txt += f"{key}:\n"
			for i in value:
				txt += str(i) + "\n\n"
		return txt