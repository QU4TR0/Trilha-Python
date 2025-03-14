class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno1 = Estudante("Guilherme", 12456)
aluno2 = Estudante("Giovanna", 75358)

mostrar_valores(aluno1,aluno2)
print(aluno1)
print(aluno2)

Estudante.escola = "Python"

aluno1.matricula = 25879
aluno3 = Estudante("Mariana", 45689)
mostrar_valores(aluno1, aluno2, aluno3)