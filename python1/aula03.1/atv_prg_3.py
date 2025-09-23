#PRIMEIRO PROGRAMA

num_1=float(input('qual o primeiro número?'))
num_2=float(input('qual o segundo número?'))

soma=num_1 + 5
subtração= num_2 - 3

print('resultado da soma do primeiro número por 5 é igual a:',soma)
print('resultado da subtração do segundo número por 3 é igual a:',subtração)

#SEGUNDO PROGRAMA
valor_produto = float(input("Digite o valor do produto: R$ "))
qtd_prestacoes = int(input("Digite a quantidade de prestações: "))


valor_prestacao = valor_produto / qtd_prestacoes

print("O valor de cada prestação será: R$", round(valor_prestacao, 2))


#TERCEIRO PROGRAMA
numero = float(input("Digite um número: "))

quadrado = numero ** 2
cubo = numero ** 3

print("Quadrado do número:", quadrado)
print("Cubo do número:", cubo)


#QUARTO PROGRAMA
ano_nascimento = int(input("Digite o ano em que você nasceu: "))

idade_em_2040 = 2040 - ano_nascimento

print("Em 2040, você terá", idade_em_2040, "anos.")


#QUINTO PROGRAMA
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

resultado = (valor1 * valor2) / valor3

print("Resultado da operação (valor1 * valor2) / valor3:", resultado)