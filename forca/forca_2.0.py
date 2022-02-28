#Jogo da Forca 21.01.2022

#Imporatando as fuinções necessarias 
import nivel as nivel 
import palavras as palavras
import placar as placar

print("====================================================")
print("BEM VINDO AO JOGO DA FORCA")
print("====================================================\n")

#Mostrando o placar do jogo
placar.mostrar_placar()
print("====================================================\n")

#chamando a função de nivel de jogabilidade
nivel = nivel.nivel()


#pontuação
  pontuacao = 1000        

#chamando a função palavras e gerando a palavra aleatorio
palavra_escolhida = palavras.palavras()
palavras_acertadas = ['_' for x in palavra_escolhida]
print()
print("A palavra secreta ::")
print(palavras_acertadas) 


#os flags para saber quando acertou ou errou
erros = 0
acertou = False
enforcou = False
chances = nivel
letras_sairam = []

while(not acertou and not enforcou):
    chute = input("\nDigite a letra desejada: ")
    letra = chute.strip().lower()

    # If para saber se a letra esta ou nao na palavra
    if letra in palavra_escolhida:
        #Se a letra estiver na palavra vamos achar a posição para retirar o traço 
        index = 0
        for x in palavra_escolhida:
            if x == letra :
                palavras_acertadas[index] = x
            index += 1
    else:
        erros +=1
        chances -=1
        letras_sairam.append(chute)
    
    enforcou = (erros == nivel)
    acertou = ('_' not in palavras_acertadas)
    print(f'\n{palavras_acertadas}')
    print(f'Chances Restante {chances}')
    print(f'As letras que já sairam: {letras_sairam}')
    print("====================================================\n")


# Quando a pessoa ganhar
if acertou:
    print("\nVOCE GANHOU O JOGO PARABENS, ERROU {} VEZE(S)\n".format(erros))

# calculando a pontuação
if enforcou:
    pontuacao = 0
else:
    pontuacao = pontuacao - 100 * int(erros)
    print("\n====================================================")
    print(f"SUA PONTUACAO FINAL É {pontuacao}")

# Add no placar
placar.add_placar(pontuacao)

#Mostrando o placar novamente
print("\n====================================================")
print("PLACAR ATUALIZADO")
placar.mostrar_placar()

print("\n====================================================")
print("FIM DE JOGO A PALAVRA CORRETA ERA")
print(f'{palavra_escolhida}')


      
                      
