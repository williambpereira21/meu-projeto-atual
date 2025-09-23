nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'Sua média foi: {media:.2f}')


if media < 5:
    print('Você está reprovado!')


elif 5 <= media <= 6.5:            #lembrar da pra construir dentro do elif
    print('Você está de recuperação.')
    recuperacao = float(input('Digite sua nota de recuperação: '))

    media_final = (media + recuperacao) / 2

    if media_final >= 6.5:
        print('Você foi aprovado na recuperação!')
    else:
        print('Você foi reprovado na recuperação!')


elif media > 6.5:
    print('Você foi aprovado!')


