lista = []
lista_inteiros=[1,2,3,4,5]
lista_caracteres=['maçã','banana','cereja']
lista_mista = [1,'olá',3.14,True]

tupla_semana=('segunda','terça','quarta')
tupla_fibonacci=(1,2,3,5,8,13,21)

print(lista_inteiros)
print(lista_caracteres[0])         #maçã
print(lista_mista[1])              #olá
print(tupla_semana[2])             #terça
print(tupla_fibonacci)




print('vou montar a marmita com 5 alimentos')
marmita=['feijão','arroz','legumes','salada','carne']
print('eis, a nossa recomendação:',marmita)

resposta=input('quer montar uma marmita diferente (s/n)?')
if resposta=='s':
    for x in range(len(marmita)):                                  #len contabiliza em marmita onde vai ser contado de 0,1,2,3,4

        print(f'digite o {x+1} o item do cardápio:')               #x+1 é pra contar apartir de 1,2,3,4,5 em vez de 0,1,2,3,4
        marmita[x]=input()
    print('a marmita montada foi:',marmita)
    print('o três primeiros itens foram ',marmita[0:3])
    print('o último item da marmita foi:',marmita[-1])

else:
    print('ok. você decide...')



#exemplos
print(marmita[:])
print(marmita[2:3])
print(marmita[0:4:2])
print(marmita[-3:-1])





print('eis, os meus maiores sonhos...')
sonhos=['1. me divertir na disney','2.me banhar na praia de sepetiba','3.tirar férias em paris','4.fazer compras no west shopping','5.ver as pirâmides do egito']
for x in sonhos:
    print(x)

print('ops , não quero sepetiba!')                                #quando tira sepetiba muda a ordem
del(sonhos[1])
print('e nem west shopping!')                                     #agora west shopping é 2
del(sonhos[3])

print('conferindo os sonhos...')
for x in sonhos:
    print(x)

numeros=[7,2,9,6,5,0,3,8,1,4]
palavras=['olá','alô','hei','uau','ops']

print('quantas variáveis possui:')
print('números:',len(numeros))
print('palavras:',len (palavras))

print('vamos reordenar estas listas?')
print(sorted(numeros))                                           #sorted reordena pondendo ser em ordem alfabética
print(sorted(palavras))

print('o somatório de número:',sum (numeros))
print('qual é o maior valor?',max (numeros))
print('qual é a primeira palavra?',min(palavras))