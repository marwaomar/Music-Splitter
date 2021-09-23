

import numpy as np
import librosa
import sounddevice as sd
from gui4 import Ui_MainWindow
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from sklearn.decomposition import FastICA, PCA
import matplotlib.pyplot as plt

from scipy import signal
class MainWindow(QMainWindow, Ui_MainWindow):

  def __init__(self, *args, **kwargs):
    super(MainWindow, self).__init__(*args, **kwargs)
    self.setupUi(self)
    self.song = None
    self.sr = None
    self.songname = None
    self.actionOpen_Song.triggered.connect(self.open_song)
    self.split.clicked.connect(self.spliter)
    self.original.clicked.connect(self.play_org)
    self.music.clicked.connect(self.play_music)
    self.vocal.clicked.connect(self.play_vocal)
    self.show() 

  def open_song(self):
    path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "All files (*.*)")
    filee = path.split('/')[-1]
    if  filee.endswith(".wav") :
      self.song,self.sr= librosa.load(path, duration=60)
      self.songname=filee[:-4]


  def spliter(self):
 
        
    S_full, phase = librosa.magphase(librosa.stft(self.song))
    S_filter = librosa.decompose.nn_filter(S_full,
                                          aggregate=np.median,
                                          metric='cosine',
                                          width=int(librosa.time_to_frames(5, sr=self.sr)))
    S_filter = np.minimum(S_full, S_filter)

    margin_i, margin_v =30, 1
    power = 2
    mask_i = librosa.util.softmask(S_filter,
                                  margin_i * (S_full - S_filter),
                                  power=power)

    mask_v = librosa.util.softmask(S_full - S_filter,
                                  margin_v * S_filter,
                                  power=power)

    S_foreground = mask_v * S_full
    S_background = mask_i * S_full

    phase1 = np.exp(1.j * np.random.uniform(0., 2*np.pi, size=phase.shape))

  
    audio1=librosa.istft(S_background* phase1)
    audio2=librosa.istft(S_foreground* phase1)
    plt.figure(figsize=(12, 8))
    plt.subplot(3, 1, 1)
    plt.plot(audio1)
    plt.title('Music')

    plt.subplot(3, 1, 2)
    plt.plot(audio2)
    plt.title('Vocals')
   
    plt.subplot(3, 1, 3)
    plt.plot(self.song)
    plt.title('Original Song')
    plt.show()
    librosa.output.write_wav(f"""{self.songname}_music.wav""", audio1, self.sr)
    librosa.output.write_wav(f"""{self.songname}_vocals.wav""", audio2, self.sr)

  def play_org(self):
    sd.play(self.song,self.sr)

  def play_music(self):
    song,sr=librosa.load(f"""{self.songname}_music.wav""")
    sd.play(song,sr)

  
  def play_vocal(self):
    song,sr=librosa.load(f"""{self.songname}_vocals.wav""")
    sd.play(song,sr)

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Failamp")
    app.setStyle("Fusion")
    window = MainWindow()
    app.exec_()

