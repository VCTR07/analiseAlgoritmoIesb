A = [64,25,12,22,11,45,1,3,23,21,67,80,99,4,14]

def selectionSort(A):
    for i in range(len(A)):
        indice_minimo = i

        for j in range (i+1, len(A)):
            if (A[indice_minimo] > A[j]):
                indice_minimo = j


        A[i], A[indice_minimo] = A[indice_minimo], A[i]

    return A



print(selectionSort(A))

#print ("Array Organizado: ")
#for i in range(len(A)):
#    print("%d" %A[i])