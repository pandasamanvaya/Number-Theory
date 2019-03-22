import sys
from base_convs import *

def str_xor(a, b):
	return str(ord(a) ^ ord(b))

def main():

	file = open(sys.argv[1], 'r')
	msg = file.read()
	en_msg = ''

	for i in range(len(msg)-1):
		if i%3 == 0:
			temp = str_xor(msg[i], 'I')
		elif i%3 == 1:
			temp = str_xor(msg[i], 'C')
		else:
			temp = str_xor(msg[i], 'E')

		temp = dec_to_hex_str(temp)
		if len(temp) != 2:
			temp += '0'
			temp  = temp[::-1]

		en_msg += temp 

	print(en_msg)

if __name__ == "__main__":
	main()