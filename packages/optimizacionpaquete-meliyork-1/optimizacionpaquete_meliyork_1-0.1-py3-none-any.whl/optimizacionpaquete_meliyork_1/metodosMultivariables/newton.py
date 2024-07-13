import numpy as np

def newton(f, x0, epsilon1, epsilon2, maxiter, metodo):
    terminar = False
    xk = x0
    k = 0

    def gradiente(f, x, deltaX=0.001):
        grad = []
        for i in range(len(x)):
            xp = x.copy()
            xn = x.copy()
            xp[i] = xp[i] + deltaX
            xn[i] = xn[i] - deltaX
            grad.append((f(xp) - f(xn)) / (2 * deltaX))
        return np.array(grad)
    
    def hessian_matrix(f, x, deltaX):
        fx = f(x)
        N = len(x)
        H = []
        for i in range(N):
            hi = []
            for j in range(N):
                if i == j:
                    xp = x.copy()
                    xn = x.copy()
                    xp[i] = xp[i] + deltaX
                    xn[i] = xn[i] - deltaX
                    hi.append((f(xp) - 2 * fx + f(xn)) / (deltaX ** 2))
                else:
                    xpp = x.copy()
                    xpn = x.copy()
                    xnp = x.copy()
                    xnn = x.copy()
                    xpp[i] = xpp[i] + deltaX
                    xpp[j] = xpp[j] + deltaX
                    xpn[i] = xpn[i] + deltaX
                    xpn[j] = xpn[j] - deltaX
                    xnp[i] = xnp[i] - deltaX
                    xnp[j] = xnp[j] + deltaX
                    xnn[i] = xnn[i] - deltaX
                    xnn[j] = xnn[j] - deltaX
                    hi.append((f(xpp) - f(xpn) - f(xnp) + f(xnn)) / (4 * deltaX ** 2))
            H.append(hi)
        return np.array(H)

    while not terminar:
        grad = np.array(gradiente(f, xk))
        hessian = hessian_matrix(f, xk, deltaX=0.001)
        hessian_inv = np.linalg.inv(hessian)

        if np.linalg.norm(grad) < epsilon1 or k >= maxiter:
            terminar = True
        else:
            def alpha_funcion(alpha):
                return f(xk - alpha * np.dot(hessian_inv, grad))

            alpha = metodo(alpha_funcion, e=epsilon2, a=0.0, b=1.0)
            x_k1 = xk - alpha * np.dot(hessian_inv, grad)

            if np.linalg.norm(x_k1 - xk) / (np.linalg.norm(xk) + 0.00001) <= epsilon2:
                terminar = True
            else:
                k += 1
                xk = x_k1
    return xk
