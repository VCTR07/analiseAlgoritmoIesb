#Busca Linear II
#Testando git novamente

import time

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
inicia_tempo = time.time_ns()
saida = busca_linear(A, n, x)
termina_tempo = time.time_ns()
tempo_total = termina_tempo - inicia_tempo

print(saida)
print('Tempo de execução em ns: ', tempo_total)