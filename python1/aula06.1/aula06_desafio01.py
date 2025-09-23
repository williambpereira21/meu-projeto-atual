saldo = 0.0
meta = float(input("Digite o valor da meta de saldo a ser alcançada: "))

total_depositos = 0
total_saques = 0
soma_movimentacoes = 0.0

tentativa = 1

for i in range(1, 1000):          # Limite de até 1000 transações
    if saldo >= meta:
        break                     # Para o programa se a meta foi atingida

    print(f"\nTentativa {tentativa}")
    tentativa += 1

    print(f"Saldo atual: R${saldo:.2f}")
    operacao = input("Digite 'd' para depósito, 's' para saque ou 'q' para ignorar: ").lower()

    if operacao == 'd':
        valor = float(input("Valor do depósito: "))
        if valor <= 0:
            print("Valor inválido. O depósito deve ser maior que zero.")
            continue
        saldo += valor
        total_depositos += 1
        soma_movimentacoes += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    elif operacao == 's':
        valor = float(input("Valor do saque: "))
        if valor <= 0:
            print("Valor inválido. O saque deve ser maior que zero.")
            continue
        if valor > saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            saldo -= valor
            total_saques += 1
            soma_movimentacoes += valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    elif operacao == 'q':
        print("Operação ignorada. Continuando...")

    else:
        print("Operação inválida. Tente novamente.")

                                                      # Relatório final
total_movimentos = total_depositos + total_saques
media = soma_movimentacoes / total_movimentos if total_movimentos > 0 else 0

print("\n=== RELATÓRIO FINAL ===")
print(f"Saldo final: R${saldo:.2f}")
print(f"Total de depósitos: {total_depositos}")
print(f"Total de saques: {total_saques}")
print(f"Média dos valores movimentados: R${media:.2f}")
