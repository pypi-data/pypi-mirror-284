import numpy as np 

def hooke_jeeves(f, x_initial, delta, alpha, epsilon):
    def movimiento_exploratorio(xc, delta, func):
        x = np.copy(xc)
        for i in range(len(x)):
            f = func(x)
            x[i] += delta[i]
            f_mas = func(x)
            if f_mas < f:
                f = f_mas
            else:
                x[i] -= 2*delta[i]
                f_menos = func(x)
                if f_menos < f:
                    f = f_menos
                else:
                    x[i] += delta[i]
        return x
    
    x = np.array(x_initial)
    delta = np.array(delta)
    while True:
        x_nuevo = movimiento_exploratorio(x, delta, f)
        
        if np.array_equal(x, x_nuevo):
            if np.linalg.norm(delta) < epsilon:
                break
            else:
                delta /= alpha
                continue
        
        x_p = x_nuevo + (x_nuevo - x)
        x_p_nuevo = movimiento_exploratorio(x_p, delta, f)
        
        if f(x_p_nuevo) < f(x_nuevo):
            x = x_p_nuevo
        else:
            x = x_nuevo
    
    return x