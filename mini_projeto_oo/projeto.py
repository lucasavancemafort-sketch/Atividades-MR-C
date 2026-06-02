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