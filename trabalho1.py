#Exercicio Estruturas de dados

#Submeter os scripts Python para os dois exerc�cios a seguir:

#1. Implemente um programa em Python que leia 15 n�meros informados pelo usu�rio. Utilizando uma estrutura de pilha, realize as seguintes tarefas:

#a) Se o n�mero for impar, adicione na pilha.

#b) Se o n�mero for par, remova um elemento da pilha caso a pilha n�o seja vazia.

#Ao final das 15 execu��es, mostre a sequencia de opera��es realizadas e a pilha final.

print("insira os dados: \n")
pilha = []
while len(pilha) < 15:
   num = input("digite um numero: ")
   if num % 2 == 1:
        pilha.append(num)
   elif num % 2 == 0:
        pilha.pop()
print(pilha)        
    
#2. Escreva um programa em Python que simule o controle de uma pista de decolagem de avi�es em um aeroporto.
#Neste programa, o usu�rio deve ser capaz de realizar as seguintes tarefas:

#a) Listar o n�mero de avi�es aguardando na fila de decolagem;

#b) Autorizar a decolagem do primeiro avi�o da fila;

#c) Adicionar um avi�o � fila de espera;

#d) Listar todos os avi�es na fila de espera.

print("bem vindo ao aeroporto dois irm�o!\n Escolha uma op��o")
menu = 0
espera = []
while menu != 5:
    print ("1 - listar avi�o")
    print ("2 - autorizar decolagem")
    print ("3 - adicionar avi�o")
    print ("4 - listar fila")
    print ("5 - sair")
    menu = input()
    if menu == 1:
        print("esta � a quantidade: ")
        print(len(espera))
    elif menu == 2:
        print("boa viagem!!")
        espera.pop(0)        
    elif menu == 3:
        espera.append(input("adicionar avi�o: "))
    elif menu == 4:
        print("codigo dos avi�o: ")
        print(espera)        
    elif menu == 5:
        print ("at�")
