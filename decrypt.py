from cryptography.fernet import Fernet
import pandas as pd
# read the file
def get_key():
    key= open("key.txt","rb").read()
    return key
# loop the pass.csv file
def decrypt():
		df = pd.read_csv('pass.csv')
		key = get_key()
		a = Fernet(key)
		print(len(df), 'credenditals found')
		row_num = input('enter the row number you want to decrypt: default(all rows)')
		row_num+=1
		if row_num == '':
			for i in range(len(df)):
				encrypted_msg = df.iloc[i]['password']
				decrypted_msg = a.decrypt(encrypted_msg.encode("utf-8"))
				print(df.loc[i,'username'],decrypted_msg.decode("utf-8"))
			return
		encrypted_msg = df.loc[int(row_num),'password']
		decrypted_msg = a.decrypt(encrypted_msg.encode("utf-8"))
		# print username and decrypted message
		print(df.loc[int(row_num),'username'], decrypted_msg.decode("utf-8"))
decrypt()