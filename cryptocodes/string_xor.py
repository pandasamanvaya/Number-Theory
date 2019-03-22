
from base_convs import *

def xor_str(a, b):
	xor = ''
	
	for i in range(len(a)):
		xor += str(int(a[i]) ^ int(b[i]))

	return xor

def pad_zeros(a, l):

	a = a[::-1]
	while len(a) != l:
		a += '0'
	a = a[::-1]

	return a

def str_xor(a, b):

	if len(a) > len(b):
		b = pad_zeros(b, len(a))
	elif len(a) < len(b):
		a = pad_zeros(a, len(b))

	bin_a = hex_to_bin_str(a)
	print(bin_a)
	bin_b = hex_to_bin_str(b)
	print(bin_a, bin_b)
	xor = xor_str(bin_a, bin_b)
	return (bin_to_hex_str(xor))

