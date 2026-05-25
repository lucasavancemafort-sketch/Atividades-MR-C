class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


produto1 = Produto("Notebook", 3500.00)
produto2 = Produto("Mouse", 150.00)

print(f"Produto: {produto1.nome} | Preço: R$ {produto1.preco:.2f}")
print(f"Produto: {produto2.nome} | Preço: R$ {produto2.preco:.2f}")