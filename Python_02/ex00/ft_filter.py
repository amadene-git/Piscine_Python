def func(nb):
	
	
	return 



def ft_filter(func, iter):
	if func is None:
		for i in iter:
			if i != False:
				yield i
	else:
		for i in iter:
			if func(i) != False:
				yield i



print(list(ft_filter(func, [1,2,0,3,0,-1,"salut"])))

# print (False == 123)