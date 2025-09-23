# 1 atv
respostas_do_aluno = []
gabarito = ['b', 'c', 'a', 'e', 'd']
acertos = 0


for c in range(5):
    respostas_do_aluno = input(f'digite a resposta para a questão{c+1}:')
    # .append adiciona uma váriavel no final da lista no caso a respota do aluno
    respostas_do_aluno.append(respostas_do_aluno)


for c in range(5):
    if respostas_do_aluno[c] == gabarito[c]:
        acertos += 1


# 2 atv
jogadores = []

for i in range(11):
    nome = input(f"Nome do jogador {i+1}: ")
    numero = input("Número da camisa: ")
    jogadores.append([nome, numero])


print("\nEscalação inicial:")
for nome, numero in jogadores:
    print(f"{nome} - Camisa {numero}")


for i in range(3):
    if input(f"\nSubstituição {i+1}? (s/n): ").lower() == 's':
        num_out = input("Número da camisa que sai: ")
        for j in range(len(jogadores)):
            if jogadores[j][1] == num_out:
                novo_nome = input("Nome do novo jogador: ")
                novo_num = input("Número da camisa do novo jogador: ")
                jogadores[j] = [novo_nome, novo_num]
                break


print("\nEscalação atualizada:")
for nome, numero in jogadores:
    print(f"{nome} - Camisa {numero}")

# 3 atv
afazeres = []


for i in range(5):
    tarefa = input(f"Tarefa {i+1}: ")
    afazeres.append(tarefa)


print("\nLista de afazeres:")
i = 1
for tarefa in afazeres:
    print(f"{i}. {tarefa}")
    i += 1


resposta = input("\nA primeira tarefa foi concluída? (s/n): ").lower()
if resposta == 's':
    afazeres.pop(0)
    nova = input("Deseja adicionar uma nova tarefa? (s/n): ").lower()
    if nova == 's':
        nova_tarefa = input("Digite a nova tarefa: ")
        afazeres.append(nova_tarefa)


print("\nLista atualizada:")
i = 1
for tarefa in afazeres:
    print(f"{i}. {tarefa}")
    i += 1
