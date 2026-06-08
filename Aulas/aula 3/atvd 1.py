class Produto:
    def __init__(self, nome, preco):
        self.nome  = nome
        self.preco = preco

p1 = Produto("Caderno", 12.90)
p2 = Produto("Caneta", 3.50)

print(p1.nome, p1.preco)
print(p2.nome, p2.preco)