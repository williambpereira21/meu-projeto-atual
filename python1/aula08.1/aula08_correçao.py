
#2
#apresentação
import random

 
def apresentar():
  print('--jogo de par ou ímpar--')
  print('digite números inteiros!')

  jogador1=int(input('digite um número de 1 a 10 aleatório:'))
  máquina= random.randint(0, 11)
  
  soma=jogador1+máquina
  if verificar(soma):
   print('deu par')
  else:
    print('deu ímpar')

# parte verificadora

def  verificar(numero):
  return numero %2==0


#3
def apresentar():                                                                              #return entrega resultado
  print('digite seu nome abaixo:')
  nome=input()
  print('agora digite sua cidade:')
  cidade=input()
  if cidade=='rio de janeiro':
     print(f'{nome},bem vindo a cidade maravilhosa')
  else:
     print(f'{nome},sua cidade é {cidade}')
  



