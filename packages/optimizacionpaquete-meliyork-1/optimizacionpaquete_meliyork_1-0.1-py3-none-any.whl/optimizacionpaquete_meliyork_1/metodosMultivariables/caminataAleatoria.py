import numpy as np

def caminata_aleatoria(f, x0, step, iter_max):
    x = x0
    for i in range(iter_max):
        x_nuevo = x + np.random.uniform(-step, step, size=x.shape)
        if f(x_nuevo) < f(x):
            x = x_nuevo
    return x