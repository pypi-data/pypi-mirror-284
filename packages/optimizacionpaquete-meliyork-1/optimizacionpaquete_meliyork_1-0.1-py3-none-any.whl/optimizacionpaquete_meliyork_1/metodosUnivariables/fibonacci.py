

def fibonacci_search(f, e, a, b):
    
    '''
    Recibe:
    a: limite inferior del intervalo de acuerdo a la funcion
    b: limite superior del intervalo
    n: número deseado de evaluaciones de la función objetivo 
    f: funcion objetivo

    '''
    
    L = b - a

    fib = [0, 1]
    while len(fib) <= e +2:
        fib.append(fib[-1] + fib[-2])

    
    k = 2

    while k < e:
        Lk = (fib[e - k + 2] / fib[e+ 2]) * L

        x1 = a + Lk
        x2 = b - Lk

        fx1 = f(x1)
        fx2 = f(x2)

        if fx1 < fx2:
            b = x2
        elif fx1 > fx2:
            a = x1
        elif fx1 == fx2:
            a=x1
            b=x2

        
        k += 1

    return a+b/2