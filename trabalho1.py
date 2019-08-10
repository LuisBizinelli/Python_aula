#Exercicio Estruturas de dados

#Submeter os scripts Python para os dois exercícios a seguir:

#1. Implemente um programa em Python que leia 15 números informados pelo usuário. Utilizando uma estrutura de pilha, realize as seguintes tarefas:

#a) Se o número for impar, adicione na pilha.

#b) Se o número for par, remova um elemento da pilha caso a pilha não seja vazia.

#Ao final das 15 execuções, mostre a sequencia de operações realizadas e a pilha final.

print("insira os dados: \n")
pilha = []
while len(pilha) < 15:
   num = input("digite um numero: ")
   if num % 2 == 1:
        pilha.append(num)
   elif num % 2 == 0:
        pilha.pop()
print(pilha)        
    
#2. Escreva um programa em Python que simule o controle de uma pista de decolagem de aviões em um aeroporto.
#Neste programa, o usuário deve ser capaz de realizar as seguintes tarefas:

#a) Listar o número de aviões aguardando na fila de decolagem;

#b) Autorizar a decolagem do primeiro avião da fila;

#c) Adicionar um avião à fila de espera;

#d) Listar todos os aviões na fila de espera.

print("bem vindo ao aeroporto dois irmão!\n Escolha uma opção")
menu = 0
espera = []
while menu != 5:
    print ("1 - listar avião")
    print ("2 - autorizar decolagem")
    print ("3 - adicionar avião")
    print ("4 - listar fila")
    print ("5 - sair")
    menu = input()
    if menu == 1:
        print("esta é a quantidade: ")
        print(len(espera))
    elif menu == 2:
        print("boa viagem!!")
        espera.pop(0)        
    elif menu == 3:
        espera.append(input("adicionar avião: "))
    elif menu == 4:
        print("codigo dos avião: ")
        print(espera)        
    elif menu == 5:
        print ("até")
