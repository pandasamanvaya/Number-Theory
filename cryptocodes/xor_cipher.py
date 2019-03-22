from base_convs import *

def pad_char(a, l):
	a = a[::-1]
	pad = a[-1]
	while len(a) != l:
		a += pad
	a = a[::-1]

	return a

def str_xor(a, b):
	if len(a) > len(b):
		b = pad_char(b, len(a))
	elif len(a) < len(b):
		a = pad_char(a, len(b))

	xor = ''
	for i in range(len(a)):
		xor += chr(ord(a[i]) ^ ord(b[i]))

	return xor

def xor_decrypt(a):
	
	decrypt_msg = ['' for i in range(128)]
	ascii = hex_to_ascii(a)
	for i in range(128):
		decrypt_msg[i] = str_xor(ascii, chr(i))

	return find_msg(decrypt_msg, 128)

def find_msg(decrypt_msg, l):

	max = 0
	pos = 0

	for i in range(l):
		sp_count = 0
		for j in decrypt_msg[i]:
			if j == ' ':
				sp_count += 1
		if sp_count >= max:
			max = sp_count
			pos = i

	#print("space = ", max)
	return decrypt_msg[pos]	
