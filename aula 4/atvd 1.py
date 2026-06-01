class Produto:
    def __init__(self, nome, preco):
        self.__nome  = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def set_nome(self, nome):
        if len(nome) > 0:
            self.__nome = nome
        else:
            print("Erro: nome não pode ser vazio")

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Erro: preço não pode ser negativo")

p = Produto("Caderno", 12.90)
print(p.get_nome(), p.get_preco())
p.set_preco(15.00)   
p.set_preco(-5)     
print(p.get_preco())