print('responda as perguntas sobre a sua aposentadoria:')
genero=int(input('digite qual o seu gênero: (1-masculino)(2-feminino)'))
match genero:
    case 1:
        print(' você escolheu o genero masculino!')
    case 2:
        print('você escolheu o genero feminino!')
    case _:
        print('genero inválido!')


idade= int(input('digite sua idade:'))

tempo_contribuição=int(input('digite  o seu tempo de contribuição :'))

exposição=input('você teve alguma exposição a insalubridade?         (sim-1)(não-2)')

match  exposição:
    case 1:
        print('sinto muito que tenha sido exposto!')       
    case 2:
        print('que bom que isso não aconteceu!')
    case _:
        print('apenas digite sim ou não.') 

if genero==1 and idade>=65 and tempo_contribuição>= 15:
    print(' você pode se aposentar!')

elif genero==2 and idade>=62 and tempo_contribuição>= 15:
    print(' você pode se aposentar!') 

elif   genero==1 and idade<65 and tempo_contribuição< 15:
    print(' você não pode se aposentar!')   

elif   genero==2 and idade<62 and tempo_contribuição< 15:
    print(' você não pode se aposentar!') 

else :
    print('Você ainda não pode se aposentar com as regras atuais.') 