#!/usr/bin/env python
# Universidade de São Paulo
## Instituto de Matemática e Estatística - Departamento de Matemática Aplicada
## Escola Politécnica
# MAP3121 - Métodos Numéricos e Aplicações - 2022.1
## Exercício-programa 01: Executável principal
# Autoria
## Bruno Prasinos Bernal
## Luciano Chaparin Luisi


import numpy as np
# Módulo próprio contendo funções customizadas para o EP
import custom_functions as cf
# Usado para selecionar arquivos .csv a partir do explorador
import tkinter
from tkinter import filedialog
# from math import cos, pi
# import matplotlib.pyplot as plt
# import sys, time, datetime, os

def main():
    # Abre um laço e um nível de menu
    while True:
        # Cria um menu de opções como dict
        options = {
            1: 'Decomposição LU de matriz',
            2: 'Resolução de sistema tridiagonal usando decomposição LU de matriz',
            3: 'Resolução de sistema tridiagonal cíclico'
            }
        # Imprime o menu e retorna um dict com as opções
        options = cf.printMenu(options=options, name="MENU PRINCIPAL")
        try: choice = int(input("Escolha a ação desejada (1 a %i): "%(len(options))))                                           # Recebe do usuário uma ação do menu (int)
        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")                                    # Imprime mensagem de erro
        else:
            try: options[choice]                                                                                                # Verifica se a opção é válida
            except KeyError: print("Opção não disponível. Escolha a ação desejada do menu abaixo: ")                            # Imprime mensagem de erro
            else:
                print("Opção escolhida: %s"%(options[choice]))                                                                  # Imprime a descrição da ação escolhida
                if(choice == 1):                                                                                                # Se escolheu decomp LU
                    while True:                                                                                                 # Abre um laço e um nível de menu
                        options = {                                                                                             # Cria um menu de opções como dict
                            1: 'Digitar elementos um a um',
                            2: 'Escolher de um arquivo .CSV',
                            3: 'Voltar'
                            }
                        options = cf.printMenu(options=options, name="DECOMP LU - MÉTODO DE ENTRADA")                           # Imprime o menu e retorna um dict com as opções
                        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))                      # Recebe do usuário uma ação do menu (int)
                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")                    # Imprime mensagem de erro
                        else:
                            try: options[choice]                                                                                # Verifica se a opção é válida
                            except KeyError: print("Opção não disponível. Escolha um método do menu abaixo: ")                  # Imprime mensagem de erro
                            else:
                                print("Opção escolhida: %s"%(options[choice]))                                                  # Imprime a descrição da ação escolhida
                                if(choice == 1):                                                                                # Se escolheu entrada manual
                                    A = cf.recebeMatriz()                                                                       # Roda função para receber os valores um a um
                                elif(choice == 2):                                                                              # Se escolheu entrada por arquivo
                                    while True:
                                        root = tkinter.Tk()
                                        root.withdraw()
                                        root.wm_attributes('-topmost', True)
                                        root.filename = filedialog.askopenfilename(title='Escolher matriz A para decomposição LU')
                                        try: root.filename
                                        except (OSError,FileNotFoundError): print("Nenhum arquivo selecionado. Abordando ação e retornando ao menu.")
                                        else:
                                            if root.filename == '':
                                                print("Nenhum arquivo selecionado. Abordando ação e retornando ao menu.")
                                            else:
                                                A = np.genfromtxt(root.filename, delimiter=',')                                 # Importa os valores do csv para um ndarray
                                        finally:
                                            break
                                elif(choice == 3):                                                                              # Se escolheu voltar ao menu
                                    break                                                                                       # Quebra o laço e volta ao menu anterior
                                else:                                                                                           # Se escolheu encerrar o programa
                                    return                                                                                      # Encerra o programa
                                try: A                                                                                          # Verifica se a variável foi definida
                                except NameError: pass
                                else:
                                    L, U = cf.decompLU(A)                                                                       # Executa script de decomposição LU
                                    print("Matriz A:")                                                                          # Imprime a matriz 'A' que foi inserida pelo usuário
                                    print(A)                                                                                    # Imprime a matriz 'A' que foi inserida pelo usuário
                                    print("Matriz inferior L:")                                                                 # Imprime a matriz 'L' calculada
                                    print(L)
                                    print("Matriz superior U:")                                                                 # Imprime a matriz 'U' calculada
                                    print(U)
                                    break                                                                                       # Quebra o laço e volta ao menu anterior
                elif(choice == 2):                                                                                              # Se escolheu sistema tridiagonal
                    while True:                                                                                                 # Abre um laço e um nível de menu
                        options = {                                                                                             # Cria um menu de opções como dict
                            1: 'Inserir matriz tridiagonal \'A\' e vetor \'d\' (Ax=d)',
                            2: 'Inserir os vetores \'a,b,c,d\' (Ax=d)',
                            3: 'Voltar'
                            }
                        options = cf.printMenu(options=options, name="SIS TRIDI - MÉTODO DE ENTRADA")                           # Imprime o menu e retorna um dict com as opções
                        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))                      # Recebe do usuário uma ação do menu
                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")                    # Imprime mensagem de erro
                        else:
                            try: options[choice]                                                                                # Verifica se a opção é válida
                            except KeyError: print("Opção não disponível. Escolha um método do menu abaixo: ")                  # Imprime mensagem de erro
                            else:                                                                                               # Se for válida
                                print("Opção escolhida: %s"%(options[choice]))                                                  # Imprime a descrição da ação escolhida
                                if(choice == 1):                                                                                # Se escolheu matriz de coeficientes
                                    while True:
                                        options = {                                                                             # Cria um menu de opções como dict
                                            1: 'Digitar matriz \'A\' e vetor \'d\' elementos um a um',
                                            2: 'Escolher de um arquivo .CSV',
                                            3: 'Voltar'
                                            }
                                        options = cf.printMenu(options=options, name="SIS TRIDI - MATRIZ A E VETOR D - MÉTODO DE ENTRADA")  # Imprime o menu e retorna um dict com as opções
                                        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))      # Recebe do usuário uma ação do menu
                                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")    # Imprime mensagem de erro
                                        else:
                                            try: options[choice]                                                                # Verifica se a opção é válida
                                            except KeyError: print("Opção não disponível. Escolha um método do menu abaixo: ")  # Imprime mensagem de erro
                                            else:                                                                               # Se for válida
                                                print("Opção escolhida: %s"%(options[choice]))                                  # Imprime a descrição da ação escolhida
                                                if(choice == 1):                                                                # Se escolheu entrada manual
                                                    A = cf.recebeMatriz()                                                       # Roda função para receber os valores um a um
                                                    d = cf.recebeVetor(tamanho=len(A),nome_vetor='d')
                                                elif(choice == 2):                                                              # Se escolheu entrada por arquivo
                                                    while True:
                                                        root = tkinter.Tk()
                                                        root.withdraw()
                                                        root.wm_attributes('-topmost', True)
                                                        root.filename = filedialog.askopenfilename(title='Escolher matriz \'A\' tridiagonal')
                                                        try: root.filename
                                                        except (OSError,FileNotFoundError): print("Nenhum arquivo selecionado. Abordando ação e retornando ao menu.")
                                                        else:
                                                            if root.filename == '':
                                                                print("Nenhum arquivo selecionado. Abordando ação e retornando ao menu.")
                                                            else:
                                                                A = np.genfromtxt(root.filename, delimiter=',')                 # Importa os valores do csv para um ndarray
                                                                while True:
                                                                    root = tkinter.Tk()
                                                                    root.withdraw()
                                                                    root.wm_attributes('-topmost', True)
                                                                    root.filename = filedialog.askopenfilename(title='Escolher vetor \'d\' termos independentes (Ax=d)')
                                                                    try: root.filename
                                                                    except (OSError,FileNotFoundError): print("Nenhum arquivo selecionado. Abordando ação e retornando ao menu.")
                                                                    else:
                                                                        if root.filename == '':
                                                                            print("Nenhum arquivo selecionado. Abordando ação e retornando ao menu.")
                                                                        else:
                                                                            d = np.genfromtxt(root.filename, delimiter=',')     # Importa os valores do csv para um ndarray
                                                                    finally:
                                                                        break
                                                        finally:
                                                            break
                                                elif(choice == 3):                                                              # Se escolheu voltar ao menu
                                                    break                                                                       # Quebra o laço e volta ao menu anterior
                                                else:                                                                           # Se escolheu encerrar o programa
                                                    return                                                                      # Encerra o programa
                                                try: A
                                                except NameError: pass
                                                else:
                                                    a,b,c = cf.A2abc(A)
                                                    break                                                                       # Quebra o laço e volta ao menu anterior
                                elif(choice == 2):                                                                              # Se escolheu vetores diagonais
                                    while True:
                                        options = {                                                                             # Cria um menu de opções como dict
                                            1: 'Digitar os vetores \'a,b,c,d\' elementos um a um',
                                            2: 'Escolher de um arquivo .CSV (um vetor por linha)',
                                            3: 'Voltar'
                                            }
                                        options = cf.printMenu(options=options, name="SIS TRIDI - VETORES - MÉTODO DE ENTRADA") # Imprime o menu e retorna um dict com as opções
                                        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))      # Recebe do usuário uma ação do menu (int)
                                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")    # Imprime mensagem de erro
                                        else:
                                            try: options[choice]                                                                # Verifica se a opção é válida
                                            except KeyError: print("Opção não disponível. Escolha um método do menu abaixo: ")  # Imprime mensagem de erro
                                            else:                                                                               # Se for válida
                                                print("Opção escolhida: %s"%(options[choice]))                                  # Imprime a descrição da ação escolhida
                                                if(choice == 1):                                                                # Se escolheu entrada manual
                                                    while True:
                                                        try: n = int(input("Digite a dimensão n (>2) do sistema: "))            # Roda função para receber os valores um a um
                                                        except ValueError: print("Inserção inválida.")
                                                        else:
                                                            if n < 3:
                                                                print("Dimensão inválida.")
                                                            else:
                                                                print("Insira o vetor subdiagonal \'a\'(dim=%i), sem o primeiro elemento nulo: "%(n-1))
                                                                a = cf.recebeVetor(tamanho=(n-1),nome_vetor='a')
                                                                print("Insira o vetor diagonal \'b\'(dim=%i): "%n)
                                                                b = cf.recebeVetor(tamanho=n,nome_vetor='b')
                                                                print("Insira o vetor sobrediagonal \'c\'(dim=%i), sem o último elemento nulo: "%(n-1))
                                                                c = cf.recebeVetor(tamanho=(n-1),nome_vetor='c')
                                                                print("Insira o vetor de independentes\'d\'(dim=%i): "%n)
                                                                d = cf.recebeVetor(tamanho=n,nome_vetor='d')
                                                                break
                                                elif(choice == 2):                                                              # Se escolheu entrada por arquivo
                                                    while True:
                                                        root = tkinter.Tk()
                                                        root.withdraw()
                                                        root.wm_attributes('-topmost', True)
                                                        root.filename = filedialog.askopenfilename(title='Escolher sistema tridiagonal')
                                                        try: root.filename
                                                        except (OSError,FileNotFoundError): print("Nenhum arquivo selecionado. Abordando ação e retornando ao menu.")
                                                        else:
                                                            if root.filename == '':
                                                                print("Nenhum arquivo selecionado. Abordando ação e retornando ao menu.")
                                                            else:
                                                                a = np.genfromtxt(root.filename, delimiter=',')[0]              # Importa os valores do csv para um ndarray
                                                                b = np.genfromtxt(root.filename, delimiter=',')[1]              # Importa os valores do csv para um ndarray
                                                                c = np.genfromtxt(root.filename, delimiter=',')[2]              # Importa os valores do csv para um ndarray
                                                                if len(a) == len(b):
                                                                    a = np.delete(a,0)
                                                                if len(c) == len(b):
                                                                    c = np.delete(c,-1)
                                                                d = np.genfromtxt(root.filename, delimiter=',')[3]              # Importa os valores do csv para um ndarray
                                                        finally:
                                                            break
                                                elif(choice == 3):                                                              # Se escolheu voltar ao menu
                                                    break                                                                       # Quebra o laço e volta ao menu anterior
                                                else:                                                                           # Se escolheu encerrar o programa
                                                    return                                                                      # Encerra o programa
                                                try: (a,b,c,d)
                                                except NameError: pass
                                                else:
                                                    break                                                                       # Quebra o laço
                                elif(choice == 3):                                                                              # Se escolheu voltar ao menu
                                    break                                                                                       # Quebra o laço e volta ao menu anterior
                                else:                                                                                           # Se escolheu encerrar o programa
                                    return                                                                                      # Encerra o programa
                                break                                                                                           # Quebra o laço e volta ao menu anterior
                    x = cf.solveTridi(a,b,c,d)                                                                                  # Executa script de resolução de sistema tridiagonal e guarda resultado em 'x'
                    print('Matriz A:')                                                                                          # Imprime a matriz A ao usuário
                    print(cf.abc2A(a,b,c))                                                                                      # Imprime a matriz A ao usuário
                    print('Vetor d:')                                                                                           # Imprime o vetor d ao usuário
                    print(d)                                                                                                    # Imprime o vetor d ao usuário
                    print('Solução X:')                                                                                         # Imprime o resultado ao usuário
                    print(x)                                                                                                    # Imprime o resultado ao usuário
                elif(choice == 3):                                                                                              # Se escolheu sistema tridiagonal cíclico
                    while True:                                                                                                 # Abre um laço e um nível de menu
                        options = {                                                                                             # Cria um menu de opções como dict
                            1: 'Inserir matriz tridiagonal cíclica \'A\' e vetor \'d\' (Ax=d)',
                            2: 'Inserir os vetores \'a,b,c,d\' (Ax=d)',
                            3: 'Testar modelo do exercício-programa',
                            4: 'Voltar'
                            }
                        options = cf.printMenu(options=options, name="SIS TRIDI CIC - MÉTODO DE ENTRADA")                       # Imprime o menu e retorna um dict com as opções
                        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))                      # Recebe do usuário uma ação do menu (int)
                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")                    # Imprime mensagem de erro
                        else:
                            try: options[choice]                                                                                # Verifica se a opção é válida
                            except KeyError: print("Opção não disponível. Escolha um método do menu abaixo: ")                  # Imprime mensagem de erro
                            else:                                                                                               # Se for válida
                                print("Opção escolhida: %s"%(options[choice]))                                                  # Imprime a descrição da ação escolhida
                                if(choice == 1):                                                                                # Se escolheu matriz de coeficientes
                                    while True:
                                        options = {                                                                             # Cria um menu de opções como dict
                                            1: 'Digitar matriz \'A\' e o vetor \'d\' elementos um a um',
                                            2: 'Escolher de um arquivo .CSV',
                                            3: 'Voltar'
                                            }
                                        options = cf.printMenu(options=options, name="SIS TRIDI CIC - MATRIZ A E VETOR D - MÉTODO DE ENTRADA")  # Imprime o menu e retorna um dict com as opções
                                        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))      # Recebe do usuário uma ação do menu (int)
                                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")    # Imprime mensagem de erro
                                        else:
                                            try: options[choice]                                                                # Verifica se a opção é válida
                                            except KeyError: print("Opção não disponível. Escolha um método do menu abaixo: ")  # Imprime mensagem de erro
                                            else:                                                                               # Se for válida
                                                print("Opção escolhida: %s"%(options[choice]))                                  # Imprime a descrição da ação escolhida
                                                if(choice == 1):                                                                # Se escolheu entrada manual
                                                    A = cf.recebeMatriz()                                                       # Roda função para receber os valores um a um
                                                    d = cf.recebeVetor(tamanho=len(A),nome_vetor='d')
                                                elif(choice == 2):                                                              # Se escolheu entrada por arquivo
                                                    while True:
                                                        root = tkinter.Tk()
                                                        root.withdraw()
                                                        root.wm_attributes('-topmost', True)
                                                        root.filename = filedialog.askopenfilename(title='Escolher matriz A tridiagonal cíclica')
                                                        try: root.filename
                                                        except (OSError,FileNotFoundError): print("Nenhum arquivo selecionado. Abordando ação e retornando ao menu.")
                                                        else:
                                                            if root.filename == '':
                                                                print("Nenhum arquivo selecionado. Abordando ação e retornando ao menu.")
                                                            else:
                                                                A = np.genfromtxt(root.filename, delimiter=',')                 # Importa os valores do csv para um ndarray
                                                                while True:
                                                                    root = tkinter.Tk()
                                                                    root.withdraw()
                                                                    root.wm_attributes('-topmost', True)
                                                                    root.filename = filedialog.askopenfilename(title='Escolher vetor \'d\' termos independentes (Ax=d)')
                                                                    try: root.filename
                                                                    except (OSError,FileNotFoundError): print("Nenhum arquivo selecionado. Abordando ação e retornando ao menu.")
                                                                    else:
                                                                        if root.filename == '':
                                                                            print("Nenhum arquivo selecionado. Abordando ação e retornando ao menu.")
                                                                        else:
                                                                            d = np.genfromtxt(root.filename, delimiter=',')     # Importa os valores do csv para um ndarray
                                                                    finally:
                                                                        break
                                                        finally:
                                                            break
                                                elif(choice == 3):                                                              # Se escolheu voltar ao menu
                                                    break                                                                       # Quebra o laço e volta ao menu anterior
                                                else:                                                                           # Se escolheu encerrar o programa
                                                    return                                                                      # Encerra o programa
                                                try: (A,d)
                                                except NameError: pass
                                                else:
                                                    a, b, c = cf.cycA2abc(A)
                                                    break                                                                       # Quebra o laço e volta ao menu anterior
                                elif(choice == 2):                                                                              # Se escolheu vetores diagonais
                                    while True:
                                        options = {                                                                             # Cria um menu de opções como dict
                                            1: 'Digitar os vetores \'a,b,c,d\' elementos um a um',
                                            2: 'Escolher de um arquivo .CSV (um vetor por linha)',
                                            3: 'Voltar'
                                            }
                                        options = cf.printMenu(options=options, name="SIS TRIDI CIC - VETORES - MÉTODO DE ENTRADA") # Imprime o menu e retorna um dict com as opções
                                        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))      # Recebe do usuário uma ação do menu (int)
                                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")    # Imprime mensagem de erro
                                        else:
                                            try: options[choice]                                                                # Verifica se a opção é válida
                                            except KeyError: print("Opção não disponível. Escolha um método do menu abaixo: ")  # Imprime mensagem de erro
                                            else:                                                                               # Se for válida
                                                print("Opção escolhida: %s"%(options[choice]))                                  # Imprime a descrição da ação escolhida
                                                if(choice == 1):                                                                # Se escolheu entrada manual
                                                    while True:
                                                        try: n = int(input("Digite a dimensão n (>2) do sistema cíclico: "))    # Roda função para receber os valores um a um
                                                        except ValueError: print("Inserção inválida.")
                                                        else:
                                                            if n < 3:
                                                                print("Dimensão inválida.")
                                                            else:
                                                                print("Insira o vetor subdiagonal \'a\'(dim=%i): "%n)
                                                                a = cf.recebeVetor(tamanho=n,nome_vetor='a')
                                                                print("Insira o vetor diagonal \'b\'(dim=%i): "%n)
                                                                b = cf.recebeVetor(tamanho=n,nome_vetor='b')
                                                                print("Insira o vetor sobrediagonal \'c\'(dim=%i): "%n)
                                                                c = cf.recebeVetor(tamanho=n,nome_vetor='c')
                                                                print("Insira o vetor de independentes \'d\'(dim=%i): "%n)
                                                                d = cf.recebeVetor(tamanho=n,nome_vetor='d')
                                                                break
                                                elif(choice == 2):                                                              # Se escolheu entrada por arquivo
                                                    while True:
                                                        root = tkinter.Tk()
                                                        root.withdraw()
                                                        root.wm_attributes('-topmost', True)
                                                        root.filename = filedialog.askopenfilename(title='Escolher sistema tridiagonal')
                                                        try: root.filename
                                                        except (OSError,FileNotFoundError): print("Nenhum arquivo selecionado. Abordando ação e retornando ao menu.")
                                                        else:
                                                            if root.filename == '':
                                                                print("Nenhum arquivo selecionado. Abordando ação e retornando ao menu.")
                                                            else:
                                                                a = np.genfromtxt(root.filename, delimiter=',')[0]              # Importa os valores do csv para um ndarray
                                                                b = np.genfromtxt(root.filename, delimiter=',')[1]              # Importa os valores do csv para um ndarray
                                                                c = np.genfromtxt(root.filename, delimiter=',')[2]              # Importa os valores do csv para um ndarray
                                                                d = np.genfromtxt(root.filename, delimiter=',')[3]              # Importa os valores do csv para um ndarray
                                                        finally:
                                                            break
                                                elif(choice == 3):                                                              # Se escolheu voltar ao menu
                                                    break                                                                       # Quebra o laço e volta ao menu anterior
                                                else:                                                                           # Se escolheu encerrar o programa
                                                    return                                                                      # Encerra o programa
                                                try: (a,b,c,d)
                                                except NameError: pass
                                                else:
                                                    break                                                                       # Quebra o laço
                                elif(choice == 3):                                                                              # Se escolheu modelo de sistema
                                    while True:
                                        try: n = int(input("Digite a dimensão n para gerar o sistema cíclico: "))               # Roda função para receber os valores um a um
                                        except ValueError: print("Inserção inválida.")
                                        else:
                                            if n == 0:
                                                print("Dimensão inválida.")
                                            else:
                                                a,b,c,d = cf.genSysMAP(n=n)                                                     # Gerar sistema e atribuir os valores aos vetores
                                                break
                                elif(choice == 4):                                                                              # Se escolheu voltar ao menu
                                    break                                                                                       # Quebra o laço e volta ao menu anterior
                                else:                                                                                           # Se escolheu encerrar o programa
                                    return                                                                                      # Encerra o programa
                                break                                                                                           # Quebra o laço e volta ao menu anterior
                    x = cf.solveCycTridi(a,b,c,d)                                                                               # Executa script de resolução de sistema tridiagonal e guarda resultado em 'x'
                    print('Matriz A:')                                                                                          # Imprime a matriz A do sistema
                    print(cf.abc2cycA(a,b,c))                                                                                   # Imprime a matriz A do sistema
                    print('Vetor d:')                                                                                           # Imprime o vetor d do sistema
                    print(d)                                                                                                    # Imprime o vetor d do sistema
                    print('Solução X:')                                                                                         # Imprime a solução X do sistema
                    print(x)                                                                                                    # Imprime a solução X do sistema
                else:                                                                                                           # Se o usuário escolheu sair
                    return                                                                                                      # Encerra o programa

main()