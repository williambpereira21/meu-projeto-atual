
#1 atv


class pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def verificar(self):
        if self.idade >= 18:
            print('você é maior de idade!')

        else:
            print("você não é maior de idade!")


pessoas2 = []


for c in range(5):
    pes1 = input('digite os nomes:')
    idade1 = int(input('digite as idades:'))
    altura1 = float(input('digite as alturas em cm:'))

    pessoa_objt = Pessoa(pes1, idade1, altura1)
    pessoas2.append(pessoa_objt)


for p in pessoas2:
    p.verificar()






#2 atv



class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


class Professor(Funcionario):
    def __init__(self, nome, salario, disciplina):
        super().__init__(nome, salario)
        self.disciplina = disciplina

# --- Cadastro ---


funcionarios = []

#  cadastrar 5 funcionários, sendo 2 professores



funcionarios.append(Professor("Ana", 2500.00, "Matemática"))
funcionarios.append(Professor("Carlos", 1900.00, "História"))
funcionarios.append(Funcionario("Beatriz", 2200.00))
funcionarios.append(Funcionario("Diego", 1800.00))
funcionarios.append(Funcionario("Fernanda", 3000.00))

# --- Tarefas ---

print("Funcionários que ganham acima de R$ 2.000,00:")
for f in funcionarios:
    if f.salario > 2000:
        print(f"- {f.nome}")

print("\nProfessores que lecionam Matemática:")
for f in funcionarios:
    # Verifica se é professor e se disciplina é Matemática
    if isinstance(f, Professor) and f.disciplina.lower() == "matemática":
        print(f"- {f.nome}")

print("\nNome e salário de todos os funcionários:")
for f in funcionarios:
    print(f"- {f.nome}: R$ {f.salario:.2f}")
