print('Digite sua idade:')
idade = int(input())

if idade < 18:
    print('Você não é maior de idade!')
    print('Não poderá realizar operações bancárias!')
    print('Obrigado por escolher os nossos serviços!')

elif idade >= 65:
    print('Você está aposentado')
    print('Poderemos oferecer suporte técnico...')

else:
    print('Você é maior de idade.')
    print('Portanto, pode realizar transações bancárias.')
    print('Obrigado por escolher os nossos serviços!')

