#Placar

#Mostrar o placar do jogo
def mostrar_placar():
    print("====================================================")
    print("PLACAR DO JOGO")
    with open('placar.txt','r') as arquivo:

        #chamando a função de ordenar o placar
        lista = arquivo.readlines()
        lista_ordenada = ordena_placar(lista)
        
        #mostrando na tela
        index = 1
        for line in lista_ordenada:
            print(str(index) + ' - ' + line.strip() + ' pontos')
            index +=1


#Adicionando nova pontuação
def add_placar(pontuacao):
    with open('placar.txt' ,'a') as arquivo:
        nome = input("Digite seu nome : ")
        placar = (nome + " : " + str(pontuacao) )
        arquivo.write('\n'+ placar)
    

#Ordenando o Placar

def ordena_placar(lista):

    #Pegando somente a pontuação e colocando numa lista
    #A variavel 'num' sai como uma lista somente com um numero
    numeros = []
    for value in lista:
        num = [int(n) for n in value.split() if n.isdigit()]
        numeros.append(num)
       
        
    #Ordenando o placar com atraves da lista de numeros
    #faço dois 'for' pq num numeros tem uma lista de varias lista com somente um numero    
    numeros.sort(reverse=True)
    lista_ordenada = []
    
    for num in numeros:
        for num1 in num:
            for value in lista:
                if str(num1) in value:
                    lista_ordenada.append(value)
                    lista.remove(value)
            
             
    return lista_ordenada



if(__name__ == '__main__'):
    mostrar_placar()
