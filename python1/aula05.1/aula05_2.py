print('o que voce vai fazer amanha de manha?')
print('dormir/estudar/planejar')
manha=input()
print('o que voce vai fazer amanha de tarde?')
print('jogar/treinar/trabalhar')
tarde=input()

if not manha or not tarde:
    print('voce precisa dizer o que vai fazer')
else:
    if manha=='dormir' or tarde=='jogar':
     print('voce esta desperdiçando o seu dia')
    elif manha=='estudar' or tarde=="treinar":
     print(' voce irá se aperfeiçoar!') 
    elif manha=='planejar' and tarde=='trabalhar':
       print('para trabalhar melhor,devo planejar')
    else:
       print('não combinamos estas açoes...')
print('tenha um bom dia')