#exercício 1

def apresentar():
 print(f'minha idade é {idade}anos')
 print(f'os filmes que posso ver são:{filmes}')
 return
def conferir(idade):
 if idade>=18 :
    print(f'os programas disponíveis para você são:{filmes_maior}')
 elif idade<18 and idade>=1:
   print(f'os programas disponíveis para você são:{filmes_menor}')
 else:
  print(f'essa idade não pode!')
 return
filmes_maior='scarface,gente grande e halo'
filmes_menor='dino-trem,família dinossauro e arnold'
idade=int(input('digite sua idade :'))
apresentar()
conferir(idade)