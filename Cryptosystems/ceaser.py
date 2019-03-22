#Encrypting Function
def encrypt(b, message):

	print("Your original message :- ", message)
	print("Your encrypted message :- ", end = " "),

	for i in range(0, len(message)):
		if message[i] != ' ':
			print(chr(((ord(message[i]) - 97 + b) % 26) + 97), end = "")
		else:
			print(" ", end  = "")
	#
	print("")

#Decrypting Function
def decrypt(b, message):
	
	print("Your encrypted message :- ", message)
	print("Your original message :- ", end = " "),

	for i in range(0, len(message)):
		if message[i] != ' ':
			print(chr(((ord(message[i]) - 97 - b) % 26) + 97), end = "")

		else:
			print(" ", end = "")
	#
	print("")

#Main Function
def main():

	exit = "No"

	b = int(input("Enter b : "))
	print("Your ceaser function :- a + ", b, "(mod 26)")

	while exit != "Yes":
		print("1. Enter message to encrypt into ceaser cipher")
		print("2. Enter ceaser cipher message to decrypt it")
		ch = int(input("Enter you choice : "))

		message = input("Enter your message : ")

		if ch == 1:
			encrypt(b, message)
		elif ch == 2:
			decrypt(b, message)
		else:
			print("You have entered a wrong choice")

		exit = input("Do you want to exit ? [Yes | No] : ")
#
if __name__ == "__main__":
	main()
