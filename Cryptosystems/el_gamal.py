import random 
from math import pow

def gcd(a, b):
	if a < b:
		return gcd(b , a)
	elif a%b == 0:
		return b;
	else:
		return gcd(b, a%b)

#Generating keys for both sender and receiver
def gen_key(q):

	key = random.randint(pow(10, 20), q)
	while gcd(q, key) != 1:
		key = random.randint(pow(10, 20), q)

	return key

#Modular Exponentiation
def power(a, b, c):
	x = 1
	y = a

	while b > 0:
		if b%2 == 0:
			x = (x*y) % c;
		y = (y * y) % c
		b = b >> 1

	return x % c

#Encryption Function
def encrypt(msg, q, h, g):

	en_msg = []

	k = gen_key(q)		#Key for sender(k)
	s = power(h, k, q)	#s = g^ak
	p = power(g, k, q)	#p = g^k
	
	for i in range(0, len(msg)):
		en_msg.append(msg[i])

	print("g^k used : ", p)
	print("g^ak used : ", s)
	for i in range(0, len(en_msg)):
		en_msg[i] = s * ord(en_msg[i])

	return en_msg, p

#Decryption Function
def decrypt(en_msg, p, key, q):

	dr_msg = []
	h = power(p, key, q)
	for i in range(0, len(en_msg)):
		dr_msg.append(chr(int(en_msg[i]/h)))

	return dr_msg

#Main Function
def main():

	msg = input("Enter the message to be encrypted : ")
	print("Original Message :", msg)

	q = random.randint(pow(10, 20), pow(10, 50))
	g = random.randint(2, q)

	key = gen_key(q)	#Key for reciever(a)
	h = power(g, key, q)	#h = g^a
	print("g used : ", g)
	print("g^a used : ", h)

	en_msg, p = encrypt(msg, q, h, g)
	print("Encrypted message :", en_msg)
	dr_msg = decrypt(en_msg, p, key, q)
	dmsg = ''.join(dr_msg)
	print("Decrypted Message :", dmsg);

if __name__ == '__main__':
	main()
