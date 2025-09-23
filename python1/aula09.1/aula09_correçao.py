#1
gabarito=['b','c','a','e','d']
aluno=[]
acertos=0

for c in range(5):
   resposta=(f'digite as sua respostas da prova da questão {c+1}:')
   aluno.append (resposta)                #adicionei resposta na lista 

   if resposta == gabarito[c]:            #compara a resposta atual com a questão correspondente do gabarito
    acertos+=1


print(f'você acertou{acertos}questões!')


#2
jogadores=[]

for c in range(11):
 nome=input('digite seu nome:')
 numero=input('digite seu número de camisa:')
jogadores.append(nome,numero)


print ('escalação inicial')
for numero,nome in jogadores:
  print(f'{nome} - camisa{numero}')


for c in range(3):
  if input(f'substituição {c+1} (s/n)?')=='s':
   substituido=input('digite o jogador que vai ser substituído pelo número da camisa:')
   for cc in range (len(jogadores)):
     if jogadores[cc] [1] ==substituido:
       novojogador=input('digite o nome do novo jogador:')
       novonumero=input('digite o novo número da camisa do jogador:')
       jogadores[cc]=[novonumero,novojogador]
       break


print(F'escalação atualizada:')

for nome, numero in jogadores:
    print(f"{nome} - Camisa {numero}")


#3
print('criação da lista digite os afazeres abaixo a serem executados:')
lista_de_afazeres=[]

for c in range(5):
  tarefas=input(f'tarefa {c+1}:')
  lista_de_afazeres.append(tarefas)

  print('lista de afazeres!')
c=1
for tarefas in lista_de_afazeres:
  print(f'{c}.{tarefas}')
  c+=1

resposta=input('a primeira tarefa foi concluída?(s/n)')
if resposta=='s':
  lista_de_afazeres.pop(0)
  nova=input('deseja adicionar uma nova tarefa?(s/n)')
  if nova =='s':
    nova_tarefa = input("Digite a nova tarefa: ")
    lista_de_afazeres.append(nova_tarefa)

print("\nLista atualizada:")
c = 1
for tarefas in lista_de_afazeres:
    print(f"{c}. {tarefas}")
    c += 1