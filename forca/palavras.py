# buscando as palavras 
import random

def palavras():
    #buscando o txt com as palavras 
    with open('palavra.txt','r') as arquivo:
        palavras = []
        for palavra in arquivo:
            palavras.append(palavra.strip().lower())

    #gerando a palavra escolhida de forma aleatoria
    numero_aleatorio = random.randrange(0,len(palavras))
    palavra_escolhida = palavras[numero_aleatorio]
    return palavra_escolhida
    
