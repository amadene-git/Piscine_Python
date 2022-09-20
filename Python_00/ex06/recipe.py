import sys

# sys.tracebacklimit = -1

cookbook = {"sandwich": {	
							"ingredients":	["ham", "bread", "cheese", "tomatoes"],
                            "meal":	"lunch",
                            "prep_time":	10
						},
			"cake" :	{	
							"ingredients":	["flour", "sugar", "eggs"], 
                        	"meal":	"dessert",
                            "prep_time":	60
						},
			"salad":	{
							"ingredients":	["avocado", "arugula", "tomatoes", "spinach"], 
                            "meal":	"lunch",
                            "prep_time":	15
						}
			}


def	print_all_recipe_names():
	print("\nRecipe Names:")
	for i in cookbook.keys():
		print("\t{}".format(i))
	print()

def	print_recipe_by_name(name):
	if not isinstance(name, str):
		raise AssertionError("print_recipe_by_name(): name not valid")
	if not name in cookbook.keys():
		print(">>> Sorry, '{}' recipe does not exist.\n".format(name))
		return
	print("\nRecipe for {}:".format(name))
	print("\tIngredients list: {}".format(cookbook[name]["ingredients"]))
	print("\tTo be eaten for {}.".format(cookbook[name]["meal"]))
	print("\tTakes {} minutes of cooking.\n".format(cookbook[name]["prep_time"]))

def	delete_recipe_by_name(name):
	if not isinstance(name, str):
		raise AssertionError("print_recipe_by_name(): name not valid")
	if not name in cookbook.keys():
		print(">>> Sorry, '{}' recipe does not exist.".format(name))
		return
	print("\nRecipe for {} has been removed\n".format(name))
	cookbook.pop(name)

def add_recipe_by_stdin():
	
	recipe = {}
	print(">>> Enter a name:")
	while 1:
		name = input(">> ")
		if len(name) == 0:
			print(">>> Please enter a name:")
		elif not name.isalpha():
			print(">>> '{}': invalid name.".format(name))
			print(">>> Please enter a name:")
		elif name in cookbook.keys():
			print(">>> Sorry, the {} recipe already exists".format(name))
		else:
			recipe[name] = {}
			break

	ingredients = []
	print(">>> Enter ingredients:")
	while 1:
		line = input(">> ")
		if len(line) == 0 and len(ingredients) > 0:
			recipe[name]["ingredients"] = ingredients
			break
		elif len(line) == 0 and len(ingredients) == 0:
			print(">>> Please enter at least one ingredients:")
		elif line in ingredients:
			print(">>> The {} is already in the recipe.".format(line))
		elif not line.isalpha():
			print(">>> '{}': invalid ingredient.".format(line))
			print(">>> Please enter ingredients:")
		else:
			ingredients.append(line)

	print(">>> Enter a meal type:")
	while 1:
		line = input(">> ")
		if len(line) == 0:
			print(">>> Please enter a meal type:")
		elif not line.isalpha():
			print(">>> {} invalid meal type.".format(line))
			print(">>> Please enter a meal type:")
		else:
			recipe[name]["meal"] = line
			break

	print(">>> Enter a preparation time:")
	while 1:
		line = input(">> ")
		try:
			if len(line) == 0:
				print(">>> Please enter a preparation time:")
			elif int(line, base=10) <= 0:
				print(">>> The preparation time must be non-negative integer")
			else:
				recipe[name]["prep_time"] = int(line, base=10)
				break
		except ValueError:
			print(">>> The preparation time must be non-negative integer")

	cookbook.update(recipe)


print("Welcome to the Python Cookbook !")

while 1:
	print("List of available option:\n\
	1: Add a recipe\n\
	2: Delete a recipe\n\
	3: Print a recipe\n\
	4: Print the cookbook\n\
	5: Quit\n")

	try:
		line = input(">>> Please select an option:\n>> ")
	except (EOFError, KeyboardInterrupt):
		line = '5'
	
	if not line.isdigit() or int(line) < 1 or int(line) > 5:
		line = '0'
	
	if line == '1':
		add_recipe_by_stdin()
	elif line == '2':
		print("\n>>> Please enter a recipe to delete:")
		line = input(">> ")
		delete_recipe_by_name(line)
	elif line == '3':
		print("\n>>> Please enter a recipe name to print:")
		line = input(">> ")
		print_recipe_by_name(line)
	elif line == '4':
		print_all_recipe_names()
	elif line == '5':
		print("\nCookbook closed. Goodbye !")
		break
	elif line == '0':
		print(">>> Sorry, this option does not exist.\n")
		continue
