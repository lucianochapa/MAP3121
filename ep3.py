#!/usr/bin/env python
# Universidade de São Paulo
## Instituto de Matemática e Estatística - Departamento de Matemática Aplicada
## Escola Politécnica
# MAP3121 - Métodos Numéricos e Aplicações - 2022.1
## Exercício-programa 03: Executável principal
# Autoria
## Bruno Prasinos Bernal
## Luciano Chaparin Luisi


import numpy as np
# Módulo próprio contendo funções customizadas para o EP
import custom_functions as cf
# # Usado para selecionar arquivos .csv a partir do explorador
# import tkinter
# from tkinter import filedialog
# from math import cos, pi
import matplotlib.pyplot as plt
# import sys, time, datetime, os

def main():
    # Abre um laço, imprime um menu e prompta o usuário a escolher uma opção
    while True:
        options = {
            1: 'Teste 1 - Validação: Seção 4.2 do EP3',
            2: 'Teste 2 - Complemento Seção 4.2 do EP3',
            3: 'Teste 3 - Forçantes de calor: Seção 4.3 do EP3',
            4: 'Teste 4 - Ilustração Burden, Faires'
            }
        options = cf.printMenu(options=options, name="MENU PRINCIPAL")  # Imprime o menu e retorna um dict com as opções
        try: choice = int(input("Escolha a ação desejada (1 a %i): "%(len(options))))   # Recebe do usuário uma ação do menu (int)
        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")    # Imprime mensagem de erro
        else:
            try: options[choice]    # Verifica se a opção é válida
            except KeyError: print("Opção não disponível. Escolha a ação desejada do menu abaixo: ")    # Imprime mensagem de erro
            else:
                print("Opção escolhida: %s"%(options[choice]))  # Imprime a descrição da ação escolhida
                if(choice == 1):        # Teste/validação da Seção 4.2 do EP3
                    while True:
                        options = {
                            1: 'Usar parâmetros de valor padrão: q=0, k=1, L=1, T_ext=20, nós=[7,15,31,63]',
                            2: 'Escolher valores dos parâmetros: L, T_ext, e nós',
                            3: 'Voltar'
                            }
                        options = cf.printMenu(options=options, name="SEÇÃO 4.2 DO EP3")  # Imprime o menu e retorna um dict com as opções
                        try: choice = int(input("Escolha a ação desejada (1 a %i): "%(len(options))))   # Recebe do usuário uma ação do menu (int)
                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")    # Imprime mensagem de erro
                        else:
                            try: options[choice]    # Verifica se a opção é válida
                            except KeyError: print("Opção não disponível. Escolha a ação desejada do menu abaixo: ")    # Imprime mensagem de erro
                            else:
                                print("Opção escolhida: %s"%(options[choice]))  # Imprime a descrição da ação escolhida
                                if(choice == 1):
                                    L = 1                                   # Comprimento do chip, em metros
                                    T_ext = 20                              # Temperatura externa (x=0 e x=L), em Kelvin
                                    nos = [2**i -1 for i in range(3,7)]     # Gera nós 7, 15, 31 e 63
                                elif(choice == 2):
                                    L = float(input("Digite o valor de L (em metros): "))
                                    T_ext = float(input("Digite o valor de T_ext (em Kelvin): "))
                                    nos = []
                                    print("Digite os valores dos nós (vazio para finalizar):")
                                    while True:
                                        entrada = input("Nós=%s\n"%nos)
                                        if entrada == '':
                                            break
                                        nos.append(int(entrada))
                                    print("Valores escolhidos: L=%f, T_ext=%f, nós=%s"%(L,T_ext,nos))
                                elif(choice == 3):
                                    break
                                else:
                                    return
                                def f(x): return 12*x*(1-x)-2
                                def solucaoExata(x): return (x**2)*((1-x)**2)
                                store = {}
                                for n in nos:
                                    xi, u, u_bar = cf.solveElemFinitos(f,n,l=L,exata=solucaoExata)
                                    u += T_ext                                                      # Soma T_ext à função temperatura
                                    print("Para n=%i nós:" %(n))
                                    print("(%i nós) Abcissas: %s"%(n, xi))
                                    print("(%i nós) Vetor de soluções u(x): %s"%(n, u))
                                    u_bar += T_ext 
                                    print("(%i nós) Vetor de soluções exatas u_bar(x): %s"%(n, u_bar))
                                    dif = abs(u-u_bar)
                                    print("(%i nós) Vetor diferença absoluta u-u_bar(x): %s"%(n, dif))
                                    print("(%i nós) Erro máximo: %f"%(n, max(dif)))
                                    print(67 * "-")
                                    store[n]={'n':n, 'xi':xi,'u':u,'u_bar':u_bar, 'erro':max(dif)}
                                plotar = input("Deseja visualizar a curva dos resultados apresentados? (S/N): ")
                                if(plotar=="S" or plotar =="s"):
                                    for n in nos:
                                        plt.plot(store[n]['xi'],store[n]['u'], label='n=%i, erro=%f'%(n,store[n]['erro']))
                                    plt.plot(store[nos[-1]]['xi'],store[nos[-1]]['u_bar'], label='exata')
                                    plt.xlabel("Distância, x[m]")
                                    plt.ylabel("Temperatura, u[K]")
                                    plt.title("Validação da Seção 4.2")
                                    plt.legend()
                                    plt.show()
                                break
                elif(choice == 2):      # Teste/validação para o complemento da Seção 4.2 do EP3
                    while True:
                        options = {
                            1: 'Usar parâmetros de valor padrão: q=0, k=exp(x), L=1, T_ext=20, nós=[7,15,31,63]',
                            2: 'Escolher valores dos parâmetros: L, T_ext, e nós',
                            3: 'Voltar'
                            }
                        options = cf.printMenu(options=options, name="COMPLEMENTO DA SEÇÃO 4.2 DO EP3")  # Imprime o menu e retorna um dict com as opções
                        try: choice = int(input("Escolha a ação desejada (1 a %i): "%(len(options))))   # Recebe do usuário uma ação do menu (int)
                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")    # Imprime mensagem de erro
                        else:
                            try: options[choice]    # Verifica se a opção é válida
                            except KeyError: print("Opção não disponível. Escolha a ação desejada do menu abaixo: ")    # Imprime mensagem de erro
                            else:
                                print("Opção escolhida: %s"%(options[choice]))  # Imprime a descrição da ação escolhida
                                if(choice == 1):
                                    L = 1
                                    T_ext = 20
                                    nos = [2**i -1 for i in range(3,7)]
                                elif(choice == 2):
                                    L = float(input("Digite o valor de L (em metros): "))
                                    T_ext = float(input("Digite o valor de T_ext (em Kelvin): "))
                                    print("Digite os valores dos nós (vazio para finalizar):")
                                    while True:
                                        entrada = input("Nós=%s\n"%nos)
                                        if entrada == '':
                                            break
                                        nos.append(int(entrada))
                                    print("Valores escolhidos: L=%f, T_ext=%f, nós=%s"%(L,T_ext,nos))
                                elif(choice == 3):
                                    break
                                else:
                                    return
                                def f(x): return np.exp(x)+1
                                def k(x): return np.exp(x)
                                def solucaoExata(x): return (x-1)*(np.exp(-x)-1)
                                store = {}
                                for n in nos:
                                    xi, u, u_bar = cf.solveElemFinitos(f,n,l=L,k=k,exata=solucaoExata)
                                    u += T_ext
                                    print("Para n=%i nós:" %(n))
                                    print("(%i nós) Abcissas: %s"%(n, xi))
                                    print("(%i nós) Vetor de soluções u(x): %s"%(n, u))
                                    if(u_bar is not None):
                                        u_bar += T_ext 
                                        print("(%i nós) Vetor de soluções exatas u_bar(x): %s"%(n, u_bar))
                                        dif = abs(u-u_bar)
                                        print("(%i nós) Vetor diferença absoluta u-u_bar(x): %s"%(n, dif))
                                        print("(%i nós) Erro máximo: %f"%(n, max(dif)))
                                    print(67 * "-")
                                    store[n]={'n':n, 'xi':xi,'u':u,'u_bar':u_bar, 'erro':max(dif)}
                                plotar = input("Deseja visualizar a curva dos resultados apresentados? (S/N): ")
                                if(plotar=="S" or plotar =="s"):
                                    for n in nos:
                                        plt.plot(store[n]['xi'],store[n]['u'], label='n=%i, erro=%f'%(n,store[n]['erro']))
                                    plt.plot(store[nos[-1]]['xi'],store[nos[-1]]['u_bar'], label='exata')
                                    plt.xlabel("Distância, x[m]")
                                    plt.ylabel("Temperatura, u[K]")
                                    plt.title("Complemento da Seção 4.2")
                                    plt.legend()
                                    plt.show()
                                break
                elif(choice == 3):      # Teste equilíbrio com forçantes de calor
                    while True:
                        options = {
                            1: 'Usar parâmetros de valor padrão: q=0, k=3.6, Q0+=15000, Q0-=5000, sigma=0.001, theta=0.001, L=0.02, T_ext=20, nós=[7,15,31,63]',
                            2: 'Escolher valores dos parâmetros: Q0+, Q0-, sigma, theta, L, T_ext, e nós',
                            3: 'Voltar'
                            }
                        options = cf.printMenu(options=options, name="SEÇÃO 4.3 DO EP3")  # Imprime o menu e retorna um dict com as opções
                        try: choice = int(input("Escolha a ação desejada (1 a %i): "%(len(options))))   # Recebe do usuário uma ação do menu (int)
                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")    # Imprime mensagem de erro
                        else:
                            try: options[choice]    # Verifica se a opção é válida
                            except KeyError: print("Opção não disponível. Escolha a ação desejada do menu abaixo: ")    # Imprime mensagem de erro
                            else:
                                print("Opção escolhida: %s"%(options[choice]))  # Imprime a descrição da ação escolhida
                            if(choice == 1):
                                Q_zero_mais = 15000     # Constante de geração de calor, em W/m³
                                Q_zero_menos = 5000     # Constante de resfriamento, em W/m³
                                L = 0.02                # Comprimento total do bloco do chip, em metros
                                sigma = 0.001           # Concentração de distribuição de aquecimento, em metros
                                theta = 0.001           # Concentração de distribuição de resfriamento, em metros
                                T_ext = 20              # Temperatura externa, em Kelvin
                                nos = [2**i -1 for i in range(3,7)]
                            elif(choice == 2):
                                Q_zero_mais = float(input("Digite o valor de Q0+ (em W/m³): "))
                                Q_zero_menos = float(input("Digite o valor de Q0- (em W/m³): "))
                                sigma = float(input("Digite o valor de sigma (em metros): "))
                                theta = float(input("Digite o valor de theta (em metros): "))
                                L = float(input("Digite o valor de L (em metros): "))
                                T_ext = float(input("Digite o valor de T_ext (em Kelvin): "))
                                nos = []
                                print("Digite os valores dos nós (vazio para finalizar):")
                                while True:
                                    entrada = input("Nós=%s\n"%nos)
                                    if entrada == '':
                                        break
                                    nos.append(int(entrada))
                                print("Valores escolhidos: Q0+=%f, Q0-=%f, sigma=%f, theta=%f, L=%f, T_ext=%f, nós=%s"%(Q_zero_mais, Q_zero_menos, sigma, theta, L,T_ext,nos))
                            elif(choice == 3):
                                break
                            else:
                                return
                            def Qmais(x, sigma, Q_zero_mais): return Q_zero_mais*np.exp(-((x-(L/2))**2)/(sigma**2))
                            def Qmenos(x, theta, Q_zero_menos): return Q_zero_menos*(np.exp(-(x**2)/(theta**2)) + np.exp(-((x-L)**2)/(theta**2)))
                            def f(x, sigma, theta, Q_zero_mais, Q_zero_menos): return Qmais(x, sigma, Q_zero_mais) - Qmenos(x, theta, Q_zero_menos)
                            def k(x): return 3.6
                            store = {}
                            for n in nos:
                                xi, u, u_bar = cf.solveElemFinitos(lambda x: f(x, sigma, theta, Q_zero_mais, Q_zero_menos),n,l=L,k=k)
                                u += T_ext
                                print("Para n=%i nós:" %(n))
                                print("(%i nós) Abcissas: %s"%(n, xi))
                                print("(%i nós) Vetor de soluções u(x): %s"%(n, u))
                                print(67 * "-")
                                store[n]={'n':n, 'xi':xi,'u':u}
                            plotar = input("Deseja visualizar a curva dos resultados apresentados? (S/N): ")
                            if(plotar=="S" or plotar =="s"):
                                for n in nos:
                                    plt.plot(store[n]['xi'],store[n]['u'], label='n=%i'%(n))
                                plt.xlabel("Distância, x[m]")
                                plt.ylabel("Temperatura, u[K]")
                                plt.title("Equilíbrio com forçantes de calor")
                                plt.legend()
                                plt.show()
                            break
                elif(choice == 4):      # Teste/validação - BURDEN;FAIRES. Numerical Analysis, 10ed, cap.11, p.719-720, 2016.
                    while True:
                        options = {
                            1: 'Usar parâmetros de valor padrão: q=pi^2, k=1, nós=[9]',
                            2: 'Escolher valores dos parâmetros: nós',
                            3: 'Voltar'
                            }
                        options = cf.printMenu(options=options, name="ILUSTRAÇÃO BURDEN FAIRES CAP.11")  # Imprime o menu e retorna um dict com as opções
                        try: choice = int(input("Escolha a ação desejada (1 a %i): "%(len(options))))   # Recebe do usuário uma ação do menu (int)
                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")    # Imprime mensagem de erro
                        else:
                            try: options[choice]    # Verifica se a opção é válida
                            except KeyError: print("Opção não disponível. Escolha a ação desejada do menu abaixo: ")    # Imprime mensagem de erro
                            else:
                                print("Opção escolhida: %s"%(options[choice]))  # Imprime a descrição da ação escolhida
                                if(choice == 1):
                                    nos = [9]
                                elif(choice == 2):
                                    nos = []
                                    print("Digite os valores dos nós (vazio para finalizar):")
                                    while True:
                                        entrada = input("Nós=%s\n"%nos)
                                        if entrada == '':
                                            break
                                        nos.append(int(entrada))
                                    print("Valores escolhidos: nós=%s"%(nos))
                                elif(choice == 3):
                                    break
                                else:
                                    return
                                def f(x): return 2*(np.pi**2)*np.sin(np.pi*x)       # Livro Burden Faires
                                def q(x): return np.pi**2                           # Livro Burden Faires
                                def solucaoExata(x): return np.sin(np.pi*x)         # Livro Burden Faires
                                store = {}
                                for n in nos:
                                    xi, u, u_bar = cf.solveElemFinitos(f,n,q=q,exata=solucaoExata)
                                    print("Para n=%i nós:" %(n))
                                    print("(%i nós) Abcissas: %s"%(n, xi))
                                    print("(%i nós) Vetor de soluções u(x): %s"%(n, u))
                                    if(u_bar is not None):
                                        print("(%i nós) Vetor de soluções exatas u_bar(x): %s"%(n, u_bar))
                                        dif = abs(u-u_bar)
                                        print("(%i nós) Vetor diferença absoluta u-u_bar(x): %s"%(n, dif))
                                        print("(%i nós) Erro máximo: %f"%(n, max(dif)))
                                    print(67 * "-")
                                    store[n]={'n':n, 'xi':xi,'u':u,'u_bar':u_bar, 'erro':max(dif)}
                                plotar = input("Deseja visualizar a curva dos resultados apresentados? (S/N): ")
                                if(plotar=="S" or plotar =="s"):
                                    for n in nos:
                                        plt.plot(store[n]['xi'],store[n]['u'], label='n=%i, erro=%f'%(n,store[n]['erro']))
                                    plt.plot(store[nos[-1]]['xi'],store[nos[-1]]['u_bar'], label='exata')
                                    plt.xlabel("x")
                                    plt.ylabel("y")
                                    plt.title("Ilustração - Burden, Faires cap.11")
                                    plt.legend()
                                    plt.show()
                                break
                else:                   # Escolheu sair
                    return
main()