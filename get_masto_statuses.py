#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 14:08:07 2023

@author: crowan
"""

import pandas as pd
import numpy as np
from datetime import date, datetime, time
from mastodon import Mastodon

start_of_day=datetime.combine(date.today(), time(0,0,0,0))

user_ids=pd.read_csv('user_id_list.txt', sep='\t')
servers=np.unique(user_ids['server'])

def get_account_status_from_server(server, start_of_day):
    accounts=user_ids[user_ids['server']==server]
    mastodon = Mastodon(api_base_url = 'https://{}'.format(server))
    posts=[]
    for account in accounts:
        posts.append(mastodon.account(accounts.user_id, since_id=start_of_day)




for user_id in np.where(user_ids['server']==servers[0]):
    print(user_id)
    
mastodon = Mastodon(api_base_url = 'https://{}'.format(servers[0]))   


posts=[]
for i,account in accounts.iterrows():
    posts.append(mastodon.account_statuses(account.user_id, since_id=start_of_day))

