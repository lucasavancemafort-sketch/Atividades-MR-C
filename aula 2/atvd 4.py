class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def extrato(self):
        print(f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")


conta = ContaBancaria("Ana Silva", 500.00)

conta.extrato()
conta.depositar(300.00)
conta.sacar(100.00)
conta.sacar(1000.00)
conta.extrato()