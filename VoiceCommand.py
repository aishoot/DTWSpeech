# coding=utf8
# A simple voice command recognition demo using DTW (Dynamic Time Warping). 
# The program has not been tested
import os
import wave
import pyaudio
from dtw import dtw
import numpy as np


def compute_distance_vec(vec1, vec2):
    return np.linalg.norm(vec1 - vec2)


class record():
    def record(self, CHUNK=44100, FORMAT=pyaudio.paInt16, CHANNELS=2, RATE=44100, RECORD_SECONDS=200,
               WAVE_OUTPUT_FILENAME="record.wav"):
        # Get data stream
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        stream.stop_stream()
        stream.close()
        p.terminate()

        # Write to wav file
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(''.join(frames))
        wf.close()


class voice():
    def loaddata(self, filepath):
        try:
            f = wave.open(filepath, 'rb')
            params = f.getparams()
            self.nchannels, self.sampwidth, self.framerate, self.nframes = params[:4]
            str_data = f.readframes(self.nframes)
            self.wave_data = np.fromstring(str_data, dtype=np.short)
            self.wave_data.shape = -1, self.sampwidth
            self.wave_data = self.wave_data.T #Store of original arrays of songs
            f.close()
            self.name = os.path.basename(filepath)  #Record the file name
            return True
        except IOError:
            print("File Error")

    def fft(self, frames=40):
        self.fft_blocks = [] #Divide the audio into 40 blocks per second through Fourier transform to each block.
        blocks_size = self.framerate   // frames
        for i in range(0, len(self.wave_data[0]) - blocks_size, blocks_size):
            self.fft_blocks.append(np.abs(np.fft.fft(self.wave_data[0][i:i + blocks_size])))

    @staticmethod
    def play(filepath):
        chunk = 1024
        wf = wave.open(filepath, 'rb')
        p = pyaudio.PyAudio()
        # The method of playing music
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        while True:
            data = wf.readframes(chunk)
            if data == "": break
            stream.write(data)
        stream.close()
        p.terminate()


if __name__ == '__main__':
    r = record()
    r.record(RECORD_SECONDS=3, WAVE_OUTPUT_FILENAME='record.wav')

    v = voice()
    v.loaddata('record.wav')
    v.fft()

    file_list = os.listdir("./sounds/")
    res = []
    for i in file_list:
        if i.split('.')[1] == 'wav':
            temp = voice()
            temp.loaddata(i)
            temp.fft()
            res.append((dtw.dtw(v.fft_blocks, temp.fft_blocks, compute_distance_vec)[0],i))
    res.sort()
    print(res)

    if res[0][1].find('open_qq') != -1:
        #os.system('C:\program\Tencent\QQ\Bin\QQScLauncher.exe')
        print("Open qq")
    elif res[0][1].find('zhimakaimen') != -1:
        #os.system('chrome.exe')
        print("Open chrome")
    elif res[0][1].find('play_music') != -1:
        #voice.play('C:\data\music\\audio\\audio\\ (9).wav')
        print("Play music")
