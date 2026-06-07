class Funcionario:
    def __init__(self, nome, matricula, salario_base):
        self._nome = nome
        self._matricula = matricula
        self.salario_base = salario_base
 
    @property
    def nome(self):
        return self._nome
 
    @property
    def matricula(self):
        return self._matricula
 
    @property
    def salario_base(self):
        return self._salario_base
 
    @salario_base.setter
    def salario_base(self, valor):
        if valor < 0:
            raise ValueError("O salário não pode ser negativo!")
        self._salario_base = valor
 
 
class CLT(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)
 
    def calcular_salario(self):
        return self.salario_base
 
    def exibir(self):
        print(f"Nome : {self.nome} | Matricula : {self.matricula} | Tipo : CLT | Salario : R$ {self.calcular_salario():.2f}")
 
 
class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_base, total_vendas):
        super().__init__(nome, matricula, salario_base)
        self._total_vendas = total_vendas
 
    def calcular_salario(self):
        comissao = self._total_vendas * 0.10
        return self.salario_base + comissao
 
    def exibir(self):
        print(f"Nome : {self.nome} | Matricula : {self.matricula} | Tipo : Vendedor | Salario : R$ {self.calcular_salario():.2f}")
 
 
class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)
        self._bonus = 1500.00
 
    def calcular_salario(self):
        return self.salario_base + self._bonus
 
    def exibir(self):
        print(f"Nome : {self.nome} | Matricula : {self.matricula} | Tipo : Gerente | Salario : R$ {self.calcular_salario():.2f}")
 
 
funcionarios = [
    CLT("Lucas", "001", 3000.00),
    Vendedor("Apyr do gus", "002", 2000.00, 12000.00),
    Gerente("Ana", "003", 5000.00),
]
 
for f in funcionarios:
    f.exibir()