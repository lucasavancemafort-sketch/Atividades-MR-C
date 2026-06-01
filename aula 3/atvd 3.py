class Carro:
    def __init__(self, marca, modelo):
        self.marca     = marca
        self.modelo    = modelo
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade = max(0, self.velocidade - 10)

carro = Carro("Toyota", "Corolla")

carro.acelerar()   
carro.acelerar()   
carro.acelerar()   
carro.frear()      

print(carro.velocidade)  