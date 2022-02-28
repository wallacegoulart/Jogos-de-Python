# Jogo de Avinhação
import adivinhacao.placar             as placar
import adivinhacao.nivel_dificuldade  as nivel

def jogo():
    
    print('###############################################')
    print("BEM VINDO AO JOGO DE ADIVINHACAO")
    print('###############################################\n')

    #Mostrar o placar
    placar.mostrar_placar()

    #Nivel de dificuldade
    modo , numero_rodada , numero_secreto = nivel.nivel_dificuldade()


    #Nivel de pontuação
    pontuacao = 1000
            
    #Lista de numero que ja foram jogados
    numeros_sairam = []


    #Entrada no jogo
    print('\n###############################################')
    print("              COMEÇANDO O JOGO")
    print('###############################################\n')
    print("Você tem {} chances para acertar".format(numero_rodada))

    for rodada in range(1,numero_rodada+1) :
        print("\nRodada de numero {} e sua pontuação é {} ".format(rodada , pontuacao))
        chute = int(input("\nDigite seu chute: "))
        numeros_sairam.append(chute)

        #Verificação do chute
        igual = (chute == numero_secreto)
        maior = (chute > numero_secreto)
        menor = (chute < numero_secreto)

        if igual:
            print("ACERTOUUUUU!!!!!!!!!!")
            break

        elif maior:
            pontuacao -= 100
            if abs(chute - numero_secreto) < 5 :
                print("Você está muito perto")
                print("O numero continua alto")
            else:
                print("Você está longe")
                print("O numero continua alto")
                
        elif menor:
            pontuacao -= 100
            if abs(chute - numero_secreto) < 5 :
                print("Você está muito perto")
                print("O numero continua baixo")
            else:
                print("Você está longe")
                print("O numero continua baixo")

                
        print("\nNumeros que já sairam " + str(numeros_sairam) )
        
    print('\n###############################################')
    print("FIM DE JOGO")
    print('\n###############################################')
    print("Sua pontuação final foi {} ".format(pontuacao))
    print('###############################################\n')


    #Add no placar somente se digitar 1
    print('\n###############################################')
    print("Você deseja entrar no placar")
    pla = int(input("Digite (1) para entrar no placar: "))
    if pla == 1:
        placar.add_placar(pontuacao)
    print('\n###############################################\n')


    #Mostrar o placar
    print("PLACAR ATUALIZADO:")
    placar.mostrar_placar()

    
