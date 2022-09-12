import sys
import string

def text_analyzer(text):
    
    lower = 0
    upper = 0
    punct = 0
    space = 0


    i = 0
    for a in  text:
        if a.islower():
            lower += 1
        elif a.isupper():
            upper += 1
        elif a in string.punctuation:
            punct += 1
        elif a.isspace():
            space += 1


    print("The text contains {} character(s):".format(len(text)))
    print("- {} upper letter(s)".format(upper))
    print("- {} lower letter(s)".format(lower))
    print("- {} punctuation mark(s)".format(punct))
    print("- {} space(s)".format(space))
