
#Busca Linear
#Teste git

def busca_linear(A, n, x):

    resposta = -1

    for i in range(0, n):
        if A[i] == x: resposta = i

    return resposta

#Entradas
A= [10,9,8,7,6,5,4,3,2,1]
n=len(A)
x=3

#Saída
saida = busca_linear(A, n, x)

print(saida)
