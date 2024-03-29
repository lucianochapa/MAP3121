#!/usr/bin/env python
# Universidade de São Paulo
## Instituto de Matemática e Estatística - Departamento de Matemática Aplicada
## Escola Politécnica
# MAP3121 - Métodos Numéricos e Aplicações - 2022.1
## Exercício-programa 02: Executável principal
# Autoria
## Bruno Prasinos Bernal
## Luciano Chaparin Luisi


import numpy as np
# Módulo próprio contendo funções customizadas para o EP
import custom_functions as cf

def main():
    # Abre um laço, imprime um menu e prompta o usuário a escolher uma opção
    while True:
        # Cria e imprime um menu de opções como dict
        options = {
            1: 'Exemplo 1 - Volume de poliedros',
            2: 'Exemplo 2 - Área limitada por funções',
            3: 'Exemplo 3 - Área de uma superfície e volume sob esta',
            4: 'Exemplo 4 - Volume de sólido de rotação'
            }
        options = cf.printMenu(options=options, name="MENU PRINCIPAL")  # Imprime o menu e retorna um dict com as opções
        try: choice = int(input("Escolha a ação desejada (1 a %i): "%(len(options))))   # Recebe do usuário uma ação do menu (int)
        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")    # Imprime mensagem de erro
        else:
            try: options[choice]    # Verifica se a opção é válida
            except KeyError: print("Opção não disponível. Escolha a ação desejada do menu abaixo: ")    # Imprime mensagem de erro
            else:
                print("Opção escolhida: %s"%(options[choice]))  # Imprime a descrição da ação escolhida
                # Se escolheu Exemplo 1
                if(choice == 1):
                    # Volume de um cubo de arestas 1
                    for n in range(6,11,2):     # Itera para (n=6, 8 e 10) nós
                        a = 0
                        b = 1
                        c = 0
                        d = 1
                        def f(x, y): return 1
                        I = cf.gaussDoubleIntegrate(f,a,b,c,d,n)
                        print("Volume de um cubo com arestas de comprimento 1")
                        print("(n=%i nós): Vol.cubo = %f"%(n,I))
                    # Volume de um tetraedro com vértices (0, 0, 0), (1, 0, 0), (0, 1, 0) e (0, 0, 1)
                    for n in range(6,11,2):     # Itera para (n=6, 8 e 10) nós
                        a = 0
                        b = 1
                        c = 0
                        d = lambda x: 1 - x
                        def f(x, y): return 1 - x - y
                        I = cf.gaussDoubleIntegrate(f,a,b,c,d,n)
                        print("Volume de um tetraedro com vértices (0,0,0), (1,0,0), (0,1,0) e (0,0,1)")
                        print("(n=%i nós): Vol.tetraedro = %f"%(n,I))
                # Se escolheu Exemplo 2
                elif(choice == 2):
                    # Integrar primeiro em y, depois em x
                    for n in range(6,11,2):     # Itera para (n=6, 8 e 10) nós
                        a = 0
                        b = 1
                        c = 0
                        d = lambda x: 1-x**2
                        def f(x, y): return 1
                        I = cf.gaussDoubleIntegrate(f,a,b,c,d,n)
                        print("Área A do primeiro quadrante entre os eixos e a curva y = 1-x²")
                        print("(n=%i nós): Área A (Idydx)= %f"%(n,I))
                    # Integrar primeiro em x, depois em y
                    for n in range(6,11,2):     # Itera para (n=6, 8 e 10) nós
                        a = 0
                        b = 1
                        c = 0
                        d = lambda y: (1-y)**(0.5)
                        def f(y, x): return 1
                        I = cf.gaussDoubleIntegrate(f,a,b,c,d,n)
                        print("Área A do primeiro quadrante entre os eixos e a curva x = (1-y)**0.5")
                        print("(n=%i nós): Área A (Idxdy)= %f"%(n,I))
                # Se escolheu Exemplo 3
                elif(choice == 3):
                    for n in range(6,11,2):     # Itera para (n=6, 8 e 10) nós
                        a = 0.1
                        b = 0.5
                        c = lambda x: x**3
                        d = lambda x: x**2
                        def f(x, y): return ((np.exp(y/x)*(-y/x**2))**2 + (np.exp(y/x)/x)**2 + 1)**0.5
                        I = cf.gaussDoubleIntegrate(f,a,b,c,d,n)
                        print("Área da superfície descrita por z = exp(y/x)")
                        print("(n=%i nós): Área A= %f"%(n,I))
                # Se escolheu Exemplo 4
                elif(choice == 4):
                    for n in range(6,11,2):     # Itera para (n=6, 8 e 10) nós
                        a = -1
                        b = 1
                        c = 0
                        d = lambda y: np.exp(-y**2)
                        def f(x, y): return (x**2 + y**2)**0.5
                        I = 2*np.pi*cf.gaussDoubleIntegrate(f,a,b,c,d,n)
                        print("Volume da calota esférica")
                        print("(n=%i nós): V= %f"%(n,I))
                # Se escolheu sair
                else:
                    return

main()