								#MILLER-RABIN PRIMALITY TEST#

from math import pow
import sys, random
sys.path.append('../')
from numop import pseudo_rep, exp_mod

def mill_rab(n):

	max_iter = 25

	s, t = pseudo_rep(n)

	for i in range(max_iter):
		a = random.randint(1, n-1)

		for j in range(1, s):
			val = exp_mod(a, int(pow(2, j))*t, n)
			if val != 1 and val != n-1:
				return False
		
	return True

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage : python3 miller_rabin.py [in_file]")
		exit(1)

	file = open(sys.argv[1])
	n = int(file.read())
	if mill_rab(n):
		print("Prime")
	else:
		print("Composite")
