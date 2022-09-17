# Put this at the top of your kata00.py file
kata = (12,21)

for i in (kata):
    if not isinstance(i, int):
        raise AssertionError("Not an integer")

print("The {} numbers are:".format(len(kata)), end='')

for i in range(len(kata)):
    print(" {},".format(kata[i]), end='')
    if i < len(kata) - 1:
        print(",", end='')

print()