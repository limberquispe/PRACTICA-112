import math


class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def getDiscriminante(self):
        return self._b ** 2 - 4 * self._a * self._c

    def getRaiz1(self):
        d = self.getDiscriminante()
        if d < 0:
            return 0
        return (-self._b + math.sqrt(d)) / (2 * self._a)

    def getRaiz2(self):
        d = self.getDiscriminante()
        if d < 0:
            return 0
        return (-self._b - math.sqrt(d)) / (2 * self._a)


# -------- PROGRAMA DE PRUEBA --------

# Caso 1: dos raíces
ecuacion = EcuacionCuadratica(1.0, 3.0, 1.0)
d = ecuacion.getDiscriminante()

if d > 0:
    print("La ecuacion tiene dos raices",
          round(ecuacion.getRaiz1(), 6),
          "y",
          round(ecuacion.getRaiz2(), 5))
elif d == 0:
    print("La ecuacion tiene una raiz", ecuacion.getRaiz1())
else:
    print("La ecuacion no tiene raices reales")


# Caso 2: una raíz
ecuacion = EcuacionCuadratica(1.0, 2.0, 1.0)
d = ecuacion.getDiscriminante()

if d > 0:
    print("La ecuacion tiene dos raices",
          ecuacion.getRaiz1(), "y", ecuacion.getRaiz2())
elif d == 0:
    print("La ecuacion tiene una raiz", ecuacion.getRaiz1())
else:
    print("La ecuacion no tiene raices reales")


# Caso 3: sin raíces reales
ecuacion = EcuacionCuadratica(1.0, 2.0, 3.0)
d = ecuacion.getDiscriminante()

if d > 0:
    print("La ecuacion tiene dos raices",
          ecuacion.getRaiz1(), "y", ecuacion.getRaiz2())
elif d == 0:
    print("La ecuacion tiene una raiz", ecuacion.getRaiz1())
else:
    print("La ecuacion no tiene raices reales")