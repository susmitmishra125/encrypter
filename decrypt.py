from cryptography.fernet import Fernet
# read the file
f = open("key.txt", "r")
lines = f.readlines()
f.close()
def get_key():
    key= open("pass.txt","rb").read()
    return key
for sent in lines:
	x=sent.split(' ')
	domain = x[0]
	username = x[1]
	# read the key from the file
	key= get_key()
	a = Fernet(key)
	password = a.decrypt(x[2].encode('utf-8'))
	print(domain,username,password.decode('utf-8'))