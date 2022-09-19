from recipe import Recipe
from book import Book

pudding = Recipe(	name="pudding",
					cooking_time=10,
					cooking_lvl=5,
					ingredients=["tomates"],
					recipe_type=10,
					description="Miam Miam")


cake = Recipe(	name="cake",
					cooking_time=120,
					cooking_lvl=1,
					ingredients=["chaocolat"],
					recipe_type="lunch",
					description="crounch")



# print(str(pudding))


cookbook = Book("CookBook")

print(cookbook)
print("\nadd\n")
cookbook.add_recipe(pudding)

print(cookbook)
print("\nget\n")

copy = cookbook.get_recipe_by_name("pudding")

print("\nget recipes by keys\n")

cookbook.add_recipe(cake)

cookbook.get_recipes_by_types("lunch")


print(cookbook)
