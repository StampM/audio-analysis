
# show how to implement the DFT

# DFT X[k] = sum ( x[n] complex sin)
# IDFT x[n] - iterate over time  to compute inverse sum

import numpy as np
import matplotlib.pyplot as plt

# iniital vars
N = 8
k0 = 2
n = 1

x = np.exp(1j * 2 * np.pi * k0 * n / N * np.arange(N))


# initialize output
X = np.array([])

# iterate over Function samples:
for k in range(N):
    1
    # create complex exp at every k
    s = np.exp(1j * 2 * np.pi * k * n / N * np.arange(N))

    # then apply via complex exponentials with dot product
    X = np.append(X, sum(x*np.conjugate(s)))
# X - then entire DFT output

# could makenp.arange(N) as var as repeated - just show absolute as complex X
plt.plot(np.arange(N), abs(X))


plt.show()

# output - shows just the frequency peak of 64 at location 7
# proves that signal was pure sinusoid
'''
# ==== REal Signal

# only change is cosine instead of complex exp it is cosine
x = np.cos(2 * np.pi * k0 / N * np.arange(N))

# apply same as above - now 2 peaks seen which is not as inuitive.

# better to go through -N/2 to N/2 asoutoput is more intuitive.
nv = np.arange(-N/2, N/2)
kv = np.arange(-N/2, N/2)

# then re-apply DFT wiht nv/kv
for k in kv:
    s = np.exp(1j * 2 * np.pi * k * n / N * nv)
    X = np.append(X, sum(x*np.conjugate(s)))

# now when speaks are shown - it is -7 and 7 frequncy.

N = 7.5
# when this projection into complex sinusoids does not show singular value
# positive for all values but with peak around N


# ==== Inverse DFT ====

# have DFT analysis above as input
y = np.array([])

for n in nv:
    s = np.exp(1j * 2 * np.pi *  n / N * kv) # s - sum of frequencies at given sample

    y = np.append(y, (1/N) * sum(X * s)) # inverse norm with X DFT output as input

plt.plot(kv, y) # kv step as 'time'
plt.axis([-N/2, N/2, -1, 1])
plt.show()
# this shows the 7.5 periods
'''