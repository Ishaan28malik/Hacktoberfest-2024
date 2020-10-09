'''Universidade Federal de Pernambuco - UFPE
Centro de Informática
Bacharelado em Sistemas de Informação
IF968 - Programação 01
Autor: Alisson Diego Diniz D. da Fonseca (adddf)
E-mail: adddf@cin.ufpe.br
Data: 09/11/18
Descrição: O programa recebe um número n e calcula o n-ésimo número da sequência de Fibonacci'''

def fib(x,dicionario):
    if not str(x).isnumeric() or int(x) < 0:
        return "Por favor, insira apenas inteiros positivos"
    elif int(x) in dicionario:
        return dicionario[int(x)]
    elif int(x) == 0:
        dicionario[int(x)] = 0
        return 0        
    elif int(x) == 1:
        dicionario[int(x)] = 1
        return 1
    else:
        dicionario[int(x)-1] = fib(int(x)-1,dicionario)
        dicionario[int(x)-2] = fib(int(x)-2,dicionario)
        return fib(int(x)-1,dicionario) + fib(int(x)-2,dicionario)
            
def main():
    print("Seja bem-vindo, digite um n, onde n é inteiro e positivo, para calcular o n-ésimo termo na sequência de Fibonacci")
    print("(Para encerrar o programa insira uma entrada em branco)")
    n = 1
    dicionario = {}  
    while n != "":
        n = input("--> ")
        if n != "":
            print(fib(n,dicionario))

main()
