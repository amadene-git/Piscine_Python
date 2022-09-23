def triple(nb1, nb2):
	return nb1

tab1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tab2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
tab3 = [213, 456, 789]

def	ft_map(func, iter, *args):
	
	lst = []
	tpl = ()

	i = 0
	while i < len(iter):
		tpl += (iter[i],)
		for a in args:
			if (i < len(a)):
				tpl += (a[i],)
		if (len(tpl) < len(args) + 1):
			break
		lst.append(tpl)
		tpl = tuple()
		i += 1
	for a in lst:
		try:
			yield func(*a)
		except AttributeError:
			return None


print(tab1)
print(tab2)
print(list(ft_map(triple, tab1, tab2)))

