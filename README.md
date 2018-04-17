# Billboard Chart Prediction
The Portfolio of INFO7390
## Introduction

## Getting Start

### Prerequisites
You should install Spotipy, billboard api , and Tensorflow

### Installation
1、spotipy api
```bash
pip install spotipy
```
You can see this api at [spotipy github](https://github.com/plamere/spotipy).

2、billboard api(Unofficial)
```bash
pip install billboard.py
```
you can see all documents at[Allen Guo](https://github.com/guoguo12/billboard-charts)

3、Tensorflow
```bash
pip install --ignore-installed --upgrade tensorflow-gpu 
```
you must install GPU version of TensorFlow,and all the documents are at[Tensorflow](https://www.tensorflow.org/?hl=zh-cn)

### Get Billboad Chart by using Billboard API
you should run getdata.py with the data1.csv to get 100000 songs rank in billboard chart,if you run getdata.py and get about 100000 songs data which were saved in data.csv.

### Use the Spotify API to get Audio Feature
run regetdata.py to get the Artist id, Track id and audio feature of each track, then you will get all data which we have saved in new_data.csv. 
 
