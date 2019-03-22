import random 
from math import pow

def max(a, b):
	if a > b:
		return a
	else:
		return b

def gcd(a, b):
	if a < b:
		return gcd(b , a)
	elif a%b == 0:
		return b;
	else:
		return gcd(b, a%b)

def gen_key(q):

	key = random.randint(pow(10, 20), q)
	while gcd(q, key) != 1:
		key = random.randint(pow(10, 20), q)

	return key

def power(a, b, c):
	x = 1
	y = a

	while b > 0:
		if b%2 == 1:
			x = (x*y) % c;
		y = (y * y) % c
		b = int(b/2)

	return x % c

def encrypt(msg, k, q, h, g):

	s = power(h, k, q)

	print("g^ak used for message", msg, ":", s)
	en_msg = s * msg

	return en_msg

def decrypt(en_msg, p, key, q):

	h = power(p, key, q)
	dr_msg = int(en_msg/h)

	return dr_msg

def hom_compute(en_msg, q):

	for i in range(len(en_msg)):
		en_msg[i] = en_msg[i] * 10

	return en_msg

def main():

	msg = []
	en_msg = []
	dr_msg = []
	key_a = []
	key_b = []

	msg.append(2334)
	print("First Message :", msg[0])

	msg.append(1346)
	print("Second Message :", msg[1])

	q = random.randint(pow(10, 40), pow(10, 50))
	g = random.randint(2, q)

	print("g used : ", g)

	for i in range(len(msg)):
		key_a.append(gen_key(q))
		key_b.append(gen_key(q))

		h = power(g, key_a[i], q)
		p = power(g, key_b[i], q)
		print("g^a used for message", msg[i],":", h)
		print("g^k used for message", msg[i],":", p)

		en_msg.append(encrypt(msg[i], key_b[i], q, h, g))

	en_msg = hom_compute(en_msg, q)

	for i in range(len(en_msg)):
		p = power(g, key_b[i], q)
		dr_msg.append(decrypt(en_msg[i], p, key_a[i], q))

	print("Decrypted Message :", dr_msg);

if __name__ == '__main__':
	main()
