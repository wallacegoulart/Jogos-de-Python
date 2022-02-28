#jogo da forca
import random 

def jogo():
    
    print("**********************************")
    print("BEM VINDO A JOGO DA FORCA")
    print("**********************************")

    nivel = int(input("DIGITE O NIVEL (5)FACIL (7)MEDIO (9) DIFICIL : "))


    filename = 'C:/Users/Wallace/Desktop/Códigos - Programação/Python/Jogo/forca/palavra.txt'
    with open(filename,'r') as arquivo:
        palavra_arquivo = []
        for linha in arquivo:
            palavra_arquivo.append( linha.strip().lower() )

    numero_aleatorio = random.randrange(0,len(palavra_arquivo))


    palavra_secreta = palavra_arquivo[numero_aleatorio]
    letras_acertadas = ['_' for palavra in palavra_secreta]
    print()
    print(letras_acertadas) 

    erros = 0
    enforcou = False
    acertou = False
    qtd_chances = nivel

    while ( not enforcou and not acertou ):

        chute = input("Digite a letra: ")
        chute = chute.strip().lower()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index +=1    

        else:
            erros += 1
            qtd_chances -=1

        enforcou = ( erros == nivel  )
        acertou  = ( '_'  not in letras_acertadas )
        print("Falta {} chances".format(qtd_chances) )
        print(letras_acertadas)
        


    print("**********************************")
    print("FIM DE JOGO")
    print("**********************************")
    print("A PALAVRA SECRETA ERA : {}".format(palavra_secreta)) 



if (__name__ == '__main__'):
    jogo()

