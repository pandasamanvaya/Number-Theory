							#NAVIE APPROACH OF CHECKING PRIME#

from math import sqrt
import sys
def naive(n):
	for i in range(2, int(sqrt(n))+1):
		if(n%i == 0):
			return False
	return True

if __name__ == "__main__":
	n = int(sys.argv[1])
	if naive(n):
		print("Prime")
	else:
		print("Composite")