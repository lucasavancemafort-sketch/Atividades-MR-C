class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo   = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor

    def extrato(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo:   R$ {self.saldo:.2f}")

conta = ContaBancaria("Maria", 500.0)
conta.depositar(200)
conta.sacar(100)
conta.sacar(800)   
conta.extrato()