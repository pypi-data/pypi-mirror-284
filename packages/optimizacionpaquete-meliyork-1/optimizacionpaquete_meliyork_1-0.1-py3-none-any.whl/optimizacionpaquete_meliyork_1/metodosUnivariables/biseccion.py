import numpy as np

def biseccion(f, e, a, b):
    def primera_derivada(x, f):
        delta = 0.0001
        return (f(x + delta) - f(x - delta)) / (2 * delta)
    
    a = np.random.uniform(a, b)
    b = np.random.uniform(a, b)
    
    while(primera_derivada(a,f) > 0):
        a = np.random.uniform(a, b)
    
    while (primera_derivada(b,f) < 0): 
        b = np.random.uniform(a, b)
    
    x1=a
    x2=b
    
    while True:
        z = (x1 + x2) / 2
        f_primaz = primera_derivada(z, f)
    
        if abs(f_primaz) < e:  
            break
        elif f_primaz < 0:
            x1 = z
        elif f_primaz > 0:
            x2 = z

    return x1+x2/2

