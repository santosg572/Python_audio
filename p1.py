import IPython.display as ipd
from glob import glob
import librosa
import librosa.display

audio_files = '2025_03_13_08_14_00.m4a'

ipd.Audio(audio_files, autoplay=True)

y, sr = librosa.load(audio_files)
print(f'y: {y[:10]}')
print(f'shape y: {y.shape}')
print(f'sr: {sr}')



