#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

#设置时间范围，和相应的曲线函数。
time_step = 0.02
period = 5.
time_vec = np.arange(0, 20, time_step)
sig = np.sin(2 * np.pi / period * time_vec) + 0.5 * np.random.randn(time_vec.size)


#对sig进行快速傅里叶变换（FFT）
sample_freq = fftpack.fftfreq(sig.size, d=time_step)
sig_fft = fftpack.fft(sig)

#对变换后的曲线进行处理。
pidxs = np.where(sample_freq > 0)
freqs = sample_freq[pidxs]
power = np.abs(sig_fft)[pidxs]
freq = freqs[power.argmax()]
sig_fft[np.abs(sample_freq) > freq] = 0
main_sig = fftpack.ifft(sig_fft)


plt.figure()

plt.plot(time_vec, sig)
plt.plot(time_vec, main_sig, linewidth=3, color='red')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.show()
