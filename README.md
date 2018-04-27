# Billboard Chart Prediction
The Portfolio of INFO7390
## Introduction
The Billboard charts tabulate the relative weekly popularity of singles or albums in the United States and
elsewhere. It is significant to music producers, singers as well as the users.
First, our project will gather the raw datasets which includes the weekly Billboard 100 hot chart ranges from
1998-2018. Second, applying linear regression model to predict the peak rank of each track by using track’s
audio features and artist social influence. Third, applying logistic regression model to predict whether the song’s
peak rank will be higher than 30 or not. The accuracy of logistic regression model is 68%.Furthermore, the
convolution neural network model will be implemented by several steps. The CNN model includes two
convolution layers and two max-pooling layer, and the accuracy improves up to 72.2%. After the
hyperparameter adjustment and model optimization, the accuracy of predicting whether the song will rank
higher than 30 or not increases. Besides, the Long Short-Term Memory Network is applied to predict the time
span of the songs’ on top 30 chart. The accuracy is 68.8%.
## Getting Start

### Prerequisites
We use anaconda3.
You should install Spotipy, billboard api , and Tensorflow and download the dataset on(https://drive.google.com/file/d/1RXsMtwsQRs_kPpgHB2uxJzspAhTPcPx8/view?usp=sharing)

### Installation
1.spotipy api
```bash
pip install spotipy
```
You can see this api at [spotipy github](https://github.com/plamere/spotipy).

2.billboard api(Unofficial)
```bash
pip install billboard.py
```
you can see all documents at[Allen Guo](https://github.com/guoguo12/billboard-charts)

3.Tensorflow
```bash
pip install --ignore-installed --upgrade tensorflow-gpu 
```
you must install GPU version of TensorFlow,and all the documents are at[Tensorflow](https://www.tensorflow.org/?hl=zh-cn)

### Get Billboad Chart by using Billboard API
you should run getdata.py with the data1.csv to get 100000 songs rank in billboard chart,if you run getdata.py and get about 100000 songs data which were saved in data.csv.

### Use the Spotify API to get Audio Feature
1.run regetdata.py to get the Artist id, Track id and audio feature of each track, then you will get all data which we have saved in new_data.csv. 

2.run aa_append_artists.py to get each artist popularity and followers, and we save in the pop_follower.csv

3.run read.Json.py to get each track's audio analysis, and we save all data into Data_Json folder.

Use Mysql to combine all these data into one csv file which we saved as Full_data.csv

### License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/WPF9500/7390-Portfolio/blob/master/LICENSE) file for details

The text in the document by <Penffei Wang> is licensed under CC BY 3.0 https://creativecommons.org/licenses/by/3.0/us/
  
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
