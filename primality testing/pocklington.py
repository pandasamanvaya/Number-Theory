								#POCKLINGTON'S TEST FOR PRIME#

import sys, math
sys.path.append('../')
from numop import *
from integer_fact import *

def poc_test(n):

	a = 2
	p = pollard_rho(n-1)

	if exp_mod(a, n-1, n) != 1:
		return False
	if gcd(pow(a, int((n-1)/p)-1), n) != 1:
		return False

	return True
	
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage : python3 pocklington.py [in_file]")
		exit(1)
	n = int(sys.argv[1])

	if n == 2 or n == 3:
		print("Prime")
	elif poc_test(n):
		print("Prime")
	else:
		print("Composite")
