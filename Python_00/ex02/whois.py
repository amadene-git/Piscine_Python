import sys

sys.tracebacklimit = -1

if len(sys.argv) == 1:
    quit()

if len(sys.argv) > 2:
    raise AssertionError("more than one argument are provided")
if len(sys.argv) == 2 and not sys.argv[1].isdigit():
    raise AssertionError("argument is not an integer")

if int(sys.argv[1]) == 0:
    print("I'm Zero.")
elif int(sys.argv[1]) % 2 == 1:
    print("I'm Odd.")
elif int(sys.argv[1]) % 2 == 0:
    print("I'm Even.")