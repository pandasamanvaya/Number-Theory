
def dec_to_bin(a, n):

	num = ''
	while a > 0:
		rem = a%2
		num += str(rem)
		a = a >> 1

	while len(num) < n:
		num += '0'
	num = num[::-1]
	return num

def bin_to_dec(a):
	num = 0
	i = 0

	while a > 0:
		num += pow(2, i)*(a%10)
		i += 1
		a = int(a/10)
	return num 

def hex_to_dec(a):
	hex_rep = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
			 '8':8, '9':9, 'a':10, 'A':10, 'b':11, 'B':11, 'c':12, 'C':12,
			 'd':13, 'D':13, 'e':14, 'E':14, 'f':15, 'F':15}
	return hex_rep[a]

def dec_to_hex(a):
	dec_rep = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7',
			 8:'8', 9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}

	return dec_rep[a]

def hex_to_bin_str(a):
	bin_a = ''

	for i in range(len(a)):
		bin = hex_to_dec(a[i])
		bin_a += dec_to_bin(bin, 4)

	return bin_a

def bin_to_hex_str(a):
	hex_a = ''

	for i in range(0, len(a), 4):
		hex = bin_to_dec(int(a[i:i+4]))
		hex_a += dec_to_hex(hex)

	return hex_a

def hex_to_ascii(a):
	ascii_a = ''

	for i in range(0, len(a), 2):
		hex = a[i:i+2]
		num = 16*hex_to_dec(hex[0]) + hex_to_dec(hex[1])
		ascii_a += chr(num)

	return ascii_a

def dec_to_hex_str(a):

	num = int(a)
	hex_num = ''

	while num > 0:
		rem = num % 16
		hex_num += dec_to_hex(rem) 
		num = num >> 4

	return hex_num[::-1]

def ascii_to_bin(a):

	num = ord(a)
	return dec_to_bin(num, 8)

def ascii_to_bin_str(a):

	bin = ''
	for i in a:
		bin += ascii_to_bin(i)

	return bin
	
def bin_to_ascii(a):
	ascii = ''

	for i in range(0, len(a), 8):
		bin = a[i: i+8]
		bin = bin_to_dec(int(bin))
		ascii += chr(bin)

	return ascii

def dec_to_base64(num):

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

def base64_to_bin(a):
	if a >= 'A' and a <= 'Z':
		str = dec_to_bin(ord(a) - ord('A'), 6)
	elif a >= 'a' and a <= 'z':
		str = dec_to_bin(26 + ord(a) - ord('a'), 6)
	elif a >= '0' and a <= '9':
		str = dec_to_bin(52 + ord(a) - ord('0'), 6)
	elif a == '+':
		str = dec_to_bin(62, 6)
	elif a == '/':
		str = dec_to_bin(63, 6)

	return str

def base64_to_bin_str(a):
	bin_str = ''

	for i in a:
		bin_str += base64_to_bin(i)
		#print(bin_str)

	return bin_str

def bin_to_base64(a):
	base64_str = ''

	for i in range(0, len(a), 6):
		bin = a[i: i+6]
		num = bin_to_dec(int(bin))
		base64_str += dec_to_base64(num)

	return base64_str

def base64_to_ascii(a):

	a = list(a)
	count = 0
	while a[-1] == '=':
		count += 1
		a.pop()

	a = ''.join(a)

	bin_str = base64_to_bin_str(a)
	
	while count != 0:
		bin_str += '0'
		bin_str += '0'
		count -= 1
		
	ascii = bin_to_ascii(bin_str)

	return ascii

def ascii_to_base64(a):
	
	bin_str = ascii_to_bin_str(a)
	count = 0

	while len(bin_str)%6 != 0:
		count += 1
		bin_str += '0' 
		bin_str += '0' 

	base64_str = bin_to_base64(bin_str)
	while count > 0:
		base64_str += '='
		count -= 1

	return base64_str