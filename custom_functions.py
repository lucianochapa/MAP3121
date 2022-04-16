import numpy as np

def recebeA():                  # Pede ao usuário os parâmetros da matriz A a ser decomposta
    '''Recebe do teclado do usuário o tamanho 'n' da matriz A e seus elementos um a um.
    
    Retorna
    ====
    A: ndarray
        Matriz formada pelas inserções do usuário
        '''
    n = int(input("Digite o tamanho n da matriz (quadrada, n x n): "))      # Recebe o tamanho da matriz (quadrada) n por n
    A = []                                                                  # Cria lista vazia para receber os valores
    for i in range(0,n):                                                    # Itera para o número 'n' de linhas
        print("Linha %i"%(i+1))                                             # Mostra ao usuário a linha atual
        A.append([int(input("A(%i,%i): "%(i+1,j+1))) for j in range(0,n)])  # Pede e concatena à lista o próximo valor
    return np.array(A, float)                                               # Devolve a matriz 'A' como np.ndarray

def decompLU(A: np.ndarray):    # Recebe uma matriz A (ndarray) e executa sua decomposição LU
    '''Recebe uma matriz A e devolve sua decomposição LU
    
    Parâmetros
    ===
    A: ndarray
        A matriz quadrada que se deseja decompor

    Retorna
    ===
    tuple [
        L: ndarray
            matriz inferior
        U: ndarray
            matriz superior
    ]
    '''
    print("Matriz A:")                                                          # Imprime a matriz 'A' que foi inserida pelo usuário
    print(A)                                                                    # Imprime a matriz 'A' que foi inserida pelo usuário
    n = len(A)                                                                  # Guarda o tamanho da matriz 'A'
    L = np.array([[0]*n]*n, float)                                              # Cria matriz 'L'(n por n) com zeros em todas as posições e transforma a lista em ndarray
    for i in range(0,n):                                                        # Itera para todas as linhas
        L[i,i] = 1                                                              # Todos os elementos da diagonal viram 1
    U = np.array([[0]*n]*n, float)                                              # Cria matriz 'U'(n por n) com zeros em todas as posições e transforma a lista em ndarray
    for i in range(0,n):                                                        # Itera para todas as linhas
        U[i,i:] = A[i,i:] - np.dot(L[i,:i],U[:i,i:])                            # EXPRESSÃO (1) DO EXERCÍCIO
        L[(i+1):,i] = (1/U[i,i])*(A[(i+1):,i] - np.dot(L[(i+1):,:i],U[:i,i]))   # EXPRESSÃO (2) DO EXERCÍCIO
    print("Matriz inferior L: ")                                                # Imprime a matriz 'L' (inferior)
    print(L)                                                                    # Imprime a matriz 'L' (inferior)
    print("Matriz superior U: ")                                                # Imprime a matriz 'U' (superior)
    print(U)                                                                    # Imprime a matriz 'U' (superior)
    return L,U                                                                  # Retorna as matrizes 'L,U' como tupla [np.ndarray, np.ndarray]

def decompLUabc(a: np.ndarray, b: np.ndarray, c: np.ndarray):   # Recebe os vetores diagonais a,b,c e decompõe em vetores l e u
    '''Realiza a decomposição LU a partir dos 3 vetores diagonais
    
    Parâmetros
    ===
    a: ndarray
        Vetor subdiagonal
    b: ndarray
        Vetor diagonal
    c: ndarray
        Vetor sobrediagonal

    Retorna
    ===
    tuple [
        l: ndarray
            Vetor subdiagonal da matriz inferior
        u: ndarray
            Vetor diagonal da matriz superior
    ]
    '''
    n = len(b)                              # Guarda o valor do vetor diagonal
    l = np.array([0]*(n-1), float)          # Cria um vetor vazio com zero em todas as posições, de tamanho n-1
    u = np.array([0]*n, float)              # Cria um vetor vazio com zero em todas as posições, de tamanho n
    u[0] = b[0]                             # Primeiro termo do vetor 'u'
    for i in range(1,n):                    # Itera ao longo do tamanho do vetor diagonal
        l[i-1] = a[i]/u[i-1]                # Expressão do exercício
        u[i] = b[i] - l[i-1]*c[i-1]         # Expressão do exercício
    return l, u                             # Retorna os vetores 'l,u' como tupla [np.ndarray, np.ndarray]

def solveLydUxy(l,u,c,d):   # Resolve um sistema tridiagonal a partir de Ly = d, Ux = y
    '''Recebe os vetores subdiagonal da matriz inferior, diagonal e sobrediagonal da matriz superior, termos independentes e retorna a solução

    Parâmetros
    ===
    L: ndarray
        Vetor subdiagonal da matriz inferior
    U: ndarray
        Vetor diagonal da matriz superior
    c: ndarray
        Vetor sobrediagonal da matriz superior
    d: ndarray
        Vetor de termos independentes

    Retorna
    ===
    x: ndarray
        Vetor de soluções do sistema
    '''
    n = len(d)                              # Guarda o tamanho do sistema
    y = np.array([0]*n, float)              # Cria um vetor 'y' com zero em todas as posições
    y[0] = d[0]                             # Primeiro termo de 'y'
    for i in range(1,n):                    # Itera para o tamanho do sistema
        y[i] = d[i] - l[i-1]*y[i-1]         # Expressão do exercício
    x = np.array([0]*n, float)              # Cria um vetor 'x' com zero em todas as posições
    x[n-1] = y[n-1]/u[n-1]                  # Último termo de 'x'
    for i in range(n-2,-1,-1):              # Itera para o tamanho do sistema, do último para o primeiro termo
        x[i] = (y[i] - c[i]*x[i+1])/u[i]    # Expressão do exercício
    return x                                # Retorna 'x' como np.ndarray

def A2abc(A: np.ndarray):   # Transforma uma matriz A tridiagonal em 3 vetores
    '''Recebe uma matriz tridiagonal e a transforma nos 3 vetores diagonais.

    Parâmetros
    ===
    A: ndarray
        Matriz tridiagonal

    Retorna
    ===
    tuple [
        a: ndarray
            Subdiagonal de A
        b: ndarray
            Diagonal de A
        c: ndarray
            Sobrediagonal de A
    ]
    '''
    n = len(A)                  # Guarda o tamanho da matriz
    a = []                      # Cria lista vazia
    b = []                      # Cria lista vazia
    c = []                      # Cria lista vazia
    for i in range(1,n):        # Itera para o tamanho da matriz
        a.append(A[i,i-1])      # Cria o vetor subdiagonal 'a'
        b.append(A[i-1,i-1])    # Cria o vetor diagonal 'b'
        c.append(A[i-1,i])      # Cria o vetor sobrediagonal 'c'
    b.append(A[n-1,n-1])        # Guarda o último valor do vetor diagonal 'b'
    a = np.array(a)             # Transforma a lista em np.ndarray
    b = np.array(b)             # Transforma a lista em np.ndarray
    c = np.array(c)             # Transforma a lista em np.ndarray
    return a, b, c              # Retorna os valores 'a,b,c' como tupla [np.ndarray, np.ndarray, np.ndarray]

def abc2A(a: np.ndarray, b: np.ndarray, c: np.ndarray): # Transforma 3 vetores diagonais em uma matriz tridiagonal
    '''Recebe 3 vetores diagonais e os transforma numa matriz tridiagonal.

    Parâmetros
    ===
    a: ndarray
        Subdiagonal de A
    b: ndarray
        Diagonal de A
    c: ndarray
        Sobrediagonal de A

    Retorna
    ===
    A: ndarray
        Matriz tridiagonal
    '''
    n = len(b)                          # Guarda o tamanho do vetor diagonal
    A = np.array([[0]*n]*n, float)      # Cria matriz 'A'(n por n) com zero em todas as posições
    for i in range(0,n-1):              # Itera para o tamanho do vetor diagonal
        A[i+1,i] = a[i]                 # Recebe valores do vetor subdiagonal 'a'
        A[i,i] = b[i]                   # Recebe valores do vetor diagonal 'b'
        A[i,i+1] = c[i]                 # Recebe valores do vetor sobrediagonal 'c'
    A[n-1,n-1] = b[n-1]                 # Recebe o último valor do vetor diagonal 'b'
    return A                            # Retorna a matriz 'A' como np.ndarray

def solveTridi(a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray): # Recebe vetores diagonais e independente e devolve a resolução
    '''Resolve um sistema linear tridiagonal A*x = d utilizando uma decomposição LU: Ly = d, Ux = y

    Parâmetros
    ===
    a: ndarray
        Vetor contendo a subdiagonal dos coeficientes de X
    b: ndarray
        Vetor contendo a diagonal dos coeficientes de X
    c: ndarray
        Vetor contendo a sobrediagonal dos coeficientes de X
    d: ndarray
        Vetor dos coeficientes independentes do sistema

    Retorna
    ===
    x: ndarray
        Vetor de soluções para X do sistema
    '''    
    l, u = decompLUabc(a,b,c)   # Decompõe 3 vetores 'a,b,c' de um sistema tridiagonal em vetores 'l' (subdiagonal inferior) e 'u' (diagonal superior)
    x = solveLydUxy(l,u,c,d)    # Usa os vetores 'l' (subdiagonal inferior), 'u' (diagonal superior), 'c' (sobrediagonal superior), 'd' (termos independentes) e resolve o sistema para X
    return x                    # Retorna um vetor de soluções