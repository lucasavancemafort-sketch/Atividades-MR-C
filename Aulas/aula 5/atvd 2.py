class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano   = ano

    def informacoes(self):
        print(f"Marca: {self.marca} | Ano: {self.ano}")


class Carro(Veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.portas = portas

    def informacoes(self):
        super().informacoes()
        print(f"Portas: {self.portas}")


class Moto(Veiculo):
    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

    def informacoes(self):
        super().informacoes()
        print(f"Cilindradas: {self.cilindradas}cc")


carro = Carro("Toyota", 2022, 4)
moto  = Moto("Honda", 2021, 300)

carro.informacoes()
print()
moto.informacoes()