# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 17:06:24 2018

@author: WPF95
"""
from __future__ import print_function
import billboard
import pandas as pd  
import spotipy 
import sys
import spotipy.util as util
import os
from spotipy.oauth2 import SpotifyClientCredentials 
import time
import json
import pprint
from collections import OrderedDict
import csv
from dateutil import parser
import numpy as np
import json
import io
from os import listdir

#os.environ["SPOTIPY_CLIENT_ID"] = 'c3ba89bb0fb34f73acb5c29dae323e53'
#os.environ["SPOTIPY_CLIENT_SECRET"] = '0c5c982374024ad1883f18afe7d19075'
#os.environ["SPOTIPY_REDIRECT_URI"] = 'http://www.baidu.com'

os.environ["SPOTIPY_CLIENT_ID"] = '2db029a6b2c047819deabd13354b2068'
os.environ["SPOTIPY_CLIENT_SECRET"] = '215c52a45bf6495fab0440060ffb643d'
os.environ["SPOTIPY_REDIRECT_URI"] = 'http://www.baidu.com'

username ="geomcintire"
scope = 'user-library-read'
token = util.prompt_for_user_token(username, scope)
sp = spotipy.Spotify(auth=token) 

filepath='C:/Users/WPF95/Desktop/Final Project/data'

filename_list=listdir(filepath)
#df = pd.read_csv("billboard-track.csv")
#name = df['title'][0] + ".json"
#print(name)
#print(filename_list[0])
#print(name in filename_list)

df = pd.read_csv("Full_data.csv")
for i in range(0,len(df)):
    comname = str(df['id'][i]) + ".json"
    comname =  ''.join(comname)
    if(comname in filename_list):
        number ='is ' + str(i)
        print(number)
        continue
    else:
        track_id = df['track_id'][i]
        try:
            analysis = sp.audio_analysis(track_id)
        except:
            continue
        jsonname = 'data/'+comname
        try:
            with open(jsonname, 'w') as f:
                json.dump(analysis, f)
        except:
            print('fail')
            continue
#        try:
#            my_df = pd.DataFrame(analysis)
#            my_df.to_json(jsonname,index = False)
#        except:
#            continue
        print(i) 
    jsonname="" 
   

#title = df['title'][0]
#result = sp.search(title, limit=1)
#data = result['tracks']['items']
#artist_uri = data[0]['artists'][0]['uri']
#artist = sp.artist(artist_uri)
#follwers = artist['followers']['total']
#popularity = artist['popularity']
#track_id = data[0]['id']
#analysis = sp.audio_analysis(track_id)
#jsonname = "json/" + title +".json"
#with open(jsonname, 'w') as f:
#    json.dump(analysis, f)
    


