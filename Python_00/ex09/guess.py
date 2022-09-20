from curses.ascii import isdigit
import random

print("This is an interactive guessing game!\n\
You have to enter a number between 1 and 99 to find out the secret number.\n\
Type 'exit' to end the game.\n\
Good luck!\n")

secretnb = random.randint(1, 99)
# secretnb = 42
# secretnb = 43

i = 1
while i:
	print("What's your guess between 1 and 99?")
	try:
		line = input(">> ")
	except (EOFError, KeyboardInterrupt):
		line = "exit"

	if line == "exit":
		print("Goodbye!")
		break
	elif not line.isdigit():
		print("That's not a number.")
		i -= 1
	elif int(line) not in range(1, 99):
		print("Number is not between 1 and 99")
	elif int(line) > secretnb:
		print("Too high!")
	elif int(line) < secretnb:
		print("Too low!")
	elif int(line) == secretnb:
		if i == 1:
			if secretnb == 42:
				print("Une erreur commune que font les gens qui tentent de fabriquer quelque chose d'infaillible est de sous estimer l'ingéniosité des gens parfaitement cons.")
			print("Congratulations! You got it on your first try!")
		else:
			print("Congratulations, you've got it!\nYou won in {} attempts!".format(i))
		break
	i += 1