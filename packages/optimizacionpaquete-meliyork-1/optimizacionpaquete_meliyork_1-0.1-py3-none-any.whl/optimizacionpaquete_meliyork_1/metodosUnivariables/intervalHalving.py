
def interval_halving_method(f, e, a, b):
    '''
    Recibe:
    a: limite inferior del intervalo de acuerdo a la funcion
    b: limite superior del intervalo
    E: criterio de terminacion
    f: funcion objetivo

    '''
    L = b - a
    xm = (a + b) / 2

    while True:
        x1 = a + (L / 4)
        x2 = b - (L / 4)

        fx1 = f(x1)
        fx2 = f(x2)
        fxm = f(xm)

        if fx1 < fxm:
            b = xm
            xm = x1
        else:
            if fx2 < fxm:
                a = xm
                xm = x2
            else:
                a = x1
                b = x2

        L = b - a
        if abs(L) < e:
            return x1+x2/2 
        