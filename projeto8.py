import wave
from scipy.io import wavfile
import numpy as np
from FFT import *
import sounddevice as sd
from filtros import *
import matplotlib.pyplot as plt
import control as ctrl
f0=1500
Q=5
# ---------Arquivo1---------
arquivo1 = wave.open("projeto8/file_example_WAV_1MG.wav")
rate1, audio1 = wavfile.read("projeto8/file_example_WAV_1MG.wav")
audio1_mono = paraMono(audio1)

# b1, a1 = filtro_passa_faixa(f0, Q, rate1)
b1, a1 = filtro_passa_baixa(5,rate1, 1500)
audiofiltrado_1= trata_audio(audio1_mono, b1, a1)

T1=  float(len(audio1)/rate1)
N1 = len(audio1)
t1 = np.linspace(0, T1,N1, endpoint=False)

# ---------------Arquivo2---------------
arquivo2 = wave.open("projeto8/relaxing-guitar-loop-v5-245859 (online-audio-converter.com).wav")
rate2, audio2 = wavfile.read("projeto8/relaxing-guitar-loop-v5-245859 (online-audio-converter.com).wav")
audio2_mono = audio2.mean(axis=1)
audio2_mono = audio2_mono*0.05
audio2_mono = audio2_mono[0:N1]
Q=20
# b2, a2 = filtro_passa_faixa(1000, Q, rate2)
b2, a2 = filtro_passa_baixa(5,rate2, 1000)
audiofiltrado_2= trata_audio(audio2_mono, b2, a2)

T2=  float(len(audio2_mono)/rate2)
N2 = len(audio2)
t2 = np.linspace(0, T2,N2, endpoint=False)
# ---------------Arquivo3--------------------------
arquivo3 = wave.open("projeto8\deep-abstract-ambient_snowcap-401656 (online-audio-converter.com).wav")
rate3, audio3 = wavfile.read("projeto8\deep-abstract-ambient_snowcap-401656 (online-audio-converter.com).wav")
audio3 = audio3*0.01
audio3_mono = audio3.mean(axis=2)
audio3_mono = audio3_mono
audio3_mono = audio3_mono[:N1]
Q=15

# b3, a3 = filtro_passa_faixa(1000, Q, rate3)
b3, a3 = filtro_passa_baixa(5,rate3, 1000)
audiofiltrado_3= trata_audio(audio3_mono, b3, a3)

T3=  float(len(audio3_mono)/rate3)
N3 = len(audio3)
t3 = np.linspace(0, T3,N3, endpoint=False)
# ---------------------------------------------


# -----------------plotagem dos originais ------------------------
# freqs, magnitude, magnitude_db = compute_fft(audiofiltrado_1, rate1, window=None, nfft=None, return_complex=False)
# plot_time_and_spectrum(t1, audiofiltrado_1, rate1 , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')

# freqs, magnitude, magnitude_db = compute_fft(audiofiltrado_2, rate2, window=None, nfft=None, return_complex=False)
# plot_time_and_spectrum(t2, audiofiltrado_2, rate2 , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')

# freqs, magnitude, magnitude_db = compute_fft(audiofiltrado_3, rate3, window=None, nfft=None, return_complex=False)
# plot_time_and_spectrum(t3, audiofiltrado_3, rate3 , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')

# plt.show()

# -------------------------------------
# -----------gerando sinais port----------
# --------------sinal 1---------------
f1 = 10500
# t1 = np.linspace(0, T1,N1, endpoint=False)
port1=1*np.sin(2*np.pi*f1*t1)
# --------------sinal 2---------------
f2 = 13500
# t2 = np.linspace(0, T2,N2, endpoint=False)
port2=1*np.sin(2*np.pi*f2*t1)
# --------------sinal 3---------------
f3 = 16500
# t3 = np.linspace(0, T3,N3, endpoint=False)
port3=1*np.sin(2*np.pi*f3*t1)

# ---------------modulado----------
mod1 = audiofiltrado_1*port1
mod2 = audiofiltrado_2*port2
mod3 = audiofiltrado_3*port3
modTotal = mod1+mod2+mod3
# ------------- plot modulados-----------
freqs, magnitude, magnitude_db = compute_fft(mod1, rate1, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t1, mod1, rate1 , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')

freqs, magnitude, magnitude_db = compute_fft(mod2, rate2, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t2, mod2, rate2 , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')

freqs, magnitude, magnitude_db = compute_fft(mod3, rate3, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t3, mod3, rate3 , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')

freqs, magnitude, magnitude_db = compute_fft(modTotal, rate3, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t3, modTotal, rate3 , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')
plt.show()

# ---------------filtro--------------
# --------------faixa1_-----------
f0 = 10500
q = 15
b11,a11 = filtro_passa_faixa(f0,q,rate1)
faixa1= trata_audio(modTotal, b11, a11)
b21, a21 = filtro_passa_baixa(5,rate3,12000)

faixa1= trata_audio(faixa1, b21, a21)

# --------------faixa2------------------
f0 = 13500
q = 25
b12,a12 = filtro_passa_faixa(f0,q,rate1)
faixa2= trata_audio(modTotal, b12, a12)
b22, a22 = filtro_passa_baixa(5,rate3,15000)
faixa2= trata_audio(faixa2, b22, a22)

# -----------faixa2--------------------------
f0 = 16500
q = 15
b13,a13 = filtro_passa_faixa(f0,q,rate1)
faixa3= trata_audio(modTotal, b13, a13)
b23, a23 = filtro_passa_baixa(5,rate3,18000)
faixa3= trata_audio(faixa3, b23, a23)

# ------------plot faixas-------------
freqs, magnitude, magnitude_db = compute_fft(faixa1, rate3, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t3, faixa1, rate3 , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')

freqs, magnitude, magnitude_db = compute_fft(faixa2, rate3, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t3, faixa2, rate3 , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')

freqs, magnitude, magnitude_db = compute_fft(faixa3, rate3, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t3, faixa3, rate3 , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')

plt.show()

# ----------------audivel---------------
faixa1_audivel = faixa1*port1

b21, a21 = filtro_passa_baixa(5,rate1,1000)
faixa1_audivel= trata_audio(faixa1_audivel, b21, a21)

# ----------------------
faixa2_audivel = faixa2*port2
b21, a21 = filtro_passa_baixa(5,rate2,1000)
faixa2_audivel= trata_audio(faixa2_audivel, b21, a21)
# --------------------
faixa3_audivel = faixa3*port3
b21, a21 = filtro_passa_baixa(5,rate3,1000)
faixa3_audivel= trata_audio(faixa3_audivel, b21, a21)
# --------------------------------
freqs, magnitude, magnitude_db = compute_fft(faixa1_audivel, rate1, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t1, faixa1_audivel, rate1 , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')


# freqs, magnitude, magnitude_db = compute_fft(audiofiltrado_3, rate3, window=None, nfft=None, return_complex=False)
# plot_time_and_spectrum(t3, audiofiltrado_3, rate3 , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')

freqs, magnitude, magnitude_db = compute_fft(faixa2_audivel, rate1, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t2, faixa2_audivel, rate2 , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')

freqs, magnitude, magnitude_db = compute_fft(faixa3_audivel, rate3, window=None, nfft=None, return_complex=False)
plot_time_and_spectrum(t3, faixa3_audivel, rate3 , freqs, magnitude, magnitude_db, x_label_time='Tempo (s)')

plt.show()

sd.play(audio1_mono,rate1)
sd.wait()
sd.play(faixa1_audivel,rate1)
sd.wait()
sd.play(audio2_mono,rate2)
sd.wait()
sd.play(faixa2_audivel,rate2)
sd.wait()

sd.play(audio3_mono,rate3)
sd.wait()
sd.play(faixa3_audivel,rate3)
sd.wait()