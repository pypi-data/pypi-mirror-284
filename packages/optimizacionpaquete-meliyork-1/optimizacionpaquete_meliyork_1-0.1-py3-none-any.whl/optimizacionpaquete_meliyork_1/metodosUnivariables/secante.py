import numpy as np

def secante(f, e, a, b):
    
    def primera_derivada(x, f):
        delta = 0.0001
        return (f(x + delta) - f(x - delta)) / (2 * delta)
       
    a = np.random.uniform(a, b)
    b = np.random.uniform(a, b)
    x1 = a
    x2 = b
    
    while True:
        z= x2- ( (primera_derivada(x2, f))  / (    ( (primera_derivada(x2, f)) - (primera_derivada(x1,f)) ) /   (x2-x1)   )     )
        f_primaz = primera_derivada(z, f)
    
        if abs(x2 - x1) < e: 
            break
        elif f_primaz < 0:
            x1 = z
        elif f_primaz > 0:
            x2 = z

    return x1+x2/2