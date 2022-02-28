def jogo():
    # Jogo da Adivinhação
    import random

    #chamada inicial do jogo 
    print('*****************************************')
    print('BEM VINDO AO JOGA DE ADIVINHAÇÃO')
    print('*****************************************')

    print()

    # digitando o modo de jogo
    while True:

        modo = int(input('Digite (1)facil, (2)intermediario , (3)dificil: '))
        
        if (modo == 1 or modo == 2 or modo == 3):
            break


    #ajutando o modo de jogo
    if (modo == 1):
        numero_rodada = 10
        numero_secreto = random.randrange(1,21)

    elif (modo == 2):
        numero_rodada = 7
        numero_secreto = random.randrange(1,41)
        
    else :
        numero_rodada = 5
        numero_secreto = random.randrange(1,71)

    print()
    print('*****************************************')
    print("Voce tem {} chances para acertar o numero".format(numero_rodada))
    print('*****************************************')

    #criando uma lista para guardar o os numeros que já foram chutados
    lista_numeros = []

    #entrada no jogo principal
    for rodada in range(1,numero_rodada+1):
        
        print("{} chance(s)".format(rodada))
        chute = int(input("Digite o numero: "))
        lista_numeros.append(chute)

        igual = ( chute == numero_secreto )
        maior = ( chute > numero_secreto  )
        menor = ( chute < numero_secreto  )

        #verificando o chute
        if igual:
            print(f'PARABENS VC ACERTOU NA {rodada} CHANCE(S)!!!!!!')
            print("BEM NA MOSCA!!!!!!!!!")
            break
            

        elif maior:    
            if ( abs(chute - numero_secreto) < 5 ):
                print("Voce esta muito perto do numero!!!")
                print("Mas o valor continua alto!!!")
            else:
                print("Você está longe ainda")
                print("Mas o valor continua alto!!!")
        
        elif menor:
             if ( abs(chute - numero_secreto) < 5 ):
                print("Voce esta muito perto do numero!!!")
                print("Mas o valor continua baixo!!!")
             else:
                 print("Você está longe ainda")
                 print("Mas o valor continua baixo!!!")


        #motrando a lista de numenro que já sairam
        print("Numero que você já tentou " + str(lista_numeros) )
        print()
                 
        
        
    print('*****************************************')
    print('FIM DE JOGO')
    print(f'O numero secreto era {numero_secreto}')
    print('*****************************************')


# modo para que funcione o jogo sem ser chamado pela função
if (__name__ == '__main__'):
    jogo()
