from cryptography.fernet import Fernet
def genewrite_key():
    key= Fernet.generate_key()
    with open("pass.txt","wb") as key_file:
        key_file.write(key)
def get_key():
    key= open("pass.txt","rb").read()
    return key


def encrypt():
	# takes a string and returns a string
	msg=input("Enter the message you want to ENCRYPT : ")
	text = msg.encode()
	# read from key.txt
	key= get_key()
	a = Fernet(key)

	encrypted_msg= a.encrypt(text)
	print(encrypted_msg)
	flag =  input('should i append this key to the file? (y/n)')
	if flag == 'y':
		print('enter the domain name or website name')
		domain = input()
		f = open("key.txt", "a")
		print('enter the username')
		username = input()
		f.write(domain+' '+username+' '+encrypted_msg.decode("utf-8")+'\n')
		f.close()
		print('key added to file')
genewrite_key()
# encrypt()
