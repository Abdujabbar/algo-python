
def factorial(n):
	if n < 2:
		return 1
	return factorial(n - 1) * n

n = 10

facto = factorial(n)
c = 0
while facto % 10 == 0:
	c += 1
	facto /= 10
print(c)