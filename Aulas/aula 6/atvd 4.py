class Pagamento:
    def processar(self, valor):
        return valor

class Dinheiro(Pagamento):
    def processar(self, valor):
        return valor * 0.95

class Cartao(Pagamento):
    def processar(self, valor):
        return valor * 1.02

class Pix(Pagamento):
    def processar(self, valor):
        return valor

formas_pagamento = [Dinheiro(), Cartao(), Pix()]
valor_base = 100.00

print(f"Valor original do pagamento: R$ {valor_base:.2f}\n")

for forma in formas_pagamento:
    nome_forma = forma.__class__.__name__
    valor_final = forma.processar(valor_base)
    print(f"Forma: {nome_forma} -> Valor Final: R$ {valor_final:.2f}")