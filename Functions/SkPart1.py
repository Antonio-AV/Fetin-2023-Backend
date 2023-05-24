import numpy as np

def skPart1(notas, peso):
    maior = np.max(notas)
    menor = np.min(notas)

    if(maior == menor):
        maior += 0.1

    resultados = []
    for i in range(len(notas)):
        resultado = round(peso * (abs(maior-notas[i])/abs(maior-menor)),7)
        resultados.append(resultado)

    return resultados    