import time
import random

def count_sort(a):
	_max = a[0]
	result = []
	for i in a:
		if i > _max:
			_max = i
	c = [-1]*(_max + 1)
	for i in range(len(a)):
		c[a[i]] += 1
	b = 0
	for i in range(len(c)):
		t = c[i]
		while t >= 0:
			a[b] = i
			b += 1
			t -= 1
	return a

def is_sorted(a):
	for i in range(1, len(a)):
		if a[i] < a[i - 1]:
			return False
	return True

arr = [random.randrange(0, 10**5) for x in range(10**5)]
start_time = time.time()
a =count_sort(arr)
print("--- %s seconds ---" % (time.time() - start_time))
print(is_sorted(a))
