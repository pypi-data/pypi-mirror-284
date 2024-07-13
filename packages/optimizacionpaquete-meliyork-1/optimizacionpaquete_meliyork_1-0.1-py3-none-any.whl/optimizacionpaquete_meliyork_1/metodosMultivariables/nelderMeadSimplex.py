import numpy as np

def nelder_mead(funcion, inicio):
    dimensiones = len(inicio)
    alfa = 1.0
    gamma = 2.0
    beta = 0.5
    tolerancia = 1e-5
    iter_max = 1000
    
    delta1 = (np.sqrt(dimensiones + 1) + dimensiones - 1) / (dimensiones * np.sqrt(2)) * alfa
    delta2 = (np.sqrt(dimensiones + 1) - 1) / (dimensiones * np.sqrt(2)) * alfa
    
    simplex = np.zeros((dimensiones + 1, dimensiones))
    simplex[0] = inicio
    
    for i in range(1, dimensiones + 1):
        punto = inicio.copy()
        punto[i - 1] += delta1
        for j in range(dimensiones):
            if j != i - 1:
                punto[j] += delta2
        simplex[i] = punto
    
    for iteracion in range(iter_max):
        simplex = sorted(simplex, key=funcion)
        simplex = np.array(simplex)
        
        centroide = np.mean(simplex[:-1], axis=0)
        reflexion = 2 * centroide - simplex[-1]
        
        if funcion(reflexion) < funcion(simplex[0]):
            expansion = centroide + gamma * (centroide - simplex[-1])
            nuevo_punto = expansion if funcion(expansion) < funcion(reflexion) else reflexion
        elif funcion(reflexion) >= funcion(simplex[-2]):
            if funcion(reflexion) < funcion(simplex[-1]):
                contraccion_fuera = centroide + beta * (reflexion - centroide)
                nuevo_punto = contraccion_fuera
            else:
                contraccion_dentro = centroide - beta * (centroide - simplex[-1])
                nuevo_punto = contraccion_dentro
        else:
            nuevo_punto = reflexion
        
        simplex[-1] = nuevo_punto
        
        if np.sqrt(np.mean([(funcion(x) - funcion(centroide))**2 for x in simplex])) <= tolerancia:
            break

    simplex = sorted(simplex, key=funcion)
    simplex = np.array(simplex)
    
    return simplex[0]