import sys

def append(str):
	return str


class Vector:
	def __init__(self, *args) -> None:
		if (len(args) < 1 or len(args) > 1):
			raise Exception("Vector.__init__() have {} argument, expected 1".format(len(args)))
		
		if isinstance(args[0], int) and args[0] > 0:# on va partir du principe que une size de 0 n'est pas possible
			print("size init called")
			i = 0.0
			self.value = []
			self.shape = (args[0], 1)
			while i < args[0]:
				self.value.append([i])
				i += 1
		
		elif isinstance(args[0], tuple) and len(args[0]) == 2 and args[0][0] <= args[0][1]:
			print("range init called")
			i = args[0][0]
			self.value = []
			self.shape = (args[0][1] - args[0][0], 1)
			while i < args[0][1]:
				self.value.append([float(i)])
				i += 1
		
		elif isinstance(args[0], list) and len(args[0]) == 1 and isinstance(args[0][0], list) and len(args[0][0]) > 0:			
			print("list init called")
			for i in args[0][0]:
				if not isinstance(i, float):
					raise Exception("Vector.__init__() {} is not a valid argument".format(args[0][0]))
			self.value = args[0]
			self.shape = (1, len(args[0][0]))
		
		elif isinstance(args[0], list) and len(args[0]) > 0 and isinstance(args[0][0], list) and len(args[0][0]) == 1:
			print("column init called")
			for i in args[0]:
				if not isinstance(i, list) and len(i) != 1 and not isinstance(i[0], float):
					raise Exception("Vector.__init__() {} is not a valid argument")
			self.value = args[0]
			self.shape = (len(args[0]), 1)
		
		else:
			raise Exception("Vector.__init__() {} is not a valid argument")


	def dot(self, *args):
		if len(args) != 1 or not isinstance(args[0], Vector):
			raise Exception("Vector.dot() requiered 1 Vector() argument")
		print("Vector.dot({})".format(args[0]))
		if self.shape != args[0].shape:
			raise Exception("Vector.dot() vectors have different shapes")
		
		ret = 0.
		if self.shape[0] == 1 and self.shape[1] > 0:
			for i in range(self.shape[1]):
				ret += self.value[0][i] * args[0].value[0][i]
		elif self.shape[1] == 1 and self.shape[0] > 0:
			for i in range(self.shape[0]):
				ret += self.value[i][0] * args[0].value[i][0]
		return ret

	def T(self):
		print("Vector.T()")
		ret = []
		if self.shape[0] == 1 and self.shape[1] > 0:
			for i in range(self.shape[1]):
				ret.append([self.value[0][i]])
			return Vector(ret)
		elif self.shape[1] == 1 and self.shape[0] > 0:
			for i in range(self.shape[0]):
				ret.append(self.value[i][0])
			return Vector([ret])

	def __add__(self, rhs):
		if not isinstance(rhs, Vector):
			if self.shape == (1, 1):
				try:
					ret = self.value[0][0] + rhs
				except TypeError:
					raise Exception("Vector.__add__() no overload viable for '{} + {}'".format(self.value, rhs))
				print("Vector.__add__(): {} + {}".format(self.value, rhs))
				return Vector([[ret]])
			else:
				raise Exception("Vector.__add__() no overload viable for '{} + {}'".format(self.value, rhs))
		
		print("Vector.__add__(): {} + {}".format(self.value, rhs.value))
		if self.shape != rhs.shape:
			raise Exception("Vector.__add__() vectors have different shapes")
		ret = []
		if self.shape[0] == 1 and self.shape[1] > 0:
			for i in range(self.shape[1]):
				ret.append(self.value[0][i] + rhs.value[0][i])
			return Vector([ret])
		elif self.shape[1] == 1 and self.shape[0] > 0:
			for i in range(self.shape[0]):
				ret.append([self.value[i][0] + rhs.value[i][0]])
			return Vector(ret)
		
	def __radd__(self, lhs):
		if not isinstance(lhs, Vector):
			if self.shape == (1, 1):
				try:
					ret = self.value[0][0] + lhs
				except TypeError:
					raise Exception("Vector.__radd__() no overload viable for '{} + {}'".format(lhs, self.value))
				print("Vector.__radd__(): {} + {}".format(lhs, self.value))
				return Vector([[ret]])
			else:
				raise Exception("Vector.__radd__() no overload viable for '{} + {}'".format(lhs, self.value))
		
		print("Vector.__radd__() {} + {}".format(lhs.value, self.value))
		if self.shape != lhs.shape:
			raise Exception("Vector.__radd__() vectors have different shapes")
		ret = []
		if self.shape[0] == 1 and self.shape[1] > 0:
			for i in range(self.shape[1]):
				ret.append(lhs.value[0][i] + self.value[0][i])
			return Vector([ret])
		elif self.shape[1] == 1 and self.shape[0] > 0:
			for i in range(self.shape[0]):
				ret.append([lhs.value[i][0] + self.value[i][0]])
			return Vector(ret)

	def __sub__(self, rhs):
		if not isinstance(rhs, Vector):
			if self.shape == (1, 1):
				try:
					ret = self.value[0][0] - rhs
				except TypeError:
					raise Exception("Vector.__sub__() no overload viable for '{} - {}'".format(self.value, rhs))
				print("Vector.__sub__(): {} - {}".format(self.value, rhs))
				return Vector([[ret]])
			else:
				raise Exception("Vector.__sub__() no overload viable for '{} - {}'".format(self.value, rhs))
		
		print("Vector.__sub__(): {} - {}".format(self.value, rhs.value))
		if self.shape != rhs.shape:
			raise Exception("Vector.__sub__() vectors have different shapes")
		ret = []
		if self.shape[0] == 1 and self.shape[1] > 0:
			for i in range(self.shape[1]):
				ret.append(self.value[0][i] - rhs.value[0][i])
			return Vector([ret])
		elif self.shape[1] == 1 and self.shape[0] > 0:
			for i in range(self.shape[0]):
				ret.append([self.value[i][0] - rhs.value[i][0]])
			return Vector(ret)

	def __rsub__(self, lhs):
		if not isinstance(lhs, Vector):
			if self.shape == (1, 1):
				try:
					ret = lhs - self.value[0][0]
				except TypeError:
					raise Exception("Vector.__rsub__() no overload viable for '{} + {}'".format(lhs, self.value))
				print("Vector.__rsub__(): {} - {}".format(lhs, self.value))
				return Vector([[ret]])
			else:
				raise Exception("Vector.__rsub__() no overload viable for '{} + {}'".format(lhs, self.value))

		print("Vector.__rsub__() {} - {}".format(lhs.value, self.value))
		if self.shape != lhs.shape:
			raise Exception("Vector.__rsub__() vectors have different shapes")
		ret = []
		if self.shape[0] == 1 and self.shape[1] > 0:
			for i in range(self.shape[1]):
				ret.append(lhs.value[0][i] - self.value[0][i])
			return Vector([ret])
		elif self.shape[1] == 1 and self.shape[0] > 0:
			for i in range(self.shape[0]):
				ret.append([lhs.value[i][0] - self.value[i][0]])
			return Vector(ret)

	def	__mul__(self, rhs):

		if not isinstance(rhs, Vector):
			raise Exception("Vector__mul__() not overload viable for '{} * {}'".format(self.value, rhs.value))
		else:
			if self.shape != (1, 1) and rhs.shape != (1, 1):
				raise Exception("Vector__mul__() not overload viable for '{} * {}'".format(self.value, rhs.value))

			print("Vector.__mul__(): {} * {}".format(self.value, rhs))
			
			ret = []
			if self.shape == (1, 1):
				lhs = rhs
				rhs = self.value[0][0]
			elif rhs.shape == (1, 1):
				lhs = self
				rhs = rhs.value[0][0]
			
			if lhs.shape[0] == 1 and lhs.shape[1] > 0:
				for i in range(lhs.shape[1]):
					ret.append(lhs.value[0][i] * rhs)
				return Vector([ret])
			elif lhs.shape[1] == 1 and lhs.shape[0] > 0:
				for i in range(lhs.shape[0]):
					ret.append([lhs.value[i][0] * rhs])
				return Vector(ret)



	def __rmul__(self, lhs):
		if isinstance(lhs, Vector) and not lhs.shape == (1, 1):
			raise Exception("Vector__rmul__() not overload viable for '{} * {}'".format(self.value, lhs.value))

		ret = []
		if isinstance(lhs, Vector) and lhs.shape == (1, 1):
			print("Vector__rmul__(): {} * {}".format(self.value, lhs.value))
			lhs = lhs.value[0][0]
		else:
			print("Vector__rmul__(): {} * {}".format(self.value, lhs))

		if self.shape[0] == 1 and self.shape[1] > 0:
			for i in range(self.shape[1]):
				ret.append(lhs * self.value[0][i])
			return Vector([ret])
		elif self.shape[1] == 1 and self.shape[0] > 0:
			for i in range(self.shape[0]):
				ret.append([lhs * self.value[i][0]])
			return Vector(ret)




	def __str__(self):
		txt = "value: {}\nshape: {}".format(self.value, self.shape)
		return txt
