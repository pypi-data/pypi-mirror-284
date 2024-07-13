
def newton_raphson(x_0, f, E):
    def primera_derivada(x, f):
        delta = 0.0001
        return (f(x + delta) - f(x - delta)) / (2 * delta)

    def segunda_derivada(x, f):
        delta = 0.0001
        return (f(x + delta) - 2 * f(x) + f(x - delta)) / (delta ** 2)
    
    k = 1

    while True:
        f_primera = primera_derivada(x_0, f)
        f_segunda = segunda_derivada(x_0, f)
        x_next = x_0 - (f_primera / f_segunda)
        f_prima_next = primera_derivada(x_next, f)
        
        if abs(f_prima_next) < E:
            break
        
        k += 1
        x_0 = x_next

    return x_next