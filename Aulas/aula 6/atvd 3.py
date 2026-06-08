class Forma:
    def area(self):
        return 0

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

formas = [
    Triangulo(base=10, altura=5),
    Quadrado(lado=4),
    Triangulo(base=6, altura=3),
    Quadrado(lado=7)
]

for i, forma in enumerate(formas, 1):
    print(f"Área da forma {i}: {forma.area()}")