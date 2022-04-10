# Decomposição de matriz LU
def decompLU():
    n = int(input("Digite o tamanho n da matriz (n x n): "))
    a = []
    for i in range(0,n):
        linha = []
        print("Linha %i"%(i+1))
        for j in range(0,n):
            elem = int(input("A(%i,%i): "%(i+1,j+1)))
            linha.append(elem)
        print(67 * "-")
        a.append(linha)
    print("Matriz A: %a"%(a))
    # return

decompLU()