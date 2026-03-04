import time
import random


class Cronometro:
    def __init__(self):
        self._inicia = time.time()
        self._finaliza = 0.0

    def get_inicia(self):
        return self._inicia

    def get_finaliza(self):
        return self._finaliza

    def inicia(self):
        self._inicia = time.time()

    def detener(self):
        self._finaliza = time.time()

    def lapsoDeTiempo(self):
        return (self._finaliza - self._inicia) * 1000


def ordenacion_seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        aux = lista[i]
        lista[i] = lista[minimo]
        lista[minimo] = aux


# ---------------- PROGRAMA PRINCIPAL ----------------

cantidad = 10000   
numeros = []

for i in range(cantidad):
    numeros.append(random.randint(1, 100000))

cronometro = Cronometro()

cronometro.inicia()
ordenacion_seleccion(numeros)
cronometro.detener()

print("Cantidad de datos:", cantidad)
print("Tiempo de ejecucion (ms):", cronometro.lapsoDeTiempo())