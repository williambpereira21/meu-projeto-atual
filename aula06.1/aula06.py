print('digite o valor máximo desejado:')
numero=int(input())

print('segue,os números desejados:')
for x in range (1,numero+1):
    print(x)



print('digite o nome desejado:')
nome=input()
print('vamos soletrar cada letra?')
for x in nome:
    print(x)
#for /in / range


print('digite o valor máximo desejado:')
numero=int(input())
x=0
print('segue,os números desejados:')
while x <=numero:
    print(x)
    x=x+1
                                      #Se a senha digitada for igual a 's3nh4':Imprime Senha correta E o break faz o laço parar imediatamente (sai do while)
                                                            
                                                            #while enquanto

   
   
    contador=0;senha=''                                      #variável;variável é pra separar sem afetar

    while senha!='s3nh4':
        print('senha correta')
        break
    else:
        print('senha errada')

    contador+=1                                    #contador+=1 é igual  a  contador=contador+1
    if contador==3:
        print('3 tentativas excedidas!')
        break         
                                                           #break quebra o laço 
 

numero=1
while numero >=0:
    print('digite um número negativo para sair:')
    numero=int(input())
    break    
    print('este texto não será exibido!mas.....')           
else:
    print('o número digitado foi',numero)                        #continue 