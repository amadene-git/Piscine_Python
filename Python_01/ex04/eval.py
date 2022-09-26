import sys

class Evaluator:
	@staticmethod
	def zip_evaluate(coefs, words):
		if not isinstance(words, list) or not isinstance(coefs, list) or len(words) != len(coefs):
			return -1
		ret = 0
		for i in words:
			if not isinstance(i, str):
				return -1
		for i in coefs:
			if not isinstance(i, float):
				return -1
		for i in tuple(zip(coefs, words)):
			ret += i[0] * len(i[1])
		return(ret)

	@staticmethod	
	def enumerate_evaluate(coefs, words):
		if not isinstance(words, list) or not isinstance(coefs, list) or len(words) != len(coefs):
			return -1
		ret = 0
		for i in words:
			if not isinstance(i, str):
				return -1
		for i in coefs:
			if not isinstance(i, float):
				return -1
		coefs_tuple = tuple(enumerate(coefs))
		words_tuple = tuple(enumerate(words))
		for i in range(len(words)):
			ret += coefs_tuple[i][1] * len(words_tuple[i][1])

		return(ret)



# words =	["Le", "Lorem", "Ipsum", "est", "simple"]
# coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
# print (Evaluator.zip_evaluate(coefs, words))
# print (Evaluator.enumerate_evaluate(coefs, words))

# words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
# coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
# print (Evaluator.zip_evaluate(coefs, words))
# print (Evaluator.enumerate_evaluate(coefs, words))
