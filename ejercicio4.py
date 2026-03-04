import math


def promedio(valores):
    suma = 0
    for x in valores:
        suma += x
    return suma / len(valores)


def desviacion(valores):
    prom = promedio(valores)
    suma = 0
    for x in valores:
        suma += (x - prom) ** 2
    return math.sqrt(suma / (len(valores) - 1))


# -------- PROGRAMA PRINCIPAL --------

datos = [1.9, 2.5, 3.7, 2, 1, 6, 3, 4, 5, 2]

prom = promedio(datos)
desv = desviacion(datos)

print("El promedio es", round(prom, 2))
print("La desviacion estandar es", round(desv, 5))