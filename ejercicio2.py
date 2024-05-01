class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Color {self.color}, {self.ruedas} ruedas"


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f", {self.velocidad} km/h, {self.cilindrada} cc"


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + f", {self.carga} kg"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f", {self.tipo}"


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f", {self.velocidad} km/h, {self.cilindrada} cc"


def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos_filtrados = [vehiculo for vehiculo in vehiculos if vehiculo.ruedas == ruedas]
        print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
        for vehiculo in vehiculos_filtrados:
            print(f"- {type(vehiculo).__name__}: {vehiculo}")
    else:
        print("Todos los vehículos:")
        for vehiculo in vehiculos:
            print(f"- {type(vehiculo).__name__}: {vehiculo}")


# Crear objetos de cada subclase y añadirlos a la lista vehiculos
coche = Coche("azul", 4, 150, 1200)
camioneta = Camioneta("blanco", 4, 120, 2200, 1500)
bicicleta = Bicicleta("verde", 2, "urbana")
motocicleta = Motocicleta("negra", 2, "deportiva", 180, 900)

vehiculos = [coche, camioneta, bicicleta, motocicleta]

# Probar la función catalogar con diferentes valores de ruedas
catalogar(vehiculos)
print("\n")
catalogar(vehiculos, 0)
print("\n")
catalogar(vehiculos, 2)
print("\n")
catalogar(vehiculos, 4)