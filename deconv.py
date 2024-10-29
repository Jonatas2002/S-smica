import numpy as np
import matplotlib.pyplot as plt
from function import model_1D
from function import Ricker
from function import reflectivity

# Parametros geral
# Construindo o modelo VP e RHOB
nz = 501
time = 1
dt = time/nz

t = np.arange(nz) * dt
print('dt = ',dt)

interfaces = np.array([0.2, 0.4, 0.6, 0.8, 1])
vp = np.array([1500, 2200, 4500, 5000, 3000])
rhob = np.array([1000, 1800, 2200, 2500, 2000 ])

VP = model_1D(nz, dt, interfaces, vp)
RHOB = model_1D(nz, dt, interfaces, rhob)

wavelet = Ricker(fs=25, t=t-0.5)
refletividade = reflectivity(VP, RHOB)
trace = np.convolve(refletividade, wavelet, mode='same')

# Tentativa de deconvolução com Wiener
fator = 0.1  # Parâmetro de regularização para o filtro de Wiener
deconvolve = np.convolve(trace, wavelet / (wavelet**2 + fator), mode='same')

plt.figure()

plt.subplot(151)
plt.title('VP')
plt.plot(VP, t)
plt.xlabel('Time [s]')
plt.ylabel(' VP [m/s]')
plt.ylim(max(t),min(t))

plt.subplot(152)
plt.title('RHOB')
plt.plot(RHOB, t)
plt.xlabel('Time [s]')
plt.ylabel(' RHOB [kg/m]')
plt.ylim(max(t),min(t))

plt.subplot(153)
plt.title('reflectivity')
plt.plot(refletividade, t)
plt.xlabel('Time [s]')
plt.ylabel('reflectivity')
plt.ylim(max(t),min(t))

plt.subplot(154)
plt.title('Trace')
plt.plot(trace, t)
plt.xlabel('Time [s]')
plt.ylabel('Trace')
plt.ylim(max(t),min(t))

plt.subplot(155)
plt.title('Trace')
plt.plot(deconvolve, t)
plt.xlabel('Time [s]')
plt.ylabel('Trace')
plt.ylim(max(t),min(t))

plt.tight_layout()
plt.show()