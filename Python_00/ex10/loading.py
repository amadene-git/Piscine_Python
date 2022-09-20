import sys
import time
from time import sleep

bar_len = 20

def	ft_progress(lst):
	t_zero = time.time()

	for i in lst:
		t_one = time.time()		
		filled_bar = int(round(i * bar_len / len(lst)))
		bar = '=' * filled_bar + '>' + ' ' * (bar_len - filled_bar)
		sys.stdout.write("ETA: {eta:.2f}s [{percent: >3}%][{bar}] {i: >6}/{total} | elapsed time {time:.2f}s{end}"\
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


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(0.01)
print()
print(ret)