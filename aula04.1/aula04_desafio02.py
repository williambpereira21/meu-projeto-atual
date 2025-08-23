# trabalho dos times
naturalidade = input(
    "Informe sua naturalidade (carioca, paulista ou mineiro): ")


if naturalidade == "carioca":
    print("Clubes disponíveis: Flamengo, Vasco, Fluminense, Botafogo")
    clube = input("Digite o nome do clube do seu coração: ")

    match clube:
        case "Flamengo":
            print("Você é um verdadeiro rubro-negro! Vai, Flamengo!")
        case "Vasco":
            print("Vasco sempre presente, orgulho cruzmaltino!")
        case "Fluminense":
            print("Tricolor das Laranjeiras, força sempre!")
        case "Botafogo":
            print("Botafogo de alma e coração!")
        case _:
            print("Clube não reconhecido, mas o importante é torcer com paixão!")

elif naturalidade == "paulista":
    print("Clubes disponíveis: Corinthians, Palmeiras, São Paulo, Santos")
    clube = input("Digite o nome do clube do seu coração: ")

    match clube:
        case "Corinthians":
            print("Vai, Timão! A Fiel torcida está contigo!")
        case "Palmeiras":
            print("Palmeiras, o alviverde imponente!")
        case "São Paulo":
            print("Tricolor Paulista, raça e tradição!")
        case "Santos":
            print("Santos, terra dos grandes craques!")
        case _:
            print("Clube não reconhecido, mas o importante é torcer com paixão!")

elif naturalidade == "mineiro":
    print("Clubes disponíveis: Atlético Mineiro, Cruzeiro, América Mineiro")
    clube = input("Digite o nome do clube do seu coração: ")

    match clube:
        case "Atlético Mineiro":
            print("Galo forte, raça e paixão mineira!")
        case "Cruzeiro":
            print("Cruzeiro estrela maior, orgulho de Minas!")
        case "América Mineiro":
            print("Coelho sempre em alta, força América!")
        case _:
            print("Clube não reconhecido, mas o importante é torcer com paixão!")

else:
    print("Naturalidade não reconhecida.")
