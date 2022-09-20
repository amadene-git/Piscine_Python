# Put this at the top of your kata00.py file
kata = (1, 2, 5)

if not isinstance(kata, tuple):
	raise AssertionError("Not a tuple")

for i in (kata):
    if not isinstance(i, int):
        raise AssertionError("Not an integer")

print("The {} numbers are:".format(len(kata)), end='')

for i in range(len(kata)):
    print(" {},".format(kata[i]), end='')
    if i < len(kata) - 1:
        print(",", end='')

print()