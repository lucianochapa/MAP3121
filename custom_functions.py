import numpy as np

def decompLU(A):        # Recebe uma matriz A e executa sua decomposição LU
    '''Recebe uma matriz A e devolve a matriz e sua decomposição LU (como tripla A,L,U)
    
    Keyword arguments:
    A -- lista contendo a matriz quadrada que se deseja decompor
    '''
    A = np.array(A)                                             # Transforma a lista em numpy.array
    print("Matriz A:")                                          # Imprime a matriz A que foi digitada pelo usuário
    print(A)                                                    # ||||||||||||||||||||||||||||||||||||||||||||||||
    n = len(A)                                                  # Guarda o tamanho da matriz A
    L = [[0] * n for i in range(0,n)]                           # Cria matriz L (n x n) com zeros em todas as posições
    for i in range(0,n):                                        # Itera para todas as linhas
        L[i][i] = 1                                             # Todos os elementos da diagonal viram 1
    L = np.array(L)                                             # Transforma a lista em numpy.array
    U = [[0] * n for i in range(0,n)]                           # Cria matriz U (n x n) com zeros em todas as posições
    U = np.array(U)                                             # Transforma a lista em numpy.array

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

    return A,L,U

def recebeA():          # Pede ao usuário os parâmetros da matriz A a ser decomposta
    '''Recebe do usuário o tamanho 'n' da matriz A e seus elementos um a um'''
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
    return A                                                            # Devolve a matriz como lista

def solveTridi():
    print("a")