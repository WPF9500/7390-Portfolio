# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 17:24:43 2018

@author: WPF95
"""

import pandas as pd  
import spotipy 
import sys
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials 
import pprint
from collections import OrderedDict
import csv
import numpy as np
import os


os.environ["SPOTIPY_CLIENT_ID"] = '2db029a6b2c047819deabd13354b2068'
os.environ["SPOTIPY_CLIENT_SECRET"] = '215c52a45bf6495fab0440060ffb643d'
os.environ["SPOTIPY_REDIRECT_URI"] = 'http://www.baidu.com'


username ="geomcintire"
scope = 'user-library-read'
token = util.prompt_for_user_token(username, scope)
sp = spotipy.Spotify(auth=token)

aa = pd.read_csv("aa.csv")
#bb = aa.copy()
#col_name = bb.columns.tolist() 
#col_name.insert(col_name.index('popularity'),'artist_pop')
#col_name.insert(col_name.index('artist_id')+1,'follower')
#print(col_name)
#bb.reindex(columns=col_name)
#print(bb.head())


result = pd.read_csv("pop_follower.csv")
n = len(result)

links = []
i = 0
while i+n <=len(aa):
    tmp = []
    artist_id = aa['artist_id'][i+n]
    artist = sp.artist(artist_id)
    tmp.append(aa['title'][i+n])
    tmp.append(aa['artist'][i+n])
    tmp.append(artist['popularity'])
    tmp.append(artist['followers']['total'])
    links.append(tmp)
    if len(links)% 1 == 0:
        try:
            fd = open('pop_follower.csv','a',encoding='utf8',newline='')
            writer = csv.writer(fd, lineterminator = '\n')
            writer.writerows(links)
            fd.close()
            links =[]
            print("append successfully")
        except:
            my_df = pd.DataFrame(links)
            my_df.to_csv('pop_follower.csv',index = False, header =('title','artist','artist_popularity','followers'))
            links =[]
            print("create successfully")
    i = i + 1
    print(i+n)
#        print("create successfully")
    

        