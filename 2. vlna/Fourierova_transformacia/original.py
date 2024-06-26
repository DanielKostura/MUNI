from numpy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import numpy as np


N = 600
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N, endpoint=False)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = fftfreq(N, T)[:N//2]
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()

# 10
# 10, 30

# 10
# 10, 20

# 10
# 5, 20