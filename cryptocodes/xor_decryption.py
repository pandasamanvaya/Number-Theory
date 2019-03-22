import sys
from xor_cipher import xor_decrypt, find_msg

def main():
	
	xor_str = []
	length = 0
	file = open(sys.argv[1], 'r')

	while True:
		line = file.readline()
		if line == '':
			print(find_msg(xor_str, length))
			return

		if line[-1] == '\n':
			l = len(line) - 1
		else:
			l = len(line)

		temp = xor_decrypt(line[0:l])
		#print(l, line[:-1])
		#print(temp)
		xor_str.append(temp)
		length += 1


if __name__ == "__main__":
	main()
