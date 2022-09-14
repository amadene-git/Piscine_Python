# Put this at the top of your kata01.py file
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

katakeys = list(kata.keys())

for i in katakeys:
    if not isinstance(i, str) or not isinstance(kata[i], str):
        raise AssertionError("Not a string")

for i in katakeys:
    print("{0} was created by {1}".format(i, kata[i]))