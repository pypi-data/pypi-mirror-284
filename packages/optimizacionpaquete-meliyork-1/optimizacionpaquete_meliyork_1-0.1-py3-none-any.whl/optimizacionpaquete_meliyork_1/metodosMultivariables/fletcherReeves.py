import numpy as np

def fletcherReeves(f, x0, epsilon1, epsilon2, epsilon3, metodo):
    def gradiente(f, x, deltaX=0.001):
        grad = []
        for i in range(len(x)):
            xp = x.copy()
            xn = x.copy()
            xp[i] = xp[i] + deltaX
            xn[i] = xn[i] - deltaX
            grad.append((f(xp) - f(xn)) / (2 * deltaX))
        return np.array(grad)

    x = x0
    grad = gradiente(f, x)
    s = -grad
    k = 0

    while True:
        alpha = metodo(lambda alpha: f(x + alpha * s), e=epsilon1, a=0.0, b=1.0)
        x_next = x + alpha * s
        grad_next = gradiente(f, x_next)

        if np.linalg.norm(x_next - x) / np.linalg.norm(x) <= epsilon2 or np.linalg.norm(grad_next) <= epsilon3:
            break

        beta = np.linalg.norm(grad_next) ** 2 / np.linalg.norm(grad) ** 2
        s = -grad_next + beta * s

        x = x_next
        grad = grad_next
        k += 1

    return x