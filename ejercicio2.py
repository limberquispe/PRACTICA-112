class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._e = e
        self._f = f

    def tieneSolucion(self):
        return (self._a * self._d - self._b * self._c) != 0

    def getX(self):
        return (self._e * self._d - self._b * self._f) / (self._a * self._d - self._b * self._c)

    def getY(self):
        return (self._a * self._f - self._e * self._c) / (self._a * self._d - self._b * self._c)


# ---------------- PROGRAMA DE PRUEBA ----------------

entrada = input("Ingrese a, b, c, d, e, f: ")
valores = entrada.split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
d = float(valores[3])
e = float(valores[4])
f = float(valores[5])

ecuacion = EcuacionLineal(a, b, c, d, e, f)

if ecuacion.tieneSolucion():
    print("x =", ecuacion.getX(), ", y =", ecuacion.getY())
else:
    print("La ecuacion no tiene solucion")