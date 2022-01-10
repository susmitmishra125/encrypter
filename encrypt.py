from cryptography.fernet import Fernet
import pandas as pd
import os
from datetime import datetime


def generate_key():
	# generate key and save it to key.txt
	if os.path.exists('key.txt'):
		print('key.txt already exists press y to overwrite the current key')
		flag = input()
		if flag.lower() != 'y':
			return
	key = Fernet.generate_key()
	with open("key.txt", "wb") as key_file:
			key_file.write(key)

def get_key():
		if not os.path.exists('key.txt'):
			generate_key()
		key= open("key.txt","rb").read()
		return key


def encrypt():
	# takes a string and returns a string
	msg=input("Enter the message you want to ENCRYPT : ")
	text = msg.encode("utf-8")
	# read from key.txt
	key = get_key()
	a = Fernet(key)

	encrypted_msg= a.encrypt(text)
	print(encrypted_msg)
	flag =  input('should i append this key to the file? (y/n)')
	if flag == 'y':
		# check if pass.csv exists else create
		if not os.path.exists('pass.csv'):
			df = pd.DataFrame(columns=['date','time','domain','username','password'])
			df.to_csv('pass.csv', index=False)
		df = pd.read_csv('pass.csv')

		print('enter the domain name or website name')
		domain = input()
		# f = open("pass.txt", "a")
		print('enter the username')
		username = input()
		# append domain username and encrypted message to pass.csv
		now = datetime.now() # current date and time
		date = now.strftime("%d/%m/%Y")
		time = now.strftime("%H:%M:%S")
		df.loc[len(df)] = [date,time,domain,username,encrypted_msg.decode("utf-8")]
		df.to_csv('pass.csv', index=False)
		print('saved encrypted message to pass.csv')
if __name__ == '__main__':
	encrypt()
	# uncomment the following line to generate a key or overwrite the current key
	# generate_key()