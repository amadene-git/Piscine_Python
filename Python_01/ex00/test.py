from recipe import Recipe
from book import Book
from time import sleep

pudding = Recipe(	name="lol",
					cooking_time=0,
					cooking_lvl=1,
					ingredients=["tomatoes"],
					recipe_type="lunch",
					description= None)


cake = Recipe(	name="cake",
					cooking_time=120,
					cooking_lvl=1,
					ingredients=["chaocolat"],
					recipe_type="lunch",
					description="crounch")



print(str(pudding))


cookbook = Book("CookBook")

print(cookbook)
sleep(1)
print("\nadd\n")
cookbook.add_recipe(pudding)

print(cookbook)
print("\nget\n")

copy = cookbook.get_recipe_by_name("pudding")

sleep(1)

print("\nget recipes by keys\n")

cookbook.add_recipe(cake)

cookbook.get_recipes_by_types("lunch")


print(cookbook)
