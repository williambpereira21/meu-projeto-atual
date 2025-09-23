# primeiro exercício

escolha_de_filmes = int(input('escolha os filmes de 1 a 5:'))


match escolha_de_filmes:
    case 1: print('ta dando onda')
    case 2: print('circulo de fogo')
    case 3: print('o exorcista')
    case 4: print('demon slayer')
    case 5: print('gente grande')

nota_do_filme = int(input('digite a nota do filme de 1 a 5:'))


match nota_do_filme:
    case 1: print('horrível')
    case 2: print('ruim')
    case 3: print('razoável')
    case 4: print('bom')
    case 5: print('ótimo')
    case _:
        print('você escreveu errado, por favor verifique e tente novamente.')

if nota_do_filme == 1 or nota_do_filme == 2:
    print('sua nota foi ruim, digite a seguir o por que.')
    input(f"por que você deu essa nota {2} ?")


# segundo exercício
dia = int(input('digite o dia da semana desejado de 1 a 7:'))

match dia:
    case  1:
        print('segunda')
    case  2:
        print('terça')
    case 3:
        print('quarta')
    case 4:
        print('quinta')
    case 5:
        print('sexta')
    case 6:
        print('sábado')
    case 7:
        print('domingo')
    case _:
        print('você digitou algo errado!')

if dia == 1:
    print('seria bom trabalhar!')

elif dia == 2:
    print('ir pro curso seria uma boa ideia!')

elif dia == 3:
    print('seria divertido ir na praia!')

elif dia == 4:
    print('ir para a escola seria incrível!')

elif dia == 5:
    print('jogar videogame pode ser uma boa pedida!')

elif dia == 6:
    print('ir pro cinema no fim de semana é ótimo!')

elif dia == 7:
    print('ir para igreja pode ser bom!')
