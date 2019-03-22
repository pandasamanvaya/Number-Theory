#This is library of modules contianing some common number theoretic algorithms

def max(a, b):
	if(a < b):
		return b
	else:
		return a

def large_mul(a, b, q):
	#Calculates a*b (mod q)
	
	prod = 0
	i = 1
	while(b > 0):
		num = ((a * (b % 10)) * i) % q 
		b = int(b/10)
		prod = prod + num
		i = i * 10

	return prod % q



def exp_mod(a, b, n):
	#Calculates a^b (mod n) [Modular Exponentiation]

	result = 1
	increment = a
	while b > 0:

		if b%2 == 1: #Checking last bit 
			result = (result * increment) % n

		increment = (increment * increment) % n
		b = b >> 1

	return result

def gcd(a, b):
	#Iterative form euclid's algo. for computing gcd of a,b

	if a < b:
		max = b
	else:
		max = a
	b = (a + b) - max
	a = max

	while a%b != 0:
		max = a
		a = b
		b = max%b

	return b

def pseudo_rep(n):
	#Representing n-1 = 2^s * t (where n is prime)

	s = 0
	t = n - 1

	while t % pow(2, s) == 0:
		t = t >> 1 #Division by 2
		s += 1
	return s, t
