import requests
import pandas as pd
import numpy as np

def get_user_id(username):
	"""
	- When given mastodon @username@server, tries to look up the user_id through the mastodon API.
	- Although it does not appear to be clearly advertised, some instances seem to block this lookup.
	If successful returns the user_id. If unsuccessful *and* the specific failure is 
	accounted for, returns -1
	"""
	pieces=username.split('@', 2) #splits at first and second @
	try:
		res=requests.get('https://{}/api/v2/search?q={}'.format(pieces[2],pieces[1]))
		if ('error' in res.json()) or (len(res.json()['accounts'])==0):
			# if requests returns something but not what we want
			account_id=-1	
		else: account_id=res.json()['accounts'][0]['id']
	except Exception: #if the request is unsuccessful..
		account_id=-1	
	# print(pieces[1],pieces[2], account_id)
	return account_id


output_file='user_id_list.txt'
accounts=pd.read_csv('./resources/earthodons.csv')
usernames=[account['account'] for i,account in accounts.iterrows()]
account_ids=[]

for username in usernames:
	account_id=get_user_id(username)
	account_ids.append(account_id)
	print(username, account_id)

result=pd.DataFrame(np.column_stack(([username.split('@')[-2] for username in usernames],
				[username.split('@')[-1] for username in usernames], account_ids)),
				columns=['username','server','user_id'])
result.to_csv(output_file,sep='\t', index=False)

