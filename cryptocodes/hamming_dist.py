
from base_convs import ascii_to_bin_str

def ham_dist(a, b):
	
	bin_a = ascii_to_bin_str(a)
	bin_b = ascii_to_bin_str(b)

	count = 0
	for i in range(len(bin_a)):
		if int(bin_a[i]) ^ int(bin_b[i]) == 1:
			count += 1

	print(count) 

def main():
	a = input()
	b = input()

	ham_dist(a, b)

if __name__ == "__main__":
	main()
