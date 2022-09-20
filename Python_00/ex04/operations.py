import sys

sys.tracebacklimit = -1

if len(sys.argv) > 3:
    raise AssertionError("too many arguments")
elif len(sys.argv) < 3:
    raise AssertionError("not enough arguments")

if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    raise AssertionError("only integers")


a = int(sys.argv[1])
b = int(sys.argv[2])

print("Sum:\t\t{}".format(a + b))
print("Difference:\t{}".format(a - b))
print("Product:\t{}".format(a * b))
if b != 0:
    print("Quotient:\t{}".format(a / b))
else:
    print("Quotient:\tERROR (division by zero)")

if b != 0:
    print("Remainder:\t{}".format(a % b))
else:
    print("Remainder:\tERROR (modulo by zero)")
