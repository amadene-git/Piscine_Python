import sys
import string


if len(sys.argv) != 3 or not isinstance(sys.argv[1], str) or not sys.argv[2].isdigit():
	print("ERROR", file=sys.stderr)
	quit(1)


tab = sys.argv[1].maketrans("", "", string.punctuation)

lst = sys.argv[1].translate(tab).split()

listComprehension = [x for x in lst if len(x) > int(sys.argv[2])]


print(listComprehension)

