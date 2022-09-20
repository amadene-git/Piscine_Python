import sys

if len(sys.argv) == 1:
	quit(0)

morse_dict = {
'A':	".-",
'B':	"-...",
'C':	"-.-.",
'D':	"-..",
'E':	".",
'F':	"..-.",
'G':	"--.",
'H':	"....",
'I':	"..",
'J':	".---",
'K':	"-.-",
'L':	".-..",
'M':	"--",
'N':	"-.",
'O':	"---",
'P':	".--.",
'Q':	"--.-",
'R':	".-.",
'S':	"...",
'T':	"-",
'U':	"..-",
'V':	"...-",
'W':	".--",
'X':	"-..-",
'Y':	"-.--",
'Z':	"--..",
'0':	"-----",
'1':	".----",
'2':	"..---",
'3':	"...--",
'4':	"....-",
'5':	".....",
'6':	"-....",
'7':	"--...",
'8':	"---..",
'9':	"----.",
' ':	"/"
}

str = str()
for i in range(1, len(sys.argv)):
	
	for letter in sys.argv[i].upper():
		try:
			str += morse_dict[letter] + ' '
		except KeyError:
			print("ERROR", file=sys.stderr)
			quit(1)
	
	if i < len(sys.argv) - 1:
		str += '/ '


print(str[:-1])



