# DTW\* applied to isolate word speech recognition
[![Run on Repl.it](https://repl.it/badge/github/pchao6/DTWSpeech)](https://repl.it/github/pchao6/DTWSpeech)<br>
*\*DTW: Dynamic Time Warping*<br>
![](/speech2.jpg)

## File description
* Folders
  * unittest: python framework "unittest" learning. Run the file "run.py" with Python3.
  * sounds: sound files of "MFCC_DTW.ipynb".
  * train: train sample audios of "DTW_MFCC_KNN.ipynb".
  * test: test sample audio of "DTW_MFCC_KNN.ipynb".
* Files
  * wavToTag.txt: 245 French words.
  * dtw.py: implementation of DTW algorithm.
  * dtwTest.py: test of DTW algorithm.
  * VoiceCommand.py: a simple voice command recognition demo using DTW. 
  * DTW_simple_example.ipynb: DTW simple example.
  * MFCC_DTW.ipynb: compare the MFCCs of two sounds using DTW.
  * speech_recognition.ipynb: simple speech recognition system can be implemented using DTW + MFCC.
  * DTW_MFCC_KNN.ipynb: simple speech recognition using DTW, MFCC, and kNN (k-NearestNeighbor)

## Requirements
* [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/)
* [Anaconda3 (Python3.5+)](https://www.anaconda.com/download)
* [Librosa](http://librosa.github.io/librosa): `pip install librosa`

## References & Code source
* https://github.com/pierre-rouanet/dtw
* https://github.com/slaypni/fastdtw
* https://github.com/psbots/dtwSpeechRecognition
* https://www.cnblogs.com/rockyf/articles/4519352.html
* http://blog.csdn.net/raym0ndkwan/article/details/45614813
* http://blog.csdn.net/zouxy09/article/details/9140207
* http://www.cnblogs.com/chuxiuhong/p/6124459.html
* https://www.cnblogs.com/51kata/p/5887940.html
