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
    # Abre um laço, imprime um menu e prompta o usuário a escolher uma opção
    while True:
        # Cria e imprime um menu de opções como dict
        options = {
            1: 'Decomposição LU de matriz',
            2: 'Resolução de sistema tridiagonal usando decomposição LU de matriz',
            3: 'Resolução de sistema tridiagonal cíclico'
            }
        options = cf.printMenu(options=options, name="MENU PRINCIPAL")  # Imprime o menu e retorna um dict com as opções
        try: choice = int(input("Escolha a ação desejada (1 a %i): "%(len(options))))   # Recebe do usuário uma ação do menu (int)
        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")    # Imprime mensagem de erro
        else:
            try: options[choice]    # Verifica se a opção é válida
            except KeyError: print("Opção não disponível. Escolha a ação desejada do menu abaixo: ")    # Imprime mensagem de erro
            else:
                print("Opção escolhida: %s"%(options[choice]))  # Imprime a descrição da ação escolhida
                # Se escolheu decomp LU
                if(choice == 1):
                    while True:
                        options = {
                            1: 'Digitar elementos um a um',
                            2: 'Escolher de um arquivo .CSV',
                            3: 'Voltar'
                            }
                        options = cf.printMenu(options=options, name="DECOMP LU - MÉTODO DE ENTRADA")
                        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))
                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")
                        else:
                            try: options[choice]
                            except KeyError: print("Opção não disponível. Escolha um método do menu abaixo: ")
                            else:
                                print("Opção escolhida: %s"%(options[choice]))
                                # Se escolheu digitar os elementos
                                if(choice == 1):
                                    A = cf.recebeMatriz()
                                # Se escolheu importar .csv
                                elif(choice == 2):
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
                                                A = np.genfromtxt(root.filename, delimiter=',')
                                        finally:
                                            break
                                # Se escolheu voltar
                                elif(choice == 3):
                                    break
                                # Se escolheu sair
                                else:
                                    return
                                try: A
                                except NameError: pass
                                else:
                                    break
                    L, U = cf.decompLU(A)
                    print("Decomposição A=LU")
                    print("Matriz A:")
                    print(A)
                    print("Matriz inferior L:")
                    print(L)
                    print("Matriz superior U:")
                    print(U)
                # Se escolheu sistema tridiagonal
                elif(choice == 2):
                    while True:
                        options = {
                            1: 'Inserir matriz tridiagonal \'A\' e vetor \'d\' (Ax=d)',
                            2: 'Inserir os vetores \'a,b,c,d\' (Ax=d)',
                            3: 'Voltar'
                            }
                        options = cf.printMenu(options=options, name="SIS TRIDI - MÉTODO DE ENTRADA")
                        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))
                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")
                        else:
                            try: options[choice]
                            except KeyError: print("Opção não disponível. Escolha um método do menu abaixo: ")
                            else:
                                print("Opção escolhida: %s"%(options[choice]))
                                # Se escolheu matriz A e vetor d
                                if(choice == 1):
                                    while True:
                                        options = {
                                            1: 'Digitar matriz \'A\' e vetor \'d\' elementos um a um',
                                            2: 'Escolher de um arquivo .CSV',
                                            3: 'Voltar'
                                            }
                                        options = cf.printMenu(options=options, name="SIS TRIDI - MATRIZ A E VETOR D - MÉTODO DE ENTRADA")
                                        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))
                                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")
                                        else:
                                            try: options[choice]
                                            except KeyError: print("Opção não disponível. Escolha um método do menu abaixo: ")
                                            else:
                                                print("Opção escolhida: %s"%(options[choice]))
                                                # Se escolheu digitar elementos
                                                if(choice == 1):
                                                    A = cf.recebeMatriz()
                                                    d = cf.recebeVetor(tamanho=len(A),nome_vetor='d')
                                                # Se escolheu importar .csv
                                                elif(choice == 2):
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
                                                                A = np.genfromtxt(root.filename, delimiter=',')
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
                                                                            d = np.genfromtxt(root.filename, delimiter=',')
                                                                    finally:
                                                                        break
                                                        finally:
                                                            break
                                                # Se escolheu voltar
                                                elif(choice == 3):
                                                    break
                                                # Se escolheu sair
                                                else:
                                                    return
                                                try: A
                                                except NameError: pass
                                                else:
                                                    a,b,c = cf.A2abc(A)
                                                    break
                                # Se escolheu vetores tridiagonais
                                elif(choice == 2):
                                    while True:
                                        options = {
                                            1: 'Digitar os vetores \'a,b,c,d\' elementos um a um',
                                            2: 'Escolher de um arquivo .CSV (um vetor por linha)',
                                            3: 'Voltar'
                                            }
                                        options = cf.printMenu(options=options, name="SIS TRIDI - VETORES - MÉTODO DE ENTRADA")
                                        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))
                                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")
                                        else:
                                            try: options[choice]
                                            except KeyError: print("Opção não disponível. Escolha um método do menu abaixo: ")
                                            else:
                                                print("Opção escolhida: %s"%(options[choice]))
                                                # Se escolheu digitar elementos
                                                if(choice == 1):
                                                    while True:
                                                        try: n = int(input("Digite a dimensão n (>2) do sistema: "))
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
                                                # Se escolheu importar .csv
                                                elif(choice == 2):
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
                                                                a = np.genfromtxt(root.filename, delimiter=',')[0]
                                                                b = np.genfromtxt(root.filename, delimiter=',')[1]
                                                                c = np.genfromtxt(root.filename, delimiter=',')[2]
                                                                if len(a) == len(b):
                                                                    a = np.delete(a,0)
                                                                if len(c) == len(b):
                                                                    c = np.delete(c,-1)
                                                                d = np.genfromtxt(root.filename, delimiter=',')[3]
                                                        finally:
                                                            break
                                                # Se escolheu voltar
                                                elif(choice == 3):
                                                    break
                                                # Se escolheu sair
                                                else:
                                                    return
                                                try: (a,b,c,d)
                                                except NameError: pass
                                                else:
                                                    break
                                # Se escolheu voltar
                                elif(choice == 3):
                                    break
                                # Se escolheu sair
                                else:
                                    return
                                break
                    x = cf.solveTridi(a,b,c,d)
                    print("Sistema Ax=d")
                    print('Matriz A:')
                    print(cf.abc2A(a,b,c))
                    print('Vetor d:')
                    print(d)
                    print('Solução X (valores encontrados):')
                    print(x)
                    np.set_printoptions(suppress=True)
                    print('Solução X (notação científica suprimida):')
                    print(x)
                    np.set_printoptions(suppress=False)
                # Se escolheu tridiagonal cíclico
                elif(choice == 3):
                    while True:
                        options = {
                            1: 'Inserir matriz tridiagonal cíclica \'A\' e vetor \'d\' (Ax=d)',
                            2: 'Inserir os vetores \'a,b,c,d\' (Ax=d)',
                            3: 'Testar modelo do exercício-programa',
                            4: 'Voltar'
                            }
                        options = cf.printMenu(options=options, name="SIS TRIDI CIC - MÉTODO DE ENTRADA")
                        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))
                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")
                        else:
                            try: options[choice]
                            except KeyError: print("Opção não disponível. Escolha um método do menu abaixo: ")
                            else:
                                print("Opção escolhida: %s"%(options[choice]))
                                if(choice == 1):
                                    while True:
                                        options = {
                                            1: 'Digitar matriz \'A\' e o vetor \'d\' elementos um a um',
                                            2: 'Escolher de um arquivo .CSV',
                                            3: 'Voltar'
                                            }
                                        options = cf.printMenu(options=options, name="SIS TRIDI CIC - MATRIZ A E VETOR D - MÉTODO DE ENTRADA")
                                        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))
                                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")
                                        else:
                                            try: options[choice]
                                            except KeyError: print("Opção não disponível. Escolha um método do menu abaixo: ")
                                            else:
                                                print("Opção escolhida: %s"%(options[choice]))
                                                if(choice == 1):
                                                    A = cf.recebeMatriz()
                                                    d = cf.recebeVetor(tamanho=len(A),nome_vetor='d')
                                                elif(choice == 2):
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
                                                                A = np.genfromtxt(root.filename, delimiter=',')
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
                                                                            d = np.genfromtxt(root.filename, delimiter=',')
                                                                    finally:
                                                                        break
                                                        finally:
                                                            break
                                                elif(choice == 3):
                                                    break
                                                else:
                                                    return
                                                try: (A,d)
                                                except NameError: pass
                                                else:
                                                    a, b, c = cf.cycA2abc(A)
                                                    break
                                elif(choice == 2):
                                    while True:
                                        options = {
                                            1: 'Digitar os vetores \'a,b,c,d\' elementos um a um',
                                            2: 'Escolher de um arquivo .CSV (um vetor por linha)',
                                            3: 'Voltar'
                                            }
                                        options = cf.printMenu(options=options, name="SIS TRIDI CIC - VETORES - MÉTODO DE ENTRADA")
                                        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))
                                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")
                                        else:
                                            try: options[choice]
                                            except KeyError: print("Opção não disponível. Escolha um método do menu abaixo: ")
                                            else:
                                                print("Opção escolhida: %s"%(options[choice]))
                                                if(choice == 1):
                                                    while True:
                                                        try: n = int(input("Digite a dimensão n (>2) do sistema cíclico: "))
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
                                                elif(choice == 2):
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
                                                                a = np.genfromtxt(root.filename, delimiter=',')[0]
                                                                b = np.genfromtxt(root.filename, delimiter=',')[1]
                                                                c = np.genfromtxt(root.filename, delimiter=',')[2]
                                                                d = np.genfromtxt(root.filename, delimiter=',')[3]
                                                        finally:
                                                            break
                                                elif(choice == 3):
                                                    break
                                                else:
                                                    return
                                                try: (a,b,c,d)
                                                except NameError: pass
                                                else:
                                                    break
                                elif(choice == 3):
                                    while True:
                                        try: n = int(input("Digite a dimensão n para gerar o sistema cíclico: "))
                                        except ValueError: print("Inserção inválida.")
                                        else:
                                            if n == 0:
                                                print("Dimensão inválida.")
                                            else:
                                                a,b,c,d = cf.genSysMAP(n=n)
                                                break
                                elif(choice == 4):
                                    break
                                else:
                                    return
                                break
                    x = cf.solveCycTridi(a,b,c,d)
                    print("Sistema Ax=d")
                    print('Matriz A:')
                    print(cf.abc2cycA(a,b,c))
                    print('Vetor d:')
                    print(d)
                    print('Solução X (valores encontrados):')
                    print(x)
                    np.set_printoptions(suppress=True)
                    print('Solução X (notação científica suprimida):')
                    print(x)
                    np.set_printoptions(suppress=False)
                # Se escolheu sair
                else:
                    return

main()