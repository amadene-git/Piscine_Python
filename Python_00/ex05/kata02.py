# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

if not isinstance(kata, tuple):
	raise AssertionError("kata is not a tuple")

if len(kata) < 5 or len(kata) > 5:
    raise AssertionError("Wrong number of kata items")

for i in range(len(kata)):
    if not isinstance(kata[i], int):
        raise AssertionError("{} is not a number".format(kata[i]))
    if kata[i] < 0:
        raise AssertionError("{} is negative".format(kata[i]))
    if i > 0 and kata[i] >= 100:
        raise AssertionError("{} contain more of 2 digits".format(kata[i]))
    elif kata[0] >= 10000:
        raise AssertionError("{} contain more of 4 digits".format(kata[i]))

print("{m:02}/{d:02}/{y:04} {h:02}:{min:02}".format(m=kata[1], d=kata[2], y=kata[0], h=kata[3], min=kata[4]))
# 09/25/2019 03:30