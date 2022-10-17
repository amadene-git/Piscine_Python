import random

# function prototype
def generator(text, sep=" ", option=None):
	'''Splits the text according to sep value and yield the substrings.
	option precise if a action is performed to the substrings before it is yielded.
	'''
	
	if (not option in ["shuffle", "unique", "ordered"] and not option is None)\
		or not isinstance(text, str) or not isinstance(sep, str)\
		or len(sep) == 0:
		yield "ERROR"
		return

	mylist = text.split(sep)

	if option == "shuffle":
		for i in range(len(mylist)):
			randomWord = random.choice(mylist)
			yield randomWord
			mylist.remove(randomWord)
	elif option == "unique":
		newlist = []
		for i in mylist:
			if i in newlist:
					continue
			else:
				newlist.append(i)
				yield i		
	elif option == "ordered":
		mylist.sort()
		for i in mylist:
			yield i
	else:
		for i in mylist:
			yield i


# if __name__ == '__main__':
# 	text = "Le Lorem Ipsum est simplement du faux texte."
# 	for word in generator(text):
# 		print(word)
# 	# Le
# 	# Lorem
# 	# Ipsum
# 	# est
# 	# simplement
# 	# du
# 	# faux
# 	# texte.

# 	print()
# 	for word in generator(text, sep=" ", option="shuffle"):
# 		print(word)

# 	print()
# 	for word in generator(text, sep=" ", option="ordered"):
# 		print(word)
# 	# Ipsum
# 	# Le
# 	# Lorem
# 	# du
# 	# est
# 	# faux
# 	# simplement
# 	# texte.

# 	print()
# 	text = "Lorem Ipsum Lorem Ipsum"
# 	for word in generator(text, sep=" ", option="unique"):
# 		print(word)
# 	# Lorem
# 	# Ipsum

