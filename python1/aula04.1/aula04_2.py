# demonstração do uso de condicional match/case....
print('Digite o número referente ao estado da moeda:')
print('1. flor de cunho')
print('2. soberba')
print('3. muito bem conservada')
print('4. outros estados')
estado = int(input())

match estado:
    case 1:
        print('Perfeita! Vou pagar 1.000.000,00!')
    case 2:
        print('Quase perfeita! Vou pagar 250.000,00!')
    case 3:
        print('Que ótimo! Vou pagar 30.000,00!')
    case 4:
        print('Desculpe, não posso aceitar nesse estado')
    case 5:
        print('Desculpe, não posso aceitar nesse estado')
    case _:
        print('Desculpe, opção não reconhecida')
