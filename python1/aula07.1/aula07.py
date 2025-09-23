#funções

def apresentar ():
    print(f'meu nome é {myname}.')
    print(f'minha altura é de {myheigh} metros.')
    print(f'minha idade é {myage} anos.')
    return
def conferir(x):
    if x >=18:
        print('você é maior de idade')

    else:
        print('ops, menor de idade não pode!')
    return

myname=str(input('digite o seu nome:'))
myheigh=float(input('digite sua altura:'))
myage=int(input('digite sua idade: '))

apresentar()
conferir(myage)


#exemplo 2


def adiçao(x,y):
    w=x+y
    return w
def subtraçao(x,y):
    return x-y
print('digite dois valores inteiros...')
n1=int(input('x:'))
n2=int(input('y:'))
op=input('qual operação (+ ou-)?')

if op== '+':
    z=adiçao(n1,n2)
    print('resultado da soma:',z)

elif op=='-':
    z=subtração(n1,n2)
    print('resultado da subtração:',z)

else:
    print('opção digitada inexistente!')


#exemplo 3

def multiplicaçao(x,y):
    w=x*y
    return w
def divisão(x,y):
    return x/y
print('digite dois valores inteiros...')
n1=int(input('x:'))
n2=int(input('y:'))
op=input('qual operação (* ou /)?')

if op== '*':
    z=multiplicaçao(n1,n2)
    print('resultado da multiplicação:',z)

elif op=='/':
    z=divisão(n1,n2)
    print('resultado da divisão:',z)

else:
    print('opção digitada inexistente!')
