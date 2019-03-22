import sys
sys.path.append('./primality testing')
from numop import *
from naive import *
def f(x):
	return x**2 + 1

def pollard_rho(n):
	x = 2; y = 2
	d = 1; c = 2
	k = 0

	if n == 2 or 4:
		return 2
		
	while d == 1:
		count = 1
		while count <= c and d <= 1:
			x = (f(x) + k) % n
			while x == y:
				k += 1
				x = (f(x) + k) % n
			d = gcd(abs(x - y), n)
			count += 1
		c *= 2
		y = x

	if naive(d):
		return d
	else:
		return(pollard_rho(d))


if __name__ == "__main__":
	n = int(sys.argv[1])
	print(pollard_rho(n))