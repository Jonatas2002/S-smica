import numpy as np

# Modelo 1D
def model_1D(nz, dx, dimensao, valor):
    """ Função responsavel pela criação de matrizes 1D utilizada para contrução de modelos
        de velocidade, densidade e outras utilidades"""
    M = np.zeros(nz)
    
    for i in range(len(dimensao)):
        start_dimensao = int(dimensao[i - 1] / dx) if i > 0 else 0
        end_dimensao = int(dimensao[i] // dx)
        M[start_dimensao:end_dimensao] = valor[i]

    return M

# Wavelet Ricker
def Ricker(fs,t):
    R = (1 - 2 * np.pi**2 * fs**2 * t**2 ) * (np.exp(-np.pi**2 * fs**2 * t**2))
    return R

# Calculo da Refletividade
def reflectivity(velocidade, densidade):
    z = densidade * velocidade
    refl = np.zeros(len(z))

    for i in range(len(z)-1):
        z2 = z[i+1]
        z1 = z[i]
        refl[i] = (z2 - z1) / (z2 + z1)

    return refl