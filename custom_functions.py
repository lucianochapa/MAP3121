# Universidade de São Paulo
## Instituto de Matemática e Estatística - Departamento de Matemática Aplicada
## Escola Politécnica
# MAP3121 - Métodos Numéricos e Aplicações - 2022.1
## Exercício-programa: Módulo de funções customizadas
# Autoria
## Bruno Prasinos Bernal
## Luciano Chaparin Luisi


# from math import cos, pi
import numpy as np

# Funções para receber input do usuário
def printMenu(options: 'dict[int,str]', name:str) -> 'dict[int, str]':
    '''Imprime um menu de opções (inclui 'Encerrar programa') no terminal

    Parâmetros
    ---
    `options`: dict
        Um dicionário contendo o índice e descrição de cada opção
    `name`: str
        Nome do menu exibido no topo

    Retorna
    ---
    `options`: dict
        O mesmo dicionário de entrada com a opção "Encerrar programa" adicionada
    '''
    
    options[len(options)+1] = 'Encerrar programa'
    print(name, (max(0,66 - len(name)))*"-")
    # Itera nas opções do menu; Imprime o número e descrição da opção
    for i in options:
        print("%s. %s"%(i,options[i]))
    print(67 * "-")
    return options

def recebeMatriz() -> np.ndarray:
    '''Recebe do teclado do usuário o tamanho 'n' de uma matriz A e seus elementos, um a um.
    
    Retorna
    ---
    `matriz`: ndarray
        Matriz formada pelas inserções do usuário
    '''
    
    while True:
        # Recebe o tamanho da matriz (quadrada) n por n
        try: n = int(input("Digite o tamanho n da matriz (quadrada, n x n): "))
        except ValueError: print("Inserção inválida.")
        else:
            if n == 0:
                print("Dimensão 0 inválida.")
            else:
                # Cria lista vazia para receber os valores
                matriz = []
                # Itera para o número 'n' de linhas; Mostra ao usuário a linha atual
                for i in range(0,n):
                    print("Linha %i"%(i+1))
                    while True:
                        # Pede o próximo valor e concatena à lista
                        try: matriz.append([float(input("A[%i,%i]: "%(i+1,j+1))) for j in range(0,n)])
                        except ValueError: print("Inserção inválida.")
                        else: break
            return np.array(matriz, float)

def recebeVetor(tamanho: int, nome_vetor: str) -> np.ndarray:
    '''Recebe do teclado do usuário um vetor de tamanho `n` e seus elementos um a um.
    
    Parâmetros
    ---
    `n`: int
        Tamanho do vetor
    `nome_vetor`: str
        Nome do vetor a ser exibido no terminal

    Retorna
    ---
    `vetor`: ndarray
        Vetor formado pelas inserções do usuário
    '''
    
    # Cria lista vazia para receber os valores
    vetor = []
    for i in range(0,tamanho):
        while True:
            # Pede e concatena à lista o próximo valor
            try: vetor.append(float(input("%s[%i de %i]: "%(nome_vetor,i+1,tamanho))))
            except ValueError: print("Inserção inválida.")
            else: break
    return np.array(vetor, float)

# Funções para transformações (ida e volta) entre matriz e vetores diagonais
def A2abc(matriz: np.ndarray) -> 'tuple[np.ndarray, np.ndarray]':
    '''Recebe uma matriz tridiagonal e a transforma em 3 vetores diagonais.

    Parâmetros
    ---
    `matriz`: ndarray
        Matriz tridiagonal

    Retorna
    ---
    tuple [
        `a`: ndarray
            Subdiagonal de A
        `b`: ndarray
            Diagonal de A
        `c`: ndarray
            Sobrediagonal de A
    ]
    '''
    
    # Guarda o tamanho da matriz
    n = len(matriz)
    # Cria listas vazias
    a = []
    b = []
    c = []
    # Itera para o tamanho da matriz; cria os vetores subdiagonal 'a', diagonal 'b', sobrediagonal 'c'
    for i in range(1,n):
        a.append(matriz[i,i-1])
        b.append(matriz[i-1,i-1])
        c.append(matriz[i-1,i])
    # Guarda o último valor do vetor diagonal 'b'
    b.append(matriz[n-1,n-1])
    # Transforma as listas em np.ndarray
    a = np.array(a, float)
    b = np.array(b, float)
    c = np.array(c, float)
    return a, b, c

def abc2A(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    '''Recebe 3 vetores diagonais e os transforma numa matriz tridiagonal.

    Parâmetros
    ---
    `a`: ndarray
        Subdiagonal de A
    `b`: ndarray
        Diagonal de A
    `c`: ndarray
        Sobrediagonal de A

    Retorna
    ---
    `A`: ndarray
        Matriz tridiagonal
    '''
    
    # Guarda o tamanho do vetor diagonal principal
    n = len(b)
    # Cria matriz 'A'(n por n) com zero em todas as posições
    matriz = np.zeros((n,n))
    # Itera para o tamanho do vetor diagonal
    for i in range(0,n-1):
        # Recebe valores dos vetores subdiagonal 'a', diagonal 'b', sobrediagonal 'c'
        matriz[i+1,i] = a[i]
        matriz[i,i] = b[i]
        matriz[i,i+1] = c[i]
    # Recebe o último valor do vetor diagonal 'b'
    matriz[n-1,n-1] = b[n-1]
    return matriz

def abc2cycA(a: np.ndarray, b: np.ndarray, c: np.ndarray)-> np.ndarray:
    '''Recebe 3 vetores diagonais e os transforma numa matriz tridiagonal cíclica.

    Parâmetros
    ---
    `a`: ndarray
        Subdiagonal de A
    `b`: ndarray
        Diagonal de A
    `c`: ndarray
        Sobrediagonal de A

    Retorna
    ---
    `A`: ndarray
        Matriz tridiagonal cíclica
    '''
    
    # Guarda o tamanho do vetor diagonal
    n = len(b)
    # Cria matriz 'A'(n por n) com zero em todas as posições
    matriz = np.zeros((n,n))
    matriz[0,0] = b[0]
    matriz[0,n-1] = a[0]
    matriz[n-1,0] = c[n-1]
    # Itera para o tamanho do vetor diagonal
    for i in range(1,n):
        # Recebe valores dos vetores subdiagonal 'a', diagonal 'b', sobrediagonal 'c'
        matriz[i,i-1] = a[i]
        matriz[i,i] = b[i]
        matriz[i-1,i] = c[i-1]
    return matriz

def cycA2abc(matriz: np.ndarray) -> 'tuple[np.ndarray, np.ndarray, np.ndarray]':
    '''Recebe uma matriz tridiagonal cíclica e a transforma em 3 vetores diagonais
    
    Parâmetros
    ---
    matriz: ndarray
        Matriz tridiagonal cíclica

    Retorna
    ---
    tuple [
        a: ndarray
            Vetor subdiagonal
        b: ndarray
            Vetor diagonal
        c: ndarray
            Vetor sobrediagonal
    ]
    '''
    
    # Guarda o tamanho da matriz
    n = len(matriz)
    # Cria listas vazias
    a = np.array([], float)
    b = np.array([], float)
    c = np.array([], float)
    # Guarda o primeiro valor do vetor subdiagonal 'a'
    a = np.append(a, matriz[0,n-1])
    # Itera para o tamanho da matriz
    for i in range(1,n):
        # Cria os vetores subdiagonal 'a', diagonal 'b', sobrediagonal 'c'
        a = np.append(a, matriz[i,i-1])
        b = np.append(b, matriz[i-1,i-1])
        c = np.append(c, matriz[i-1,i])
    # Guarda o último valor dos vetores 'b' e 'c'
    b = np.append(b, matriz[n-1,n-1])
    c = np.append(c, matriz[n-1,0])
    a = np.array(a, float)
    b = np.array(b, float)
    c = np.array(c, float)
    return a, b, c

# Funções de cálculo do exercício-programa 1
def decompLU(matriz: np.ndarray) -> 'tuple[np.ndarray, np.ndarray]':
    '''Recebe uma matriz e devolve sua decomposição LU
    
    Parâmetros
    ---
    `matriz`: ndarray
        A matriz quadrada que se deseja decompor

    Retorna
    ---
    tuple [
        `L`: ndarray
            matriz inferior
        `U`: ndarray
            matriz superior
    ]
    '''
    
    # Guarda o tamanho da matriz
    n = len(matriz)
    # Cria matriz 'L'(n por n) com zeros em todas as posições e transforma a lista em ndarray
    L = np.zeros((n,n))
    # Itera para todas as linhas; todos os elementos da diagonal viram 1
    for i in range(0,n):
        L[i,i] = 1
    # Cria matriz 'U'(n por n) com zeros em todas as posições e transforma a lista em ndarray
    U = np.zeros((n,n))
    # Itera para todas as linhas; realiza a decomposição (a exemplo das expressões 1 e 2 do enunciado)
    for i in range(0,n):
        U[i,i:] = matriz[i,i:] - np.dot(L[i,:i],U[:i,i:])
        L[(i+1):,i] = (1/U[i,i])*(matriz[(i+1):,i] - np.dot(L[(i+1):,:i],U[:i,i]))
    return L, U

def decompLUabc(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> 'tuple[np.ndarray, np.ndarray]':
    '''Recebe 3 vetores diagonais de uma matriz e retorna sua decomposição LU (como vetores `l` e `u`)
    
    Parâmetros
    ---
    `a`: ndarray
        Vetor subdiagonal
    `b`: ndarray
        Vetor diagonal
    `c`: ndarray
        Vetor sobrediagonal

    Retorna
    ---
    tuple [
        `l`: ndarray
            Vetor subdiagonal da matriz inferior
        `u`: ndarray
            Vetor diagonal da matriz superior
    ]
    '''
    
    # Guarda o valor do vetor diagonal
    n = len(b)
    # Cria vetores com zero em todas as posições, de tamanhos 'n-1' e 'n'
    l = np.zeros(n-1)
    u = np.zeros(n)
    # Primeiro termo do vetor 'u'
    u[0] = b[0]
    # Itera ao longo do tamanho do vetor diagonal; realiza a decomposição (a exemplo das expressões do enunciado)
    for i in range(1,n):
        l[i-1] = a[i-1]/u[i-1]
        u[i] = b[i] - l[i-1]*c[i-1]
    return l, u

def genSysMAP(n: int) -> 'tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]':
    '''Gera um sistema tridiagonal padronizado de acordo com o enunciado do exercício-programa, retornando 3 vetores diagonais e um vetor de termos independentes (1<=i<=n):

        a[i]=(2i-1)/4i, a[n]=(2n-1)/2n

        b[i]=2
        
        c[i]=1-a[i]
        
        d[i]=cos{2(pi)i²/n²}

    Parâmetros
    ---
    `n`: int
        Dimensão do sistema

    Retorna
    ---
    tuple [
        `a`: ndarray
            Vetor subdiagonal da matriz de coeficientes do sistema
        `b`: ndarray
            Vetor diagonal da matriz de coeficientes do sistema
        `c`: ndarray
            Vetor sobrediagonal da matriz de coeficientes do sistema
        `d`: ndarray
            Vetor de coeficientes independentes do sistema
    ]
    '''
    
    # Cria vetores vazios
    a = np.array([], float)
    b = np.array([], float)
    c = np.array([], float)
    d = np.array([], float)
    # Itera para a dimensão do sistema
    for i in range(0,n-1):
        a = np.append(a,(2*(i+1)-1)/(4*(i+1)))
        c = np.append(c,1-a[i])
        b = np.append(b,2)
        d = np.append(d,np.cos(2*np.pi*((i+1)**2)/(n**2)))
    # Anexa os últimos elementos a cada vetor
    a = np.append(a,(2*n-1)/(2*n))
    c = np.append(c,1-a[n-1])
    b = np.append(b,2)
    d = np.append(d,np.cos(2*np.pi))
    a = np.array(a, float)
    b = np.array(b, float)
    c = np.array(c, float)
    d = np.array(d, float)
    return a,b,c,d

def solveCycTridi(a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray) -> np.ndarray:
    '''Resolve um sistema tridiagonal cíclico Ax = d a partir dos vetores diagonais e de termos independentes, passando por sua submatriz principal T e resolvendo: T*(x')+(x_n)*v=(d'), (w^t)*(x')+(x_n)(b_n)=(d_n)

    Parâmetros
    ---
    `a`: ndarray
        Vetor contendo a subdiagonal
    `b`: ndarray
        Vetor contendo a diagonal
    `c`: ndarray
        Vetor contendo a sobrediagonal
    `d`: ndarray
        Vetor dos coeficientes independentes do sistema

    Retorna
    ---
    `x`: ndarray
        Vetor de soluções para X do sistema
    '''    
    
    # Guarda o tamanho do vetor diagonal principal
    n = len(b)
    # Cria vetores vazios
    v = np.array([], float)
    w = np.array([], float)
    # Anexa o primeiro termo de 'a' ao vetor 'v' e o último termo de 'c' ao vetor 'w'
    v = np.append(v,a[0])
    w = np.append(w,c[n-1])
    # Itera para n-2 (dimSistema - 1)
    for t in range(1,n-2):
        v = np.append(v,0)
        w = np.append(w,0)
    # Anexa o penúltimo termo de 'c' ao vetor 'v' e o último termo de 'a' ao vetor 'w'
    v = np.append(v,c[n-2])
    w = np.append(w,a[n-1])
    # Resolve o sistema com a submatriz principal: Ty=d, Tz=v
    l, u = decompLUabc(np.delete(a,[0,n-1]),np.delete(b,n-1),np.delete(c,[n-1,n-2]))
    y = solveLydUxy(l,u,np.delete(c,[n-1,n-2]),np.delete(d,[n-1]))
    z = solveLydUxy(l,u,np.delete(c,[n-1,n-2]),v)
    # Encontra o último termo da solução X, em seguida os termos restantes
    x_n = (d[n-1]-c[n-1]*y[0]-a[n-1]*y[n-2])/(b[n-1]-c[n-1]*z[0]-a[n-1]*z[n-2])
    x = y - x_n*z
    x = np.append(x,x_n)
    x = np.array(x, float)
    return x

def solveLydUxy(l: np.ndarray, u: np.ndarray, c: np.ndarray, d: np.ndarray) -> np.ndarray:
    '''Resolve um sistema LUx=d a partir dos vetores subdiagonal da matriz inferior, diagonal e sobrediagonal da matriz superior, de termos independentes e retorna a solução para: Ly=d, Ux=y

    Parâmetros
    ---
    `l`: ndarray
        Vetor subdiagonal da matriz inferior
    `u`: ndarray
        Vetor diagonal da matriz superior
    `c`: ndarray
        Vetor sobrediagonal da matriz superior
    `d`: ndarray
        Vetor de termos independentes

    Retorna
    ---
    `x`: ndarray
        Vetor de soluções do sistema
    '''
    
    # Guarda o tamanho do sistema
    n = len(d)
    # Cria um vetor 'y' com zero em todas as posições
    y = np.zeros(n)
    # Primeiro termo de 'y'
    y[0] = d[0]
    # Itera para o tamanho do sistema; expressão do exercício
    for i in range(1,n):
        y[i] = d[i] - l[i-1]*y[i-1]
    # Cria um vetor 'x' com zero em todas as posições
    x = np.zeros(n)
    # Último termo de 'x'
    x[n-1] = y[n-1]/u[n-1]
    # Itera para o tamanho do sistema, do último para o primeiro termo; Expressão do exercício
    for i in range(n-2,-1,-1):
        x[i] = (y[i] - c[i]*x[i+1])/u[i]
    return x

def solveTridi(a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray) -> np.ndarray:
    '''Resolve um sistema linear tridiagonal Ax = d a partir dos vetores diagonais e de termos independentes, utilizando uma decomposição A = LU e resolvendo para: Ly = d, Ux = y

    Parâmetros
    ---
    `a`: ndarray
        Vetor contendo a subdiagonal dos coeficientes de X
    `b`: ndarray
        Vetor contendo a diagonal dos coeficientes de X
    `c`: ndarray
        Vetor contendo a sobrediagonal dos coeficientes de X
    `d`: ndarray
        Vetor dos coeficientes independentes do sistema

    Retorna
    ---
    `x`: ndarray
        Vetor de soluções para X do sistema
    '''    
    
    l, u = decompLUabc(a,b,c)
    return solveLydUxy(l,u,c,d)

# Funções de cálculo do exercício-programa 2
def gaussIntegrate(f, a, b, n: int) -> float:
    '''Integra uma função `f(x)` no intervalo `x = [a,b]` usando fórmulas de Gauss com `n` nós

    Parâmetros
    ---
    `f`: function
        Função de x a ser integrada
    `a`: float or callable
        Limite inferior de integração
    `b`: float or callable
        Limite superior de integração
    `n`: int
        Número de nós a ser usado

    Retorna
    ---
    `F`: 
        Integral calculada
    '''    
    
    if n == 6:
        x = np.array([0.2386191860831969086305017,0.6612093864662645136613996,0.9324695142031520278123016],dtype=float)
        w = np.array([0.4679139345726910473898703,0.3607615730481386075698335,0.1713244923791703450402961],dtype=float)
    elif n == 8:
        x = np.array([0.1834346424956498049394761,0.5255324099163289858177390,0.7966664774136267395915539,0.9602898564975362316835609],dtype=float)
        w = np.array([0.3626837833783619829651504,0.3137066458778872873379622,0.2223810344533744705443560,0.1012285362903762591525314],dtype=float)
    elif n == 10:
        x = np.array([0.1488743389816312108848260,0.4333953941292471907992659,0.6794095682990244062343274,0.8650633666889845107320967,0.9739065285171717200779640],dtype=float)
        w = np.array([0.2955242247147528701738930,0.2692667193099963550912269,0.2190863625159820439955349,0.1494513491505805931457763,0.0666713443086881375935688],dtype=float)

    # Guarda novos vetores com valores negativos das abscissas
    x = np.append(np.flip(x),-x)
    w = np.append(np.flip(w),w)

    # Transportando linearmente para os limites desejados, [-1,1] para [a,b]:
    # # x = (b-a)*t/2 + (b+a)/2
    # # dx = (b-a)/2 dt
    # # Mudança de variável de x para t
    # # int[a,b](f(x))dx = int[-1,1](f(((b-a)/2)*t+((b+a)/2))*((b-a)/2))dt = (b-a)/2)*int[-1,1](f(((b-a)/2))*t+((b+a)/2))))dt = ((b-a)/2))*sum[i,n](w[i]*f(((b-a)/2))*x[i]+(b+a)/2)))

    x = ((b-a)/2)*x + ((b+a)/2)
    soma = np.sum(np.multiply(w,f(x))) # Somatória dos w[i]*f(x[i]) termos, i de 0 até n
    return ((b-a)/2)*soma

def gaussDoubleIntegrate(f, a, b, c, d, n: int,) -> float:
    '''Calcula a integral dupla de uma função `f(x,y)` no intervalo `x = [a,b], y = [c(x),d(x)]` usando fórmulas de Gauss com `n` nós.


    Parâmetros
    ---
    `f`: function
        Função de x,y a ser integrada
    `a`: float
        Limite inferior de integração em x
    `b`: float
        Limite superior de integração em x
    `c`: float or callable
        Limite inferior de integração em y; pode ser uma função de x
    `d`: float or callable
        Limite superior de integração em y; pode ser uma função de x
    `n`: int
        Número de nós a ser usado

    Retorna
    ---
    `I`: 
        Integral dupla calculada
    '''

    if n == 6:
        x = np.array([0.2386191860831969086305017,0.6612093864662645136613996,0.9324695142031520278123016],dtype=float)
        w = np.array([0.4679139345726910473898703,0.3607615730481386075698335,0.1713244923791703450402961],dtype=float)
    elif n == 8:
        x = np.array([0.1834346424956498049394761,0.5255324099163289858177390,0.7966664774136267395915539,0.9602898564975362316835609],dtype=float)
        w = np.array([0.3626837833783619829651504,0.3137066458778872873379622,0.2223810344533744705443560,0.1012285362903762591525314],dtype=float)
    elif n == 10:
        x = np.array([0.1488743389816312108848260,0.4333953941292471907992659,0.6794095682990244062343274,0.8650633666889845107320967,0.9739065285171717200779640],dtype=float)
        w = np.array([0.2955242247147528701738930,0.2692667193099963550912269,0.2190863625159820439955349,0.1494513491505805931457763,0.0666713443086881375935688],dtype=float)

    # Guarda novos vetores com valores negativos das abscissas
    x = np.append(np.flik(x),-x)
    w = np.append(np.flip(w),w)
    
    x = ((b-a)/2)*x + ((b+a)/2)         # Cria um novo vetor x2 para contrair e transportar os limites de integração em y
    C = c(x) if callable(c) else c      # Vetor dos valores mínimos
    D = d(x) if callable(d) else d      # Vetor dos valores máximos
    soma = 0
    for i in range(n):                                  # Itera para o número de nós
        inf = C[i] if hasattr(C, "__len__") else C      # Garante que o limite inferior seja um valor e não um vetor
        sup = D[i] if hasattr(D, "__len__") else D      # Garante que o limite superior seja um valor e não um vetor
        soma += gaussIntegrate(lambda y: f(x[i],y),inf,sup,n)*w[i]  # Integra para cada valor de x[i], pondera e adiciona à `soma`
    return soma*(b-a)/2

def solveElemFinitos(f, n: int, l: float = 1, q = lambda x: 0, k = lambda x: 1) -> 'tuple[np.ndarray, np.ndarray]':
    '''Resolve uma equação do tipo `L(u(x)) := (-k(x)u'(x))' + q(x)u(x) = f(x)`, para `x em [0,1]`, com `u(0) = u(1) = 0`, em `n` nós uniformemente espaçados.


    Parâmetros
    ---
    `f`: function
        Função `f(x)` da equação
    `n`: int
        Número de nós a ser usado
    `l`: int
        Tamanho do intervalo em metros, vale `1` por padrão se não declarado
    `q`: function
        Função `q(x)` da equação, vale `0` por padrão se não declarado
    `k`: function
        Função `q(x)` da equação, valor `1` por padrão se não declarado

    Retorna
    ---
    tuple [
        `xi`: ndarray
            Vetor dos valores das abscissas dos nós
        `u`: ndarray
            Vetor de soluções `u(x)` para cada `x[i]`, exceto nas extremidades
    ]
    '''

    h = l/(n+1)                                         # Calcula valor de h
    xi = np.array([i*h for i in range(n+2)], float)     # Calcula o valor das abcissas dos nós
    
    # Calcula os produtos internos de f com cada função chapéu, e entre as funções chapéu, utilizando função de integração numérica do EP2
    Q1, Q2, Q3, Q4, Q5, Q6 = (np.array([], float) for _ in range(6))    # Cria listas para receber os valores
    for i in range(1, n+1):
        if(i<n):
            Q1 = np.append(Q1,gaussIntegrate(lambda x: ((xi[i+1]-x)/h)*((x-xi[i])/h)*q(x),xi[i],xi[i+1],10))
        Q2 = np.append(Q2,gaussIntegrate(lambda x: (((x-xi[i-1])/h)**2)*q(x),xi[i-1],xi[i],10))
        Q3 = np.append(Q3,gaussIntegrate(lambda x: (((xi[i+1]-x)/h)**2)*q(x),xi[i],xi[i+1],10))
        Q4 = np.append(Q4,gaussIntegrate(lambda x: (1/h)*(1/h)*k(x),xi[i-1],xi[i],10))
        if(i==n+1):
            Q4 = np.append(Q4,gaussIntegrate(lambda x: (1/h)*(1/h)*k(x),xi[i],xi[i+1],10))
        Q5 = np.append(Q5,gaussIntegrate(lambda x: ((x-xi[i-1])/h)*(f(x)),xi[i-1],xi[i],10))
        Q6 = np.append(Q6,gaussIntegrate(lambda x: ((xi[i+1]-x)/h)*(f(x)),xi[i],xi[i+1],10))
    print(Q4)

    
    # Monta o sistema matricial referente à equação (8) do enunciado do exercício, da forma A*x = d
    diagonal, sobrediagonal, subdiagonal, independentes = (np.array([], float) for _ in range(4))
    diagonal = np.append(diagonal, Q4[0]+Q4[1]+Q2[0]+Q3[0])
    sobrediagonal = np.append(sobrediagonal, -Q4[1]+Q1[0])
    independentes = np.append(independentes, Q5[0]+Q6[0])
    for i in range(1, n-1):
        diagonal = np.append(diagonal, Q4[i]+Q4[i+1]+Q2[i]+Q3[i])
        sobrediagonal = np.append(sobrediagonal, -Q4[i+1]+Q1[i])
        subdiagonal = np.append(subdiagonal, -Q4[i]+Q1[i-1])
        independentes = np.append(independentes, Q5[i]+Q6[i])
    diagonal = np.append(diagonal, Q4[n-2]+Q4[n-1]+Q2[n-1]+Q3[n-1])
    subdiagonal = np.append(subdiagonal, -Q4[n-1]+Q1[n-2])
    independentes = np.append(independentes, Q5[n-1]+Q6[n-1])
    # print(abc2A(subdiagonal,diagonal,sobrediagonal))
    # Resolve o sistema tridiagonal utilizando função do EP1
    return xi, solveTridi(subdiagonal,diagonal,sobrediagonal,independentes)
