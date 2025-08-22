temperatura = input("Digite o valor da temperatura: ")


temperatura = float(temperatura)

print("Escolha a unidade de entrada:")
print("1 - Celsius")
print("2 - Kelvin")
print("3 - Fahrenheit")

opcao = input("Digite 1, 2 ou 3: ")

match opcao:
    case '1':  # Celsius
        print(f'Celsius para Kelvin: {temperatura + 273.15:.2f}')
        print(f'Celsius para Fahrenheit: {((temperatura * 9) / 5) + 32:.2f}')
    case '2':  # Kelvin
        print(f'Kelvin para Celsius: {temperatura - 273.15:.2f}')
        print(f'Kelvin para Fahrenheit: {((temperatura - 273.15) * 9) / 5 + 32:.2f}')
    case '3':  # Fahrenheit
        print(f'Fahrenheit para Celsius: {((temperatura - 32) * 5) / 9:.2f}')
        print(f'Fahrenheit para Kelvin: {(((temperatura - 32) * 5) / 9) + 273.15:.2f}')
    case _:  # Caso inválido
        print("Opção inválida!")
