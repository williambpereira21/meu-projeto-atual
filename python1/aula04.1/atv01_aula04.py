# atividade 1
saldo = float(input("Informe o saldo da sua conta bancária: R$ "))
valor_produto = float(input("Informe o valor do produto que deseja comprar: R$ "))

if saldo >= valor_produto:
    saldo_final = saldo - valor_produto
    print(f"Compra realizada com sucesso! Seu saldo restante é R$ {saldo_final:.2f}")
else:
    print("Saldo insuficiente para realizar a compra.")



#atividade 2
nota1 = float(input("Digite a nota do 1º trimestre: "))
nota2 = float(input("Digite a nota do 2º trimestre: "))
nota3 = float(input("Digite a nota do 3º trimestre: "))
nota4 = float(input("Digite a nota do 4º trimestre: "))

media = (nota1 + nota2 + nota3 + nota4) / 4


if media >= 6:
    print(f"Aluno aprovado com média {media:.2f}")
else:
    print(f"Aluno reprovado com média {media:.2f}")



# atividade 3
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))


imc = peso / (altura ** 2)

if imc > 25:
    print(f"IMC: {imc:.2f} - Acima do peso ideal")
elif imc < 18:
    print(f"IMC: {imc:.2f} - Abaixo do peso ideal")
else:
    print(f"IMC: {imc:.2f} - O seu peso está OK")