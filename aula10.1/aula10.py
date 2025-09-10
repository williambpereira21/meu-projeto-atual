tabuada=[]

for x in range(1,10):
    linhas=[]
    for y in range(1,10):
        linhas.append(x*y)
        tabuada.append(linhas)

for tabela in tabuada:
    print(tabela)




print('eis,o teclado númerico do teminal:')
teclado=[[1,2,3],[4,5,6][7,8,9]]

senha=[]

print('digite a sua senha de 4 digitos...')
for x in range(0,4):
    senha.append(int(input(f'digite o dígito {x+1}:')))

for x in range(0,3):
    for y in range(0,3):
        for z in range(0,4):
            if teclado(x)(y)==senha(z):
                teclado(x)(y)=0

print('eis,a senha digitada',senha)
print('confira,as teclas acionadas:')
for listas in teclado:
    print(listas)







print('eis, a tabela numérica original')
tabuada=[[1,2,3],[4,5,6],[7,8,9]]
multiplicar=int(input('digite o multiplicador:'))
for x in  range(0,3):
    for y in range(0,3):
        tabuada[x][y]=tabuada*multiplicar

print('eis,o multiplicador: ',multiplicar)
print('confira o resultado das operações')
for resultado in tabuada:
    print(resultado)