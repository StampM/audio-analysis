import matplotlib.pyplot as plt
import numpy as np

# apply variables

A = .8
f0 =  1000

phi = np.pi / 2
# sampling rate
fs = 44100

# do vector operations for time index - so use time as this

t = np.arange(-0.002, .002, 1.0/fs)

# - ready to compute function

x = A * cos(2 * np.pi * f0 * t + phi)

# plot x wrt t
'''
plt.plot(t,x)

# good practice, but should be auto
plt.axis([-0.002, .002, -0.8, .8])
plt.xlabel('time')
plt.ylabel('amplitude')

plt.show()
'''
# then shown in terminal through 'python sinusoids_pl.py'

# ==== Complex Sine Wave

N = 500 # in dft, size of dft
k = 3
n = np.arange(-N / 2, N / 2) # best way to show as then over 1

s = np.exp(1j * 2 * np.pi * k * n / N)
# to display , cannot be complex in 2-D

plt.plot(n, np.real(s))
# plt.plot(n, np.imag(s))

plt.xlabel('indexes')
plt.ylabel('amplitude')
plt.axis([-N/2, N/2, -1, 1])
plt.show()

# complex sine wave shown - cosine output - k = 3 so 3 periods seen

# imaginary - 3 periods of sine function

# in DFT - for different sinusoids to compare