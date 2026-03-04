import math


class Estadistica:
    def __init__(self, datos):
        self._datos = datos

    def promedio(self):
        suma = 0
        for x in self._datos:
            suma += x
        return suma / len(self._datos)

    def desviacion(self):
        prom = self.promedio()
        suma = 0
        for x in self._datos:
            suma += (x - prom) ** 2
        return math.sqrt(suma / (len(self._datos) - 1))


# -------- PROGRAMA DE PRUEBA --------

datos = [1.9, 2.5, 3.7, 2, 1, 6, 3, 4, 5, 2]

estadistica = Estadistica(datos)

print("El promedio es", round(estadistica.promedio(), 2))
print("La desviacion estandar es", round(estadistica.desviacion(), 5))