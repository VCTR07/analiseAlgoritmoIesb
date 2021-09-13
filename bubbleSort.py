
def bubbleSort(lista):
    for num_pass in range (len(lista)-1, 0, -1):
        for i in range(num_pass):
            if lista[i] > lista[i+1]:
                #lista[i], lista[i+1] = lista[i+1], lista[i]
                aux = lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=aux


lista = [10, 17, 18, 3, 5, 0, 33, 97]
bubbleSort(lista)
print(lista)