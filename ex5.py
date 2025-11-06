import wave
from scipy.io import wavfile
import numpy as np
from FFT import *
import sounddevice as sd
from filtros import peaking_eq, trata_audio, filtro_passa_baixa
import matplotlib.pyplot as plt
import control as ctrl


arquivo = wave.open("projeto8/file_example_WAV_1MG.wav")
rate, audio = wavfile.read("projeto8/file_example_WAV_1MG.wav")
audio_mono=[]
for i in audio:
    audio_mono.append(float(i[0]))
T=  float(len(audio)/rate)
N = len(audio)
print(rate,len(audio), len(audio)/rate)
t = np.linspace(0, T,N, endpoint=False)
f = 16000
port=1*np.sin(2*np.pi*f*t)
# print(len(audio_mono),len(port), rate)
print(rate)
transmitida = audio_mono*port
trasnmitida1 = transmitida*port
gain_db=-10
Q=1
f0=500
b, a = filtro_passa_baixa(f0, Q, rate)
# G1= ctrl.TransferFunction(b,a, dt=(1/rate))
result= trata_audio(trasnmitida1, b, a)
# result= trasnmitida1
freqs, magnitude, magnitude_db = compute_fft(audio_mono, rate, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t, audio_mono, rate , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')

freqs, magnitude, magnitude_db = compute_fft(port, rate, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t, port, rate , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')

freqs, magnitude, magnitude_db = compute_fft(transmitida, rate, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t, transmitida, rate , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')  

freqs, magnitude, magnitude_db = compute_fft(result, rate, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t, result, rate , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')  
plt.show()
sd.play(audio_mono,rate)
sd.wait()
sd.play(transmitida,rate)
sd.wait()
sd.play(result,rate)
sd.wait()