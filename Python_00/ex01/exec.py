import sys

for i in sys.argv[::-1]:
    print(i[::-1].swapcase(), end='\n' if i == 1 else ' ')
    