import numpy as np

def cauchy(f, x0, epsilon1, epsilon2,  maxiter, metodo):
    def gradiente(f, x, deltaX=0.001):
        grad=[]
        for i in range(0, len(x)):
            xp=x.copy()
            xn=x.copy()
            xp[i]=xp[i]+deltaX
            xn[i]=xn[i]-deltaX
            grad.append((f(xp)-f(xn))/(2*deltaX))
        return grad
    
    terminar=False
    xk=x0
    k=0

    while not terminar:
        grad=np.array(gradiente(f, xk))

        if np.linalg.norm(grad)<epsilon1 or k>=maxiter:
            terminar=True
        else:
            def alpha_funcion(alpha):
                return f(xk-alpha*grad)
            
            alpha=metodo(alpha_funcion, e=epsilon2, a=0.0, b=1.0) 
            x_k1=xk-alpha*grad

            if np.linalg.norm(x_k1-xk)/(np.linalg.norm(xk)+0.00001) <= epsilon2:
                terminar=True
            else:
                k=k+1
                xk=x_k1
    return xk