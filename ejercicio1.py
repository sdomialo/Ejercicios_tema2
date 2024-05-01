import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Cuadrante I"
        elif self.x < 0 and self.y > 0:
            return "Cuadrante II"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante III"
        elif self.x > 0 and self.y < 0:
            return "Cuadrante IV"
        elif self.x == 0 and self.y != 0:
            return "Sobre eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre eje X"
        else:
            return "Origen"

    def vector(self, otro_punto):
        return Punto(otro_punto.x - self.x, otro_punto.y - self.y)

    def distancia(self, otro_punto):
        distancia = math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)
        print(f"La distancia entre {self} y {otro_punto} es {distancia}")

class Rectangulo:
    def __init__(self, punto1=Punto(), punto2=Punto()):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto2.x - self.punto1.x)

    def altura(self):
        return abs(self.punto2.y - self.punto1.y)

    def area(self):
        return self.base() * self.altura()

# Creación de los puntos
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto()

# Imprimir los puntos
print("Puntos:")
print("A:", A)
print("B:", B)
print("C:", C)
print("D:", D)

# Consultar cuadrantes
print("\nCuadrantes:")
print("Cuadrante de A:", A.cuadrante())
print("Cuadrante de C:", C.cuadrante())
print("Cuadrante de D:", D.cuadrante())

# Consultar vectores AB y BA
print("\nVectores:")
print("Vector AB:", A.vector(B))
print("Vector BA:", B.vector(A))

# Consultar distancia entre puntos A y B, y B y A
A.distancia(B)
B.distancia(A)

# Determinar punto más lejano al origen entre A, B y C
puntos = [A, B, C]
distancias_al_origen = [math.sqrt(p.x**2 + p.y**2) for p in puntos]
indice_mas_lejano = distancias_al_origen.index(max(distancias_al_origen))
print(f"\nEl punto más lejano al origen es: {puntos[indice_mas_lejano]}")

# Crear un rectángulo utilizando los puntos A y B
rectangulo_AB = Rectangulo(A, B)

# Consultar base, altura y área del rectángulo
print("\nPropiedades del rectángulo AB:")
print("Base:", rectangulo_AB.base())
print("Altura:", rectangulo_AB.altura())
print("Área:", rectangulo_AB.area())