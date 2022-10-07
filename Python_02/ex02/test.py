a = 5
def double(funct: object):
	def print2(*args):
		
		funct(args)
		print(args)
	return (print2)

nb = 12

@double
def print_secret(nb):
	print('lalilali')
#



def print_log(funct):
	def funct2(*args, **kwargs):
		print(funct.__name__)
		print(args)
		print(kwargs)
		return funct(*args, **kwargs)
	return funct2

@print_log
def add_one(nb):
	nb += 1
	return nb

# add_one = print_log()






# print_secret = double(print_secret)


@print_log
def print_hello(name: str, punctuation: str):
	print(f"Hello {name} {punctuation}")

@print_log
def print_keyarg(keykey='lala', **kwargs):
	print(keykey)


#
print('END')
print(add_one(10), ' = 21')
print(add_one(20),' = 41')
# print(add_one("salut"))



print_hello("titouan", "^^'")
print_keyarg(lalali='lala')
print_keyarg(keykey='lulu')
