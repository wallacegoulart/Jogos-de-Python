#Nivel de Dificuldade
import random 

def nivel_dificuldade():
    while True:
        modo = int(input("\nDigite o nivel (1)Facil (2)Medio (3)Dificil: ") )

        if modo == 1 or modo == 2 or modo == 3 :
            #definindo a rodada
            if modo == 1:
                numero_rodada = 10
                numero_secreto = random.randrange(1,21)
                
            elif modo == 2:
                 numero_rodada = 7
                 numero_secreto = random.randrange(1,51)

            else:
                numero_rodada = 5
                numero_secreto = random.randrange(1,101)
                
            break

        else:
            print("Modo Invalido")

    return(modo , numero_rodada , numero_secreto) 
