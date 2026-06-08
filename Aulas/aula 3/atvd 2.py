class Produto:
    def __init__(self, nome, preco):
        self.nome  = nome
        self.preco = preco

    def desconto(self, percentual):
        fator = percentual / 100
        return self.preco - (self.preco * fator)

p1 = Produto("Notebook", 100.0)
print(p1.desconto(10)) 
print(p1.desconto(25))  