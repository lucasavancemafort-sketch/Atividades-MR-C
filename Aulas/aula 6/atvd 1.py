class Funcionario:
    def calcular_salario(self):
        return 0

class Vendedor(Funcionario):
    def __init__(self, salario_fixo, comissao):
        self.salario_fixo = salario_fixo
        self.comissao = comissao

    def calcular_salario(self):
        return self.salario_fixo + self.comissao

class Gerente(Funcionario):
    def __init__(self, salario_fixo, bonus):
        self.salario_fixo = salario_fixo
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_fixo + self.bonus

vendedor = Vendedor(salario_fixo=2000, comissao=500)
gerente = Gerente(salario_fixo=5000, bonus=1500)

print(f"Salário do Vendedor: R$ {vendedor.calcular_salario():.2f}")
print(f"Salário do Gerente: R$ {gerente.calcular_salario():.2f}")