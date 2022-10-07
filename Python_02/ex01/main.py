def what_are_the_vars(*args, **kwargs):
	obj = ObjectC()
	for i in range(len(args)):
		setattr(obj, f'var_{i}', args[i])

	for key, value in kwargs.items():
		if (key in obj.__dict__.keys()):
			return None
		setattr(obj, key, value)
	return obj


class ObjectC(object):
	def __init__(self):
		return

def doom_printer(obj):
	if obj is None:
		print("ERROR")
		print("end")
		return
	for attr in dir(obj):
		if attr[0] != '_':
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print("end")

if __name__ == "__main__":
	obj = what_are_the_vars(7)
	print(type(obj))
	print("***********************")
	doom_printer(obj)
	obj = what_are_the_vars(None, [])
	print("***********************")
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	print("***********************")
	doom_printer(obj)
	obj = what_are_the_vars()
	print("***********************")
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	print("***********************")
	doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	print("***********************")
	doom_printer(obj)
	obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
	print("***********************")
	doom_printer(obj)
