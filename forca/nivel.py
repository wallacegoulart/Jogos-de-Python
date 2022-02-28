# nivel de dificuldade

def nivel():

# nivel do jogo para definir a quantidade para jogar , fica em lopp ate ter o numero correto das opcoes
    while True:
        nivel = int(input("Digite o nivel da dificuldade (9)Facil (7)Medio (5)Dificil: " ))
        if nivel == 7 or nivel == 5 or nivel == 9:
            break
    return nivel
