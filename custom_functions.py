import numpy as np

def decompLU(A):        # Recebe uma matriz A (ndarray) e executa sua decomposição LU
    '''Recebe uma matriz A ndarray e devolve sua decomposição LU (como tupla L,U)
    
    Keyword arguments:
    A -- ndarray: a matriz quadrada que se deseja decompor
    '''
    print("Matriz A:")                                          # Imprime a matriz A que foi digitada pelo usuário
    print(A)                                                    # ||||||||||||||||||||||||||||||||||||||||||||||||
    n = len(A)                                                  # Guarda o tamanho da matriz A
    L = [[0]*n]*n                                               # Cria matriz L (n x n) com zeros em todas as posições
    for i in range(0,n):                                        # Itera para todas as linhas
        L[i][i] = 1                                             # Todos os elementos da diagonal viram 1
    L = np.array(L)                                             # Transforma a lista em ndarray
    U = [[0]*n]*n                                               # Cria matriz U (n x n) com zeros em todas as posições
    U = np.array(U)                                             # Transforma a lista em ndarray

    # ------------------------------------------------------------------------------------------------------
    # 2. Método que funciona mas não deve ser usado
    for j in range(0,n):                                        # Itera para todas as colunas
        for i in range(0,j+1):                                  # Itera para as linhas acima da diagonal
            s1 = sum(L[i][k] * U[k][j] for k in range(0,i))     # Soma dos elementos (multiplicação de matrizes)
            U[i][j] = A[i][j] - s1                              # Guarda o valor do(s) elementos(s) na linha i
        for i in range(j, n):                                   # Itera para as linhas abaixo da diagonal
            s2 = sum(U[k][j] * L[i][k] for k in range(0,j))     # Soma dos elementos (multiplicação de matrizes)
            L[i][j] = (A[i][j] - s2) / U[j][j]                  # Guarda o valor do(s) elemento(s) na coluna j
    # ------------------------------------------------------------------------------------------------------

    print("L: ")                                                # Imprime a matriz L (inferior)
    print(L)                                                    # Imprime a matriz L (inferior)
    print("U: ")                                                # Imprime a matriz U (superior)
    print(U)                                                    # Imprime a matriz U (superior)

    return L,U

def recebeA():          # Pede ao usuário os parâmetros da matriz A a ser decomposta
    '''Recebe do teclado do usuário o tamanho 'n' da matriz A e seus elementos um a um.
    
    Retorna uma matriz A como ndarray'''
    n = int(input("Digite o tamanho n da matriz (quadrada, n x n): "))  # Recebe o tamanho da matriz (quadrada) n x n
    A = []                                                              # Cria lista vazia para receber os valores
    for i in range(0,n):                                                # Itera para o número n de linhas
        linha = []                                                      # Cria lista vazia para vetor linha
        print("Linha %i"%(i+1))                                         # Mostra ao usuário a linha atual
        for j in range(0,n):                                            # Itera para o número n de colunas
            elem = int(input("A(%i,%i): "%(i+1,j+1)))                   # Recebe o elemento A[i][j]
            linha.append(elem)                                          # Add o elemento ao final do vetor linha
        print(67 * "-")                                                 # ------------------------------------------
        A.append(linha)                                                 # Add o vetor linha à matriz A
    return np.array(A)                                                            # Devolve a matriz como lista

def solveTridi(a,b,c,d):
    '''Resolve um sistema linear tridiagonal A*x = d utilizando uma decomposição LU --> LUx = d

    a --ndarray: um vetor contendo a subdiagonal dos coeficientes de x, de tamanho n
    b --ndarray: um vetor contendo a diagonal dos coeficientes de x, de tamanho n
    c --ndarray: um vetor contendo a sobrediagonal dos coeficientes de x, de tamanho n
    d --ndarray: um vetor dos coeficientes independentes do sistema, de tamanho n
    '''    
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    d = np.array(d)
    L, U = tridiDecompLU(a,b,c)
    x = solveLUxd(L,U,c,d)
    return x

def tridiDecompLU(a,b,c):
    n = len(b)
    L = [0]*(n-1)
    U = [0]*n
    L = np.array(L)
    U = np.array(U)

    U[0]=b[0]
    for i in range(1,n):
        L[i] = a[i]/U[i-1]
        U[i] = b[i] - L[i]*c[i-1]
    
    # print(L)
    # print(U)

    return L, U

def solveLUxd(L,U,c,d):
    n = len(d)
    y = [0]*n
    y[0] = d[0]
    for i in range(1,n):
        y[i] = d[i] - L[i]*y[i-1]
    x = [0]*n
    x[n-1] = y[n-1]/U[n-1]
    for i in range(n-2,-1,-1):
        x[i] = (y[i] - c[i]*x[i+1])/U[i]
    x = np.array(x)
    return x
