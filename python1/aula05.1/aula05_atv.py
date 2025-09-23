#atv1
time=input('digite o nome do time:')
posição=input('digite a posição do time:')

if posição==1:
   classificação=('seu time é campeão')

elif posição >=1 and posição<=6:
    classificação=('seu time foi pra libertadores')

elif posição >=7 and posição<=12:
   classificação=('seu time foi pra sul americana')

elif posição >=13 and posição<=16:
   classificação=('seu time foi desclassificado')

else:
    classificação=('posição inválida')


print(f"time:{time}")
print(f"posição:{posição}")
print(f"classificação:{classificação}")





#atv2 
print('defina os valores a serem organizados:')
x=float(input('digite o primeiro número (x):'))
y=float(input('digite o segundo número(y):'))
z=float(input('digite o terceiro número(z):'))

if x>y>z:
   print('eles estão em ordem crescente.')

if z>y>x:
   print('eles estão em ordem decrescente.')

else:
   print('eles estão misturados!')



#atv3

primeiro_lado=float(input('digite o valor do primeiro lado:'))
segundo_lado=float(input('digite o valor do segundo lado:'))
terceiro_lado=float(input('digite o valor do terceiro lado:'))

if primeiro_lado==segundo_lado==terceiro_lado:
   print('seu tringulo é equilátero.')

elif primeiro_lado==segundo_lado !=terceiro_lado:
   print('seu triângulo é isósceles.')

else:
   print('seu triângulo é escaleno.')


#atv4

função=input('digite a função que gostaria de  exercer em um jogo de futebol:')

if  função=="zagueiro"or'goleiro'or'lateral':
   print('defesa!')

if  função=='ala'or'volante'or'meia':
   print('meio campo!')

if  função=='atacante' or 'centroavante':
   print('ataque!')

else:
   print('teimoso!')


#atv5

servico = input("O serviço foi prestado? (sim/não): ")

if servico == "sim":
    nota = input("Avalie o serviço com uma nota de 1 a 5: ")

    if nota == "1":
        print("Você avaliou como: Péssimo")
    elif nota == "2":
        print("Você avaliou como: Ruim")
    elif nota == "3":
        print("Você avaliou como: Razoável")
    elif nota == "4":
        print("Você avaliou como: Bom")
    elif nota == "5":
        print("Você avaliou como: Ótimo")
    else:
        print("Nota inválida. Por favor, digite um número de 1 a 5.")

elif servico == "não":
    print("Serviço não prestado. Nota atribuída: 0")
    reclamacao = input("Por favor, descreva sua reclamação: ")
    print("Sua reclamação foi registrada:", reclamacao)

else:
    print("Resposta inválida. Digite apenas 'sim' ou 'não'.")

#atv6
print("=== Jogo: Pedra, Papel ou Tesoura ===")
print("Opções válidas: pedra, papel, tesoura")

jogador1 = input("Jogador 1, escolha: ")
jogador2 = input("Jogador 2, escolha: ")

if jogador1 == jogador2:
    print("Empate!")

elif (jogador1 == "pedra" and jogador2 == "tesoura") or \
     (jogador1 == "papel" and jogador2 == "pedra") or \
     (jogador1 == "tesoura" and jogador2 == "papel"):
    print("Jogador 1 venceu!")

elif (jogador2 == "pedra" and jogador1 == "tesoura") or \
     (jogador2 == "papel" and jogador1 == "pedra") or \
     (jogador2 == "tesoura" and jogador1 == "papel"):
    print("Jogador 2 venceu!")

else:
    print("Opção inválida de um dos jogadores.")
    