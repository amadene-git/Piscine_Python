# Put this at the top of your kata03.py file
kata = "The right format"

if not isinstance(kata, str) or len(kata) > 42:
	raise AssertionError("kata is not valid")

print("{:->42s}".format(kata), end='')