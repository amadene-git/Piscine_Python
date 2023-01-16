from random import random
import sys
import time
from time import sleep
import random

bar_len = 20

def	ft_progress(lst):
	t_zero = time.time()

	for i in lst:
		t_one = time.time()		
		filled_bar = int(round(i * bar_len / len(lst)))
		bar = '=' * filled_bar + '>' + ' ' * (bar_len - filled_bar)
		sys.stdout.write("ETA: {eta:.3f}s [{percent: >3}%][{bar}] {i: >6}/{total} | elapsed time {time:.3f}s{end}"\
		.format\
		(\
			bar = bar,\
			i = i + 1,\
			total = len(lst),\
			time = time.time() - t_zero,\
			eta = ((t_one - t_zero) / (1 if i == 0 else i)) * (len(lst) - 1),\
			percent = int(round(i * 100 / len(lst))),\
			end = "\r" if i < len(lst) - 1 else "\n"\
		))
		yield i



if __name__ == "__main__":
	listy = range(1000)
	ret = 0
	for elem in ft_progress(listy):
		ret += (elem + 3) % 5
		sleep(random.randrange(1, 5) / 100)
	print()
	print(ret)
 