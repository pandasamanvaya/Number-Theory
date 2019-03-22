								#FERMAT'S CRITERION FOR PRIMES#
import random
import sys
import time
sys.path.append('../')
from numop import *

def main():

	if len(sys.argv) != 2:
		print("Usage : python3 fermat.py [in_file]")
		exit(1)

	file = open(sys.argv[1])
	n = int(file.read())

	start = time.time()

	if n == 2:
		print("Prime")
		return
	elif n < 2:
		print("Neither a Prime nor a Composite")	
		return

	a = random.randint(2, n-1)

	if gcd(a, n) != 1:
		print("Composite")
		
	if exp_mod(a, n-1, n) == 1:
		print("Prime")
	else:
		print("Composite")

	print("Time taken = ", time.time() - start, "s")

if __name__ == "__main__":
	main()
