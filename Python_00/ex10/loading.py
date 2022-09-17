from ast import Yield
import sys
# https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
# def progress(count, total, status=''):
#     bar_len = 60
#     filled_len = int(round(bar_len * count / float(total)))

#     percents = round(100.0 * count / float(total), 1)
#     bar = '=' * filled_len + '-' * (bar_len - filled_len)

#     sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
#     sys.stdout.flush()  # As suggested by Rom Ruben (see: http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console/27871113#comment50529068_27871113)

import time
from time import sleep
from tqdm import tqdm

bar_len = 20

def	ft_progress(lst):
	t_zero = time.time()
	for i in lst:
		if i <= 1:
			t_one = time.time()
		filled_bar = int(round(i * bar_len / len(lst)))
		bar = '=' * filled_bar + '>' + ' ' * (bar_len - filled_bar)
		sys.stdout.write("ETA: {eta:.2f}s [{percent}%][{bar}] {i}/{total} | elapsed time {time:.2f}s{end}"\
		.format\
		(\
			bar = bar,\
			i = i + 1,\
			total = len(lst),\
			time = time.time() - t_zero,\
			eta = (t_one - t_zero) * len(lst),\
			percent = int(round(i * 100 / len(lst))),\
			end = "\r" if i < len(lst) - 1 else "\n"\
		))
		sys.stdout.flush()
		yield i # ??? alors la aucune idee...


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(0.01)
print()
print(ret)