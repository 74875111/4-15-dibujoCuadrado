class CuadradoDibujador:
    def __init__(self, size):
        self.size = int(input("Ingrese tamaño del cuadrado a dibujar: "))
        self.lista = []
        self.generar_cuadrado()

    def generar_cuadrado(self):
        for i in range(self.size):
            row = []
            if i == 0 or i == self.size - 1:
                row = ["*"] * self.size
            else:
                row = ["*"] + [" "] * (self.size - 2) + ["*"]
            self.lista.append(row)

    def print(self):
        for row in self.lista:
            print(" ".join(row))
