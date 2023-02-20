#opens earthsci.csv, adds column for url of mastodon profiles, saves to earthodons.csv

import pandas as pd
data=pd.read_csv('earthsci.csv')
mast_url=[]
for thing in data['account']:
     pieces=thing.split('@', 2) #because someone had to go and add another @...
     #print(pieces[2],pieces[1])
     mast_url.append('https://{}/@{}'.format(pieces[2],pieces[1]))
data['link']=mast_url
data.to_csv('earthodons.csv', index=False)

