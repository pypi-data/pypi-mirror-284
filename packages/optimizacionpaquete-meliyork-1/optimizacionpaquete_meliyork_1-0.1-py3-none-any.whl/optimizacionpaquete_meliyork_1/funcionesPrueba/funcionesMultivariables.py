import numpy as np 

def rastrigin(x):
        A=10
        n = len(x)
        return A * n + np.sum(x**2 - A * np.cos(2 * np.pi * x))

def ackley(x):
    a = 20
    b = 0.2
    c = 2 * np.pi
    suma1 = x[0]**2 + x[1]**2
    suma2 = np.cos(c * x[0]) + np.cos(c * x[1])
    term1 = -a * np.exp(-b * np.sqrt(0.5 * suma1))
    term2 = -np.exp(0.5 * suma2)
    resul = term1 + term2 + a + np.exp(1)
    return resul

def himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

def sphere(x):
    return np.sum(np.square(x))

def rosenbrock(x):
    return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

def beale(x):
    return ((1.5 - x[0] + x[0] * x[1])**2 +
            (2.25 - x[0] + x[0] * x[1]**2)**2 +
            (2.625 - x[0] + x[0] * x[1]**3)**2)

def goldstein(self, x):
    a = (1 + (x[0] + x[1] + 1)**2 * 
                 (19 - 14 * x[0] + 3 * x[0]**2 - 14 * x[1] + 6 * x[0] * x[1] + 3 * x[1]**2))
    b = (30 + (2 * x[0] - 3 * x[1])**2 * 
                 (18 - 32 * x[0] + 12 * x[0]**2 + 48 * x[1] - 36 * x[0] * x[1] + 27 * x[1]**2))
    return a * b

def booth(x):
    return (x[0] + 2 * x[1] - 7)**2 + (2 * x[0] + x[1] - 5)**2

def bunkin(x):
    return 100 * np.sqrt(np.abs(x[1] - 0.001 * x[0]**2)) + 0.01 * np.abs(x[0] + 10)

def matyas(x):
        return 0.26 * (x[0]**2 + x[1]**2) - 0.48 * x[0] * x[1]

def levi(x):
    a = np.sin(3 * np.pi * x[0])**2
    b= (x[0] - 1)**2 * (1 + np.sin(3 * np.pi * x[1])**2)
    c= (x[1] - 1)**2 * (1 + np.sin(2 * np.pi * x[1])**2)
    return a + b + c

def threehumpcamel(x):
    return 2 * x[0]**2 - 1.05 * x[0]**4 + (x[0]**6) / 6 + x[0] * x[1] + x[1]**2

def easom(x):
    return -np.cos(x[0]) * np.cos(x[1]) * np.exp(-(x[0] - np.pi)**2 - (x[1] - np.pi)**2)

def crossintray(x):
    op = np.abs(np.sin(x[0]) * np.sin(x[1]) * np.exp(np.abs(100 - np.sqrt(x[0]**2 + x[1]**2) / np.pi)))
    return -0.0001 * (op + 1)**0.1

def eggholder(x):
    a = -(x[1] + 47) * np.sin(np.sqrt(np.abs(x[0] / 2 + (x[1] + 47))))
    b = -x[0] * np.sin(np.sqrt(np.abs(x[0] - (x[1] + 47))))
    return a + b

def holdertable(x):
    return -np.abs(  np.sin(x[0])*np.cos(x[1]) * np.exp(np.abs(1-((np.sqrt(x[0]**2 + x[1]**2))/(np.pi))))   )

def mccormick(x):
    return np.sin(x[0] + x[1]) + (x[0] - x[1])**2 - 1.5 * x[0] + 2.5 * x[1] + 1

def schaffer2(x):
        numerador = np.sin(x[0]**2 - x[1]**2)**2 - 0.5
        denominador = (1 + 0.001 * (x[0]**2 + x[1]**2))**2
        return 0.5 + numerador / denominador

def schaffer_n4(x):
    term1 = np.cos(np.sin(np.abs(x[0]**2 - x[1]**2)))**2
    term2 = 1 + 0.001 * (x[0]**2 + x[1]**2)
    return 0.5 + (term1 - 0.5) / term2

def styblinskitang(x):
    return np.sum(x**4 - 16 * x**2 + 5 * x) / 2

def shekel(x):
    a = np.array([[4, 4, 4, 4],
                [1, 1, 1, 1]])
    c = np.array([0.1, 0.2, 0.2, 0.4])
    result = 0
    for i in range(len(c)):
        result += 1 / (c[i] + (x[0] - a[0, i])**2 + (x[1] - a[1, i])**2)
    return result





