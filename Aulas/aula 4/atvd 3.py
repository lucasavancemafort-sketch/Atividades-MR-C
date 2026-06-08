class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo   = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Erro: valor do depósito deve ser positivo")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente")
        else:
            self.__saldo -= valor

    def get_saldo(self):
        return self.__saldo

    def extrato(self):
        print(f"Titular: {self.__titular}")
        print(f"Saldo:   R$ {self.__saldo:.2f}")

c = ContaBancaria("Ana")
c.depositar(500)
c.sacar(200)
c.depositar(-100)  
c.sacar(400)       
c.extrato()