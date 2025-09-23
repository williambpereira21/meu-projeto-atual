empresa = str(input('nome da empresa:'))
gestor = str(input('nome do gestor:'))
cargo = str(input('cargo:'))
inicio = input('data de início do aviso prévio:')
termino = input('data do término do aviso prévio:')
local = str(input('local:'))
data = input('data:')
nome_completo = str(input('nome:'))
# \n cria uma linha em branco para separar
print("\n\n--- Sua Carta de Demissão Gerada ---")
print("----------------------------------------")

carta_formatada = f"""

À {empresa}

Prezado(a) {gestor},

Venho por meio desta carta comunicar formalmente meu pedido de demissão do cargo de {cargo}.

Estarei à disposição da empresa durante o aviso prévio, no período de {inicio} a {termino}.

{local}, {data}

_________________________
(assinatura)

{nome_completo}
"""
print(carta_formatada)
print('-------------------------------------')
print('Cópia gerada com sucesso! Use como referência para escrever a carta de próprio punho.')
