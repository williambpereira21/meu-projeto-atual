print('o que voce va ifazer amanhã de manhã?')
print('dormir/estudar/planejar')
manhã=input()

print('o que voce va ifazer amanhã de tarde?')
print('jogar/treinar/trabalhar')
tarde=input()

if manhã=="dormir":
    print('você está desperdiçando o seu dia!')
    
if tarde=="jogar":
    print('você está desperdiçando o seu dia!')

if manhã=="estudar":
    print('que bom voce ira se aperfeiçoar')

if tarde=="treinar":
    print('que bom voce ira se aperfeiçoar')

if manhã=="planejar":
    if tarde=="trabalhar":
        print('para trabalhar melhor,devo planejar!')

    print('tenha um bom dia')
