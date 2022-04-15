import numpy as np

def decompLU(A: np.ndarray):    # Recebe uma matriz A (ndarray) e executa sua decomposição LU
    '''Recebe uma matriz A e devolve sua decomposição LU
    
    Parâmetros
    ===
    A: ndarray
        A matriz quadrada que se deseja decompor

    Retorna
    ===
    tuple [
        L: ndarray - matriz inferior,
        U: ndarray - matriz superior
            ]
    '''
    print("Matriz A:")                                                          # Imprime a matriz A que foi inserida pelo usuário
    print(A)                                                                    # Imprime a matriz A que foi inserida pelo usuário
    n = len(A)                                                                  # Guarda o tamanho da matriz A
    L = [[0]*n]*n                                                               # Cria matriz L (n x n) com zeros em todas as posições
    L = np.array(L)                                                             # Transforma a lista em ndarray
    for i in range(0,n):                                                        # Itera para todas as linhas
        L[i,i] = 1                                                              # Todos os elementos da diagonal viram 1
    U = [[0]*n]*n                                                               # Cria matriz U (n x n) com zeros em todas as posições
    U = np.array(U)                                                             # Transforma a lista em ndarray
    for i in range(0,n):                                                        # Itera para todas as linhas
        U[i,i:] = A[i,i:] - np.dot(L[i,:i],U[:i,i:])                            # EXPRESSÃO (1) DO EXERCÍCIO
        L[(i+1):,i] = (1/U[i,i])*(A[(i+1):,i] - np.dot(L[(i+1):,:i],U[:i,i]))   # EXPRESSÃO (2) DO EXERCÍCIO
    print("Matriz inferior L: ")                                                # Imprime a matriz L (inferior)
    print(L)                                                                    # Imprime a matriz L (inferior)
    print("Matriz superior U: ")                                                # Imprime a matriz U (superior)
    print(U)                                                                    # Imprime a matriz U (superior)
    return L,U                                                                  # Retorna as matrizes L e U como tupla

def recebeA():                  # Pede ao usuário os parâmetros da matriz A a ser decomposta
    '''Recebe do teclado do usuário o tamanho 'n' da matriz A e seus elementos um a um.
    
    Retorna
    ====
    A: ndarray
        Matriz formada pelas inserções do usuário
        '''
    n = int(input("Digite o tamanho n da matriz (quadrada, n x n): "))      # Recebe o tamanho da matriz (quadrada) n x n
    A = []                                                                  # Cria lista vazia para receber os valores
    for i in range(0,n):                                                    # Itera para o número n de linhas
        print("Linha %i"%(i+1))                                             # Mostra ao usuário a linha atual
        A.append([int(input("A(%i,%i): "%(i+1,j+1))) for j in range(0,n)])  # Pede e concatena à lista o próximo valor
    return np.array(A)                                                      # Devolve a matriz como np.ndarray

def solveTridi(a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray):
    '''Resolve um sistema linear tridiagonal A*x = d utilizando uma decomposição LU --> LUx = d

    Parâmetros
    ===
    a: ndarray
        Vetor contendo a subdiagonal dos coeficientes de X, de tamanho n
    b: ndarray
        Vetor contendo a diagonal dos coeficientes de X, de tamanho n
    c: ndarray
        Vetor contendo a sobrediagonal dos coeficientes de X, de tamanho n
    d: ndarray
        Vetor dos coeficientes independentes do sistema, de tamanho n
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
