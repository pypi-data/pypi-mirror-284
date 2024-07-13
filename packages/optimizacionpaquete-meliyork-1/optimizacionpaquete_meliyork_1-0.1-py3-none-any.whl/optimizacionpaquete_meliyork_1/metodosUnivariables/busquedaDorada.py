import numpy as np

def busquedaDorada(funcion, e:float, a:float=None, b:float=None)->float:
    '''
    Recibe:
    a: limite inferior del intervalo de acuerdo a la funcion
    b: limite superior del intervalo
    e: criterio de terminacion
    f: funcion objetivo

    '''
    def regla_eliminacion(x1, x2, fx1, fx2, a, b)->tuple[float, float]:
        if fx1>fx2:
            return x1, b
        
        if fx1<fx2:
            return a, x2
        
        return x1, x2 

    def w_to_x(w:float, a, b)->float:
        return w*(b-a)+a 
    
    phi=(1 + np.math.sqrt(5) )/ 2 - 1
    aw, bw=0,1
    Lw=1
    k=1

    while Lw>e:
        w2=aw+phi*Lw
        w1=bw-phi*Lw
        aw, bw=regla_eliminacion(w1, w2, funcion(w_to_x(w1, a, b)), funcion(w_to_x(w2, a, b)), aw, bw)
        k+=1
        Lw=bw-aw

    return(w_to_x(aw, a, b)+w_to_x(bw, a, b))/2

