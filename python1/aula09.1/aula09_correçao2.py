numeros=[]
jogadores=[]
for x in range(0,11):
    numero=input('digite a camisa:')
    numeros.append(numero)
    jogador=input('digite o nome do jogador:')
    jogadores.append(jogador)
print(numeros,jogadores)


saida=input('digite o numero da saida:')
numero1=input('digite o nome da entrada:')
jogador1=input('digite o nome do jogador:')

for x in range(0,11):
    if numeros(x)==saida:
        numeros(x)=numero
        jogadores(x)=jogador


print(numeros,jogadores)