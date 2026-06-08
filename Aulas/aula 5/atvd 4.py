class Pessoa:
    def __init__(self, nome, idade):
        self.nome  = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print(f"Aluno: {self.nome} | Idade: {self.idade} | Matrícula: {self.matricula}")


class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def apresentar(self):
        print(f"Professor: {self.nome} | Idade: {self.idade} | Salário: R$ {self.salario:.2f}")


pessoas = [
    Aluno("Ana", 17, "2024001"),
    Professor("Carlos", 40, 4500.0),
    Aluno("Bruno", 16, "2024002"),
    Professor("Lúcia", 35, 5200.0),
]

for p in pessoas:
    p.apresentar()