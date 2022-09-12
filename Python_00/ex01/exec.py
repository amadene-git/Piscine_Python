import sys

i = len(sys.argv) - 1
endl = ' '

while i > 0:
    if i == 1:
        endl = '\n'
    print(sys.argv[i][::-1].swapcase(), end=endl)
    
    i -= 1
