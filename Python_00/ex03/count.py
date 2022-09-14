import sys
import string
sys.tracebacklimit = -1



    


def text_analyzer(*argv):
    '''
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    '''    
    argc = len(argv)    
    lower = 0
    upper = 0
    punct = 0
    space = 0


    if argc == 0:
        text = input("What is the text to analyze?\n>> ")
    elif argc != 1:
        raise AssertionError("more than one argument is provided")
    else: 
        if not isinstance(argv[0], str):
             raise AssertionError("argument is not a string")
        text = argv[0]
    
    for a in text:
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


if __name__=='__main__':
    
    
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()