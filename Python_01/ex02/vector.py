import sys

sys.tracebacklimit = -1

def append(str):
	return str


class Vector:
	def __init__(self, *args) -> None:
		if (len(args) < 1 or len(args) > 1):
			raise Exception("Vector.__init__() have {} argument, expected 1".format(len(args)))
		
		if isinstance(args[0], int) and args[0] > 0:# on va partir du principe que une size de 0 n'est pas possible
			# print("size init called")
			i = 0.0
			self.values = []
			self.shape = (args[0], 1)
			while i < args[0]:
				self.values.append([i])
				i += 1
		
		elif isinstance(args[0], tuple) and len(args[0]) == 2 and args[0][0] <= args[0][1]:
			# print("range init called")
			i = args[0][0]
			self.values = []
			self.shape = (args[0][1] - args[0][0], 1)
			while i < args[0][1]:
				self.values.append([float(i)])
				i += 1
		
		elif isinstance(args[0], list) and len(args[0]) == 1 and isinstance(args[0][0], list) and len(args[0][0]) > 0:			
			# print("list init called")
			for i in args[0][0]:
				if not isinstance(i, float):
					raise Exception("Vector.__init__() {} is not a valid argument".format(args[0][0]))
			self.values = args[0]
			self.shape = (1, len(args[0][0]))
		
		elif isinstance(args[0], list) and len(args[0]) > 0 and isinstance(args[0][0], list) and len(args[0][0]) == 1:
			# print("column init called")
			for i in args[0]:
				if not isinstance(i, list) and len(i) != 1 and not isinstance(i[0], float):
					raise Exception("Vector.__init__() {} is not a valid argument")
			self.values = args[0]
			self.shape = (len(args[0]), 1)
		
		else:
			raise Exception(f"Vector.__init__() {args[0]} is not a valid argument")

	def __str__(self):
		return "Vector({})".format(self.values)

	def __repr__(self):
		return "Vector({})".format(self.values)

	def dot(self, *args):
		if len(args) != 1 or not isinstance(args[0], Vector):
			raise Exception("Vector.dot() requiered 1 Vector() argument")
		# print("Vector.dot({})".format(args[0]))
		if self.shape != args[0].shape:
			raise Exception("Vector.dot() vectors have different shapes")
		
		ret = 0.
		if self.shape[0] == 1 and self.shape[1] > 0:
			for i in range(self.shape[1]):
				ret += self.values[0][i] * args[0].values[0][i]
		elif self.shape[1] == 1 and self.shape[0] > 0:
			for i in range(self.shape[0]):
				ret += self.values[i][0] * args[0].values[i][0]
		return ret

	def T(self):
		# print("Vector.T()")
		ret = []
		if self.shape[0] == 1 and self.shape[1] > 0:
			for i in range(self.shape[1]):
				ret.append([self.values[0][i]])
			return Vector(ret)
		elif self.shape[1] == 1 and self.shape[0] > 0:
			for i in range(self.shape[0]):
				ret.append(self.values[i][0])
			return Vector([ret])

	def __add__(self, rhs):
		if not isinstance(rhs, Vector):
			if self.shape == (1, 1):
				try:
					ret = self.values[0][0] + rhs
				except TypeError:
					raise NotImplementedError("'{} + {}' Add a {} to a Vector is not defined here.".format(self, rhs, type(rhs)))
				# print("Vector.__add__(): {} + {}".format(self, rhs))
				return Vector([[ret]])
			else:
				raise NotImplementedError("'{} + {}' Add a {} to a non-scalar Vector is not defined here.".format(self, rhs, type(rhs)))
		
		if self.shape != rhs.shape:
			raise NotImplementedError("'{} + {}' Add Vectors with differents shapes is not defined here.".format(self, rhs))
		
		# print("Vector.__add__(): {} + {}".format(self, rhs))
		
		ret = []
		if self.shape[0] == 1 and self.shape[1] > 0:
			for i in range(self.shape[1]):
				ret.append(self.values[0][i] + rhs.values[0][i])
			return Vector([ret])
		elif self.shape[1] == 1 and self.shape[0] > 0:
			for i in range(self.shape[0]):
				ret.append([self.values[i][0] + rhs.values[i][0]])
			return Vector(ret)
		
	def __radd__(self, lhs):
		if not isinstance(lhs, Vector):
			if self.shape == (1, 1):
				try:
					ret = self.values[0][0] + lhs
				except TypeError:
					raise NotImplementedError("'{} + {}' Add a {} to a Vector is not defined here.".format(lhs, self, type(lhs)))
				# print("Vector.__radd__(): {} + {}".format(lhs, self))
				return Vector([[ret]])
			else:
				raise NotImplementedError("'{} + {}' Add a {} to a non-scalar Vector is not defined here.".format(lhs, self, type(lhs)))
		
		if self.shape != lhs.shape:
			raise NotImplementedError("'{} + {}' Add Vectors with differents shapes is not defined here.".format(lhs, self))
		
		# print("Vector.__radd__() {} + {}".format(lhs, self))
		
		ret = []
		if self.shape[0] == 1 and self.shape[1] > 0:
			for i in range(self.shape[1]):
				ret.append(lhs.values[0][i] + self.values[0][i])
			return Vector([ret])
		elif self.shape[1] == 1 and self.shape[0] > 0:
			for i in range(self.shape[0]):
				ret.append([lhs.values[i][0] + self.values[i][0]])
			return Vector(ret)

	def __sub__(self, rhs):
		if not isinstance(rhs, Vector):
			if self.shape == (1, 1):
				try:
					ret = self.values[0][0] - rhs
				except TypeError:
					raise NotImplementedError("'{} - {}' Subtract a Vector by a {} is not defined here.".format(self, rhs, type(rhs)))
				# print("Vector.__sub__(): {} - {}".format(self, rhs))
				return Vector([[ret]])
			else:
				raise NotImplementedError("'{} - {}' Subtract a non-scalar Vector by a {} is not defined here.".format(self, rhs, type(rhs)))
		
		if self.shape != rhs.shape:
			raise NotImplementedError("'{} - {}' Subtract Vectors with differents shapes is not defined here.".format(self, rhs))
		
		# print("Vector.__sub__(): {} - {}".format(self, rhs))
		
		ret = []
		if self.shape[0] == 1 and self.shape[1] > 0:
			for i in range(self.shape[1]):
				ret.append(self.values[0][i] - rhs.values[0][i])
			return Vector([ret])
		elif self.shape[1] == 1 and self.shape[0] > 0:
			for i in range(self.shape[0]):
				ret.append([self.values[i][0] - rhs.values[i][0]])
			return Vector(ret)

	def __rsub__(self, lhs):
		if not isinstance(lhs, Vector):
			if self.shape == (1, 1):
				try:
					ret = lhs - self.values[0][0]
				except TypeError:
					raise NotImplementedError("'{} - {}' Subtract a {} by a Vector is not defined here.".format(lhs, self, type(lhs)))
				# print("Vector.__rsub__(): {} - {}".format(lhs, self))
				return Vector([[ret]])
			else:
				raise NotImplementedError("'{} - {}' Subtract a {} by a non-scalar Vector is not defined here.".format(lhs, self, type(lhs)))

		if self.shape != lhs.shape:
			raise NotImplementedError("'{} - {}' Subtract Vectors with differents shapes is not defined here.".format(lhs, self))
		
		# print("Vector.__rsub__() {} - {}".format(lhs, self))
		
		ret = []
		if self.shape[0] == 1 and self.shape[1] > 0:
			for i in range(self.shape[1]):
				ret.append(lhs.values[0][i] - self.values[0][i])
			return Vector([ret])
		elif self.shape[1] == 1 and self.shape[0] > 0:
			for i in range(self.shape[0]):
				ret.append([lhs.values[i][0] - self.values[i][0]])
			return Vector(ret)

	def	__mul__(self, rhs):

		if not isinstance(rhs, Vector):
			try:
				self.values[0][0] * rhs
			except TypeError:
				raise NotImplementedError("'{} * {}' Multiply Vector by a {} is not defined here.".format(self, rhs, type(rhs)))
			
			# print("Vector.__mul__(): {} * {}".format(self, rhs))
			
			ret = []
			if self.shape[0] == 1:
				for i in self.values[0]:
					ret.append(i * rhs)
				return (Vector([ret]))
			else:
				for i in self.values:
					ret.append([i[0] * rhs])
				return (Vector(ret))
		else:
			if self.shape != (1, 1) and rhs.shape != (1, 1):
				raise NotImplementedError("'{} * {}' Multiply non-scalar Vectors by non-scalar Vectors is not defined here.".format(self, rhs))
			
			# print("Vector.__mul__(): {} * {}".format(self, rhs))
			
			ret = []
			if self.shape == (1, 1):
				lhs = rhs
				rhs = self.values[0][0]
			elif rhs.shape == (1, 1):
				lhs = self
				rhs = rhs.values[0][0]
			
			if lhs.shape[0] == 1 and lhs.shape[1] > 0:
				for i in range(lhs.shape[1]):
					ret.append(lhs.values[0][i] * rhs)
				return Vector([ret])
			elif lhs.shape[1] == 1 and lhs.shape[0] > 0:
				for i in range(lhs.shape[0]):
					ret.append([lhs.values[i][0] * rhs])
				return Vector(ret)



	def __rmul__(self, lhs):
		try:
			lhs * self.values[0][0]
		except TypeError:
				raise NotImplementedError("'{} * {}' Multiply {} by Vector is not defined here.".format(lhs, self, type(lhs)))
		
		# print("Vector.__rmul__(): {} * {}".format(lhs, self))

		ret = []
		if self.shape[0] == 1 and self.shape[1] > 0:
			for i in range(self.shape[1]):
				ret.append(lhs * self.values[0][i])
			return Vector([ret])
		elif self.shape[1] == 1 and self.shape[0] > 0:
			for i in range(self.shape[0]):
				ret.append([lhs * self.values[i][0]])
			return Vector(ret)


	def	__truediv__(self, rhs):

		if not isinstance(rhs, Vector):
			try:
				self.values[0][0] / rhs
			except TypeError:
				raise NotImplementedError("'{} / {}' Divide Vector by a {} is not defined here.".format(self, rhs, type(rhs)))
			
			# print("Vector.__truediv__(): {} / {}".format(self, rhs))
			
			ret = []
			if self.shape[0] == 1:
				for i in self.values[0]:
					ret.append(i / rhs)
				return (Vector([ret]))
			else:
				for i in self.values:
					ret.append([i[0] / rhs])
				return (Vector(ret))
		else:
			if rhs.shape != (1, 1):
				raise NotImplementedError("'{} / {}' Division of a scalar by a Vector is not defined here.".format(self, rhs))
			
			# print("Vector.__truediv__(): {} / {}".format(self, rhs))
			
			ret = []
			if self.shape == (1, 1):
				lhs = rhs
				rhs = self.values[0][0]
			elif rhs.shape == (1, 1):
				lhs = self
				rhs = rhs.values[0][0]
			
			if lhs.shape[0] == 1 and lhs.shape[1] > 0:
				for i in range(lhs.shape[1]):
					ret.append(lhs.values[0][i] / rhs)
				return Vector([ret])
			elif lhs.shape[1] == 1 and lhs.shape[0] > 0:
				for i in range(lhs.shape[0]):
					ret.append([lhs.values[i][0] / rhs])
				return Vector(ret)

	def __rtruediv__(self, lhs):
		if self.shape != (1, 1):
			raise NotImplementedError("'{} / {}' Division of a scalar by a Vector is not defined here.".format(lhs, self, type(lhs)))

		try:
			lhs / self.values[0][0]
		except TypeError:
				raise NotImplementedError("'{} / {}' Divide {} by Vector is not defined here.".format(lhs, self, type(lhs)))

		# print("Vector.__rtruediv__(): {} / {}".format(lhs, self))

		return Vector([[lhs / self.values[0][0]]])

