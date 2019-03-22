					#Converting a message in base64 representation

from base_convs import *

def dec_to_b64(num):

	if num < 26:
		return str(chr(num + 65))
	elif num < 52:
		return str(chr(num + 97 - 26))
	elif num < 62:
		return str(chr(num + 48 - 52))
	elif num == 62:
		return '+'
	else:
		return '/'


def main():
	msg = input()
	
	bin_msg = hex_to_bin_str(msg)
	bin_msg = bin_msg[::-1]
	
	while len(bin_msg)%6 != 0:
		bin_msg += '0'
	
	bin_msg = bin_msg[::-1]
	b64_num = ''

	for i in range(0, len(bin_msg), 6):
		num = bin_msg[i: i+6]
		num = bin_to_dec(int(num))
		b64_num += dec_to_b64(num)

	print(b64_num)

if __name__ == "__main__":
	main()
