class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        return self.preco * (1 - percentual / 100)


produto1 = Produto("Notebook", 3500.00)
produto2 = Produto("Mouse", 150.00)

novo_preco1 = produto1.desconto(10)
novo_preco2 = produto2.desconto(25)

print(f"{produto1.nome}: de R$ {produto1.preco:.2f} por R$ {novo_preco1:.2f} (10% de desconto)")
print(f"{produto2.nome}: de R$ {produto2.preco:.2f} por R$ {novo_preco2:.2f} (25% de desconto)")