#15 de Octubre de 2024 
a = [[4,3],[9,3]]
print(a)
print()
def newMatrix(f,c,n):
    matriz = []
    for i in range(f):
        a = [n]*c
        matriz.append(a)
    return matriz
def sumaMatriz(A,B):
    numFilasA = len(A)
    numFilasB = len(B)
    numColumnasA = len(A[0])
    numColumnasB = len(B[0])
    
    if numFilasA == numFilasB and numColumnasA == numColumnasB:
        C = newMatrix(numFilasA, numColumnasA, 0) 
        for i in range(numFilasA): 
            for j in range(numColumnasA):
                C[i][j] = A[i][j] + B[i][j]
    return C
suma = sumaMatriz([[1,2,3],[7,8,9],[13,14,15]], [[4,5,6],[10,11,12],[16,17,18]])
print(suma)
def multiplicacionMatriz(A,B):
    # *Dimensiones de la matriz
    numFilasA = len(A)
    numFilasB = len(B)
    numColumnasA = len(A[0])
    numColumnasB = len(B[0])
    if numFilasA == numFilasB and numColumnasA == numColumnasB:
        C = newMatrix(numFilasA, numColumnasA, 0) 
        for i in range(numFilasA): 
            for j in range(numColumnasA):
                C[i][j] = A[i][j] * B[i][j]
    return C
def show_matrix(M):
        """ Imprime los valores almacenados en la matriz """
        filas = len(M)
        columnas = len(M[0])
        for i in range(filas):
            for j in range(columnas):
                print("| {0} ".format(M[i][j]), sep=',', end='')
            print('|\n')
a = [[1,2,3],[7,8,9],[4,5,6]]
show_matrix(a)
print()
show_matrix(suma)
