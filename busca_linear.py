
#Busca Linear
#Testando git

def busca_linear_sentinela(A, n, x):

    resposta = -1

    ultimo = A[n-1]
    A[n-1] = x
    i = 0

    while A[i] != x:
        i+=1
    
    A[n-1] = ultimo

    if i < n-1 or A[n-1] == x:
        resposta = i
    
    return resposta    

#Entradas
A= [10,9,8,7,6,5,4,3,2,1]
n=len(A)
x=3

#Saída
saida = busca_linear_sentinela(A, n, x)

print(saida)
