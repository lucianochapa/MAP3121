# Universidade de São Paulo
## Instituto de Matemática e Estatística - Departamento de Matemática Aplicada
## Escola Politécnica
# MAP3121 - Métodos Numéricos e Aplicações - 2022.1
## Exercício-programa 01
# Autoria
## Bruno Prasinos Bernal
## Luciano Chaparin Luisi


## Importação de libs
from math import cos, pi
import numpy as np

# Funções para receber input do usuário
def recebeMatriz() -> np.ndarray:                                                               # Recebe do usuário os parâmetros de uma matriz
    '''Recebe do teclado do usuário o tamanho 'n' da matriz A e seus elementos um a um.
    
    Retorna
    ---
    ndarray
        Matriz formada pelas inserções do usuário
    '''
    
    while True:
        try: n = int(input("Digite o tamanho n da matriz (quadrada, n x n): "))      # Recebe o tamanho da matriz (quadrada) n por n
        except ValueError: print("Inserção inválida.")
        else:
            if n == 0:
                print("Dimensão 0 inválida.")
            else:
                matriz = []                                                                          # Cria lista vazia para receber os valores
                for i in range(0,n):                                                            # Itera para o número 'n' de linhas
                    print("Linha %i"%(i+1))                                                     # Mostra ao usuário a linha atual
                    while True:
                        try: matriz.append([int(input("A[%i,%i]: "%(i+1,j+1))) for j in range(0,n)]) # Pede e concatena à lista o próximo valor
                        except ValueError: print("Inserção inválida.")
                        else: break
            return np.array(matriz, float)                                                       # Devolve a matriz 'A' como np.ndarray

def recebeVetor(tamanho: int, nome_vetor: str) -> np.ndarray:                                   # Recebe do usuário um vetor
    '''Recebe do teclado do usuário um vetor de tmanho 'n' e seus elementos um a um.
    
    Parâmetros
    ---
    n: int
        Tamanho do vetor
    nome_vetor: str
        Nome do vetor a ser exibido no terminal

    Retorna
    ---
    ndarray
        Vetor formado pelas inserções do usuário
    '''
    
    vetor = []                                                                          # Cria lista vazia para receber os valores
    for i in range(0,tamanho):
        while True:
            try: vetor.append(int(input("%s[%i de %i]: "%(nome_vetor,i+1,tamanho))))    # Pede e concatena à lista o próximo valor
            except ValueError: print("Inserção inválida.")
            else: break
    return np.array(vetor, float)                                                       # Devolve 'vetor' como np.ndarray

def printMenu(options: 'dict[int,str]', name:str) -> 'dict[int, str]':                          # Gera um menu de opções
    '''Imprime um menu de opções no terminal

    Parâmetros
    ---
    options: dict
        Um dicionário contendo o índice e descrição de cada opção
    name: str
        Nome do menu exibido no topo

    Retorna
    ---
    dict
        O mesmo dicionário de entrada com a opção "Encerrar programa" adicionada
    '''
    
    options[len(options)+1] = 'Encerrar programa'
    print(name, (max(0,66 - len(name)))*"-")                            # MENU--------------------------------------------
    for i in options:                                                   # Itera nas opções do menu
        print("%s. %s"%(i,options[i]))                                  # Imprime o número e descrição da opção
    print(67 * "-")                                                     # ------------------------------------------------
    return options                                                      # Retorna o dict 'options'

# Funções para transformações (ida e volta) entre matriz e vetores diagonais
def A2abc(matriz: np.ndarray) -> 'tuple[np.ndarray, np.ndarray]':                               # Transforma uma matriz tridiagonal em 3 vetores
    '''Recebe uma matriz tridiagonal e a transforma nos 3 vetores diagonais.

    Parâmetros
    ---
    matriz: ndarray
        Matriz tridiagonal

    Retorna
    ---
    tuple [
        ndarray
            Subdiagonal de A
        ndarray
            Diagonal de A
        ndarray
            Sobrediagonal de A
    ]
    '''
    
    n = len(matriz)                 # Guarda o tamanho da matriz
    a = []                          # Cria lista vazia
    b = []                          # Cria lista vazia
    c = []                          # Cria lista vazia
    for i in range(1,n):            # Itera para o tamanho da matriz
        a.append(matriz[i,i-1])     # Cria o vetor subdiagonal 'a'
        b.append(matriz[i-1,i-1])   # Cria o vetor diagonal 'b'
        c.append(matriz[i-1,i])     # Cria o vetor sobrediagonal 'c'
    b.append(matriz[n-1,n-1])       # Guarda o último valor do vetor diagonal 'b'
    a = np.array(a, float)          # Transforma a lista em np.ndarray
    b = np.array(b, float)          # Transforma a lista em np.ndarray
    c = np.array(c, float)          # Transforma a lista em np.ndarray
    return a, b, c                  # Retorna os valores 'a,b,c' como tupla [np.ndarray, np.ndarray, np.ndarray]

def abc2A(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:                           # Transforma 3 vetores diagonais em uma matriz tridiagonal
    '''Recebe 3 vetores diagonais e os transforma numa matriz tridiagonal.

    Parâmetros
    ---
    a: ndarray
        Subdiagonal de A
    b: ndarray
        Diagonal de A
    c: ndarray
        Sobrediagonal de A

    Retorna
    ---
    ndarray
        Matriz tridiagonal
    '''
    
    n = len(b)                              # Guarda o tamanho do vetor diagonal
    matriz = np.array([[0]*n]*n, float)     # Cria matriz 'A'(n por n) com zero em todas as posições
    for i in range(0,n-1):                  # Itera para o tamanho do vetor diagonal
        matriz[i+1,i] = a[i]                # Recebe valores do vetor subdiagonal 'a'
        matriz[i,i] = b[i]                  # Recebe valores do vetor diagonal 'b'
        matriz[i,i+1] = c[i]                # Recebe valores do vetor sobrediagonal 'c'
    matriz[n-1,n-1] = b[n-1]                # Recebe o último valor do vetor diagonal 'b'
    return matriz                           # Retorna a matriz 'A' como np.ndarray

def cycA2abc(matriz: np.ndarray) -> 'tuple[np.ndarray, np.ndarray, np.ndarray]':                # Transforma uma matriz tridiagonal cíclica em 3 vetores diagonais
    '''Recebe uma matriz tridiagonal cíclica e a transforma em 3 vetores
    
    Parâmetros
    ---
    matriz: ndarray
        Matriz tridiagonal cíclica

    Retorna
    ---
    tuple [
        ndarray
            Vetor subdiagonal
        ndarray
            Vetor diagonal
        ndarray
            Vetor sobrediagonal
    ]
    '''
    
    n = len(matriz)                 # Guarda o tamanho da matriz
    a = np.array([], float)         # Cria lista vazia
    b = np.array([], float)         # Cria lista vazia
    c = np.array([], float)         # Cria lista vazia
    a = np.append(a, matriz[0,n-1])     # Guarda o primeiro valor do vetor subdiagonal 'a'
    for i in range(1,n):        # Itera para o tamanho da matriz
        a = np.append(a, matriz[i,i-1])      # Cria o vetor subdiagonal 'a'
        b = np.append(b, matriz[i-1,i-1])    # Cria o vetor diagonal 'b'
        c = np.append(c, matriz[i-1,i])      # Cria o vetor sobrediagonal 'c'
    b = np.append(b, matriz[n-1,n-1])   # Guarda o último valor do vetor diagonal 'b'
    c = np.append(c, matriz[n-1,0])     # Guarda o último valor do vetor sobrediagonal 'c'
    a = np.array(a, float)
    b = np.array(b, float)
    c = np.array(c, float)
    return a, b, c

def abc2cycA(a: np.ndarray, b: np.ndarray, c: np.ndarray)-> np.ndarray:                         # Transforma 3 vetores diagonais em uma matriz tridiagonal
    '''Recebe 3 vetores diagonais e os transforma numa matriz tridiagonal cíclica.

    Parâmetros
    ---
    a: ndarray
        Subdiagonal de A
    b: ndarray
        Diagonal de A
    c: ndarray
        Sobrediagonal de A

    Retorna
    ---
    ndarray
        Matriz tridiagonal
    '''
    
    n = len(b)                              # Guarda o tamanho do vetor diagonal
    matriz = np.array([[0]*n]*n, float)     # Cria matriz 'A'(n por n) com zero em todas as posições
    matriz[0,0] = b[0]
    matriz[0,n-1] = a[0]
    matriz[n-1,0] = c[n-1]
    for i in range(1,n):                    # Itera para o tamanho do vetor diagonal
        matriz[i,i-1] = a[i]                # Recebe valores do vetor subdiagonal 'a'
        matriz[i,i] = b[i]                  # Recebe valores do vetor diagonal 'b'
        matriz[i-1,i] = c[i-1]              # Recebe valores do vetor sobrediagonal 'c'
    return(matriz)

# Funções de cálculo do exercício-programa
def decompLU(matriz: np.ndarray) -> 'tuple[np.ndarray, np.ndarray]':                            # Recebe uma matriz e executa sua decomposição LU
    '''Recebe uma matriz A e devolve sua decomposição LU
    
    Parâmetros
    ---
    matriz: ndarray
        A matriz quadrada que se deseja decompor

    Retorna
    ---
    tuple [
        ndarray
            matriz inferior
        ndarray
            matriz superior
    ]
    '''
    
    n = len(matriz)                                                                  # Guarda o tamanho da matriz 'A'
    L = np.array([[0]*n]*n, float)                                              # Cria matriz 'L'(n por n) com zeros em todas as posições e transforma a lista em ndarray
    for i in range(0,n):                                                        # Itera para todas as linhas
        L[i,i] = 1                                                              # Todos os elementos da diagonal viram 1
    U = np.array([[0]*n]*n, float)                                              # Cria matriz 'U'(n por n) com zeros em todas as posições e transforma a lista em ndarray
    for i in range(0,n):                                                        # Itera para todas as linhas
        U[i,i:] = matriz[i,i:] - np.dot(L[i,:i],U[:i,i:])                            # EXPRESSÃO (1) DO EXERCÍCIO
        L[(i+1):,i] = (1/U[i,i])*(matriz[(i+1):,i] - np.dot(L[(i+1):,:i],U[:i,i]))   # EXPRESSÃO (2) DO EXERCÍCIO
    return L,U                                                                  # Retorna as matrizes 'L,U' como tupla [np.ndarray, np.ndarray]

def decompLUabc(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> 'tuple[np.ndarray, np.ndarray]':# Recebe os vetores diagonais a,b,c e decompõe em vetores l e u
    '''Realiza a decomposição LU a partir dos 3 vetores diagonais
    
    Parâmetros
    ---
    a: ndarray
        Vetor subdiagonal
    b: ndarray
        Vetor diagonal
    c: ndarray
        Vetor sobrediagonal

    Retorna
    ---
    tuple [
        ndarray
            Vetor subdiagonal da matriz inferior
        ndarray
            Vetor diagonal da matriz superior
    ]
    '''
    
    n = len(b)                              # Guarda o valor do vetor diagonal
    l = np.array([0]*(n-1), float)          # Cria um vetor vazio com zero em todas as posições, de tamanho n-1
    u = np.array([0]*n, float)              # Cria um vetor vazio com zero em todas as posições, de tamanho n
    u[0] = b[0]                             # Primeiro termo do vetor 'u'
    for i in range(1,n):                    # Itera ao longo do tamanho do vetor diagonal
        l[i-1] = a[i-1]/u[i-1]              # Expressão do exercício
        u[i] = b[i] - l[i-1]*c[i-1]         # Expressão do exercício
    return l, u                             # Retorna os vetores 'l,u' como tupla [np.ndarray, np.ndarray]

def solveLydUxy(l: np.ndarray, u: np.ndarray, c: np.ndarray, d: np.ndarray) -> np.ndarray:      # Resolve um sistema tridiagonal a partir de Ly = d, Ux = y
    '''Recebe os vetores subdiagonal da matriz inferior, diagonal e sobrediagonal da matriz superior, termos independentes e retorna a solução

    Parâmetros
    ---
    l: ndarray
        Vetor subdiagonal da matriz inferior
    u: ndarray
        Vetor diagonal da matriz superior
    c: ndarray
        Vetor sobrediagonal da matriz superior
    d: ndarray
        Vetor de termos independentes

    Retorna
    ---
    ndarray
        Vetor de soluções do sistema
    '''
    
    n = len(d)                              # Guarda o tamanho do sistema
    y = np.array([0]*n, float)              # Cria um vetor 'y' com zero em todas as posições
    y[0] = d[0]                             # Primeiro termo de 'y'
    for i in range(1,n):                    # Itera para o tamanho do sistema
        y[i] = d[i] - l[i-1]*y[i-1]         # Expressão do exercício
    # print("Sistema Ly=d")
    # print("L: ")
    # print(abc2A(l,[1]*(len(l)+1),[0]*(len(l)+1)))
    # print("d: ")
    # print(d)
    # print("Valor encontrado para \'y\'")
    # print("y: ")
    # print(y)
    x = np.array([0]*n, float)              # Cria um vetor 'x' com zero em todas as posições
    x[n-1] = y[n-1]/u[n-1]                  # Último termo de 'x'
    for i in range(n-2,-1,-1):              # Itera para o tamanho do sistema, do último para o primeiro termo
        x[i] = (y[i] - c[i]*x[i+1])/u[i]    # Expressão do exercício
    # print("Sistema Ux=y")
    # print("U: ")
    # print(abc2A([0]*(len(l)+1),u,c))
    # print("y: ")
    # print(y)
    # print("Valor encontrado para \'x\'")
    # print("x: ")
    # print(x)
    return x                                # Retorna 'x' como np.ndarray

def solveTridi(a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray) -> np.ndarray:       # Recebe vetores diagonais e independente e devolve a resolução
    '''Resolve um sistema linear tridiagonal A*x = d utilizando uma decomposição LU: Ly = d, Ux = y

    Parâmetros
    ---
    a: ndarray
        Vetor contendo a subdiagonal dos coeficientes de X
    b: ndarray
        Vetor contendo a diagonal dos coeficientes de X
    c: ndarray
        Vetor contendo a sobrediagonal dos coeficientes de X
    d: ndarray
        Vetor dos coeficientes independentes do sistema

    Retorna
    ---
    ndarray
        Vetor de soluções para X do sistema
    '''    
    
    # print("Sistema Ax=d")
    # print("A: ")
    # A = abc2A(a,b,c)
    # print(A)
    # print("d: ")
    # print(d)
    l, u = decompLUabc(a,b,c)   # Decompõe 3 vetores 'a,b,c' de um sistema tridiagonal em vetores 'l' (subdiagonal inferior) e 'u' (diagonal superior)
    # print("Decomposição A=LU")
    # print("A: ")
    # print(A)
    # print("L: ")
    # print(abc2A(l,[1]*(len(l)+1),[0]*(len(l)+1)))
    # print("U: ")
    # print(abc2A([0]*len(u),u,c))
    return solveLydUxy(l,u,c,d)        # Resolve o sistema para X

def solveCycTridi(a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray) -> np.ndarray:    # Recebe vetores diagonais e independente e devolve a resolução
    '''Resolve um sistema tridiagonal cíclico A*x = d passando por sua submatriz principal T e resolvendo: T*(x')+(x_n)*v=(d'), (w^t)*(x')+(x_n)(b_n)=(d_n)

    Parâmetros
    ---
    a: ndarray
        Vetor contendo a subdiagonal
    b: ndarray
        Vetor contendo a diagonal
    c: ndarray
        Vetor contendo a sobrediagonal
    d: ndarray
        Vetor dos coeficientes independentes do sistema

    Retorna
    ---
    ndarray
        Vetor de soluções para X do sistema
    '''    
    
    n = len(b)
    v = np.array([], float)
    w = np.array([], float)
    v = np.append(v,a[0])
    for t in range(1,n-2):
        v = np.append(v,0)
    v = np.append(v,c[n-2])
    w = np.append(w,c[n-1])
    w = np.append(w,a[n-1])
    l, u = decompLUabc(np.delete(a,[0,n-1]),np.delete(b,n-1),np.delete(c,[n-1,n-2]))
    y = solveLydUxy(l,u,np.delete(c,[n-1,n-2]),np.delete(d,[n-1]))
    z = solveLydUxy(l,u,np.delete(c,[n-1,n-2]),v)
    x_n = (d[n-1]-c[n-1]*y[0]-a[n-1]*y[n-2])/(b[n-1]-c[n-1]*z[0]-a[n-1]*z[n-2])
    x = y - x_n*z
    x = np.append(x,x_n)
    x = np.array(x, float)
    
    return x        # Resolve o sistema para X

def genSysMAP(n: int) -> 'tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]':               # Gera vetores diagonais e termos independentes de um sistema tridiagonal
    '''Gera um sistema linear tridiagonal padronizado de acordo com o exercício-programa

    Parâmetros
    ---
    n: int
        Dimensão do sistema

    Retorna
    ---
    tuple [
        ndarray
            Vetor subdiagonal da matriz de coeficientes do sistema
        ndarray
            Vetor diagonal da matriz de coeficientes do sistema
        ndarray
            Vetor sobrediagonal da matriz de coeficientes do sistema
        ndarray
            Vetor de coeficientes independentes do sistema
    ]    
    '''
    
    a = np.array([], float)
    b = np.array([], float)
    c = np.array([], float)
    d = np.array([], float)
    for i in range(0,n-1):
        a = np.append(a,(2*(i+1)-1)/(4*(i+1)))
        c = np.append(c,1-a[i])
        b = np.append(b,2)
        d = np.append(d,cos(2*pi*((i+1)**2)/(n**2)))
    a = np.append(a,(2*n-1)/(2*n))
    c = np.append(c,1-a[n-1])
    b = np.append(b,2)
    d = np.append(d,cos(2*pi))
    a = np.array(a, float)
    b = np.array(b, float)
    c = np.array(c, float)
    d = np.array(d, float)
    
    return a,b,c,d
