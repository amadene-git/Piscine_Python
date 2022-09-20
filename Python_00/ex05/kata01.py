# Put this at the top of your kata01.py file
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

if not isinstance(kata, dict):
	raise AssertionError("kata is not a dictionary")

for key, value in kata.items():
	if not isinstance(key, str) or not isinstance(value, str):
		raise AssertionError("kata is not a dictionary of string")

for key, value in kata.items():
	print(key, " was created by ", value)