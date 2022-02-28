#placar


def mostrar_placar():
    filename = 'C:/Users/Wallace/Desktop/Códigos - Programação/Python/Jogo/adivinhacao/placar.txt'

    with open(filename,'r') as file_obj:
        lista = file_obj.readlines()

        #chamando a função para ordenar o placar
        lines = ordena_placar(lista)

        #mostrando na tela
        index = 1
        for line in lines:
            print(str(index) + ' - ' + line.strip() + ' pontos')
            index +=1




def add_placar(pontuacao):
    filename = 'C:/Users/Wallace/Desktop/Códigos - Programação/Python/Jogo/adivinhacao/placar.txt'

    with open(filename,'a') as file_obj:
        nome = input("Digite seu nome: ")
        placar = (nome + " : " + str(pontuacao))
        file_obj.write('\n'+ placar )



#------------------
# função interna
#------------------
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
