# Universidade de São Paulo
## Instituto de Matemática e Estatística - Departamento de Matemática Aplicada
## Escola Politécnica
# MAP3121 - Métodos Numéricos e Aplicações - 2022.1
## Exercício-programa 01
# Bruno Prasinos Bernal
# Luciano Chaparin Luisi


# # Importação de libs
import numpy as np, custom_functions as cf, tkinter
from tkinter import filedialog
from math import cos, pi
# import matplotlib.pyplot as plt
# import sys, time, datetime, os

def printMenu(options: dict, name:str):
    '''Imprime um menu de opções no terminal

    Parâmetros
    ===
    options: dict
        Um dicionário contendo o índice e descrição de cada opção
    name: str
        Nome do menu exibido no topo
    '''
    options[len(options)+1] = 'Encerrar programa'
    print(name, (max(0,66 - len(name)))*"-")                            # MENU--------------------------------------------
    for i in options:                                                   # Itera nas opções do menu
        print("%s. %s"%(i,options[i]))                                  # Imprime o número e descrição da opção
    print(67 * "-")                                                     # ------------------------------------------------
    return options                                                      # Retorna o dict 'options'

def main():
    while True:                                                                                                                 # Abre um laço e um nível de menu
        options = {                                                                                                             # Cria um menu de opções como dict
            1: 'Decomposição LU de matriz',
            2: 'Resolução de sistema tridiagonal usando decomposição de matriz LU',
            3: 'Resolução de sistema tridiagonal cíclico'
            }
        options = printMenu(options=options, name="MENU PRINCIPAL")                                                             # Imprime o menu e retorna um dict com as opções
        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))                                      # Recebe do usuário uma ação do menu (int)
        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")                                    # Imprime mensagem de erro
        else:
            try: options[choice]                                                                                                # Verifica se a opção é válida
            except KeyError: print("Opção não disponível. Escolha a ação desejada do menu abaixo: ")                            # Imprime mensagem de erro
            else:                                                                                                               # Se for válida
                print("Opção escolhida: %s"%(options[choice]))                                                                  # Imprime a descrição da ação escolhida
                if(choice == 1):                                                                                                # Se escolheu decomp LU
                    while True:                                                                                                 # Abre um laço e um nível de menu
                        options = {                                                                                             # Cria um menu de opções como dict
                            1: 'Digitar elementos um a um',
                            2: 'Escolher de um arquivo .CSV',
                            3: 'Voltar'
                            }
                        options = printMenu(options=options, name="MÉTODO DE ENTRADA")                                          # Imprime o menu e retorna um dict com as opções
                        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))                      # Recebe do usuário uma ação do menu (int)
                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")                    # Imprime mensagem de erro
                        else:
                            try: options[choice]                                                                                # Verifica se a opção é válida
                            except KeyError: print("Opção não disponível. Escolha um método do menu abaixo: ")                  # Imprime mensagem de erro
                            else:                                                                                               # Se for válida
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
                                try: A
                                except NameError: pass
                                else:
                                    cf.decompLU(A)                                                                              # Executa script de decomposição LU
                                    break                                                                                       # Quebra o laço e volta ao menu anterior
                elif(choice == 2):                                                                                              # Se escolheu sistema tridiagonal
                    while True:                                                                                                 # Abre um laço e um nível de menu
                        options = {                                                                                             # Cria um menu de opções como dict
                            1: 'Inserir matriz tridiagonal \'A\' e vetor \'d\' (Ax=d)',
                            2: 'Inserir os vetores \'a,b,c,d\' (Ax=d)',
                            3: 'Voltar'
                            }
                        options = printMenu(options=options, name="MÉTODO DE ENTRADA")                                          # Imprime o menu e retorna um dict com as opções
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
                                            1: 'Digitar matriz \'A\' elementos um a um',
                                            2: 'Escolher de um arquivo .CSV',
                                            3: 'Voltar'
                                            }
                                        options = printMenu(options=options, name="MÉTODO DE ENTRADA")                          # Imprime o menu e retorna um dict com as opções
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
                                                        root.filename = filedialog.askopenfilename(title='Escolher matriz A tridiagonal')
                                                        try: root.filename
                                                        except (OSError,FileNotFoundError): print("Nenhum arquivo selecionado. Abordando ação e retornando ao menu.")
                                                        else:
                                                            if root.filename == '':
                                                                print("Nenhum arquivo selecionado. Abordando ação e retornando ao menu.")
                                                            else:
                                                                A = np.genfromtxt(root.filename, delimiter=',')                         # Importa os valores do csv para um ndarray
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
                                                                            d = np.genfromtxt(root.filename, delimiter=',')             # Importa os valores do csv para um ndarray
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
                                        options = printMenu(options=options, name="MÉTODO DE ENTRADA")                          # Imprime o menu e retorna um dict com as opções
                                        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))      # Recebe do usuário uma ação do menu (int)
                                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")    # Imprime mensagem de erro
                                        else:
                                            try: options[choice]                                                                # Verifica se a opção é válida
                                            except KeyError: print("Opção não disponível. Escolha um método do menu abaixo: ")  # Imprime mensagem de erro
                                            else:                                                                               # Se for válida
                                                print("Opção escolhida: %s"%(options[choice]))                                  # Imprime a descrição da ação escolhida
                                                if(choice == 1):                                                                # Se escolheu entrada manual
                                                    while True:
                                                        try: n = int(input("Digite a dimensão n do sistema: "))                 # Roda função para receber os valores um a um
                                                        except ValueError: print("Inserção inválida.")
                                                        else:
                                                            if n == 0:
                                                                print("Dimensão 0 inválida.")
                                                            else:
                                                                print("Insira o vetor \'a\'(dim=%i), sem o primeiro elemento nulo: "%(n-1))
                                                                a = cf.recebeVetor(tamanho=(n-1),nome_vetor='a')
                                                                print("Insira o vetor \'b\'(dim=%i): "%n)
                                                                b = cf.recebeVetor(tamanho=n,nome_vetor='b')
                                                                print("Insira o vetor \'c\'(dim=%i), sem o último elemento nulo: "%(n-1))
                                                                c = cf.recebeVetor(tamanho=(n-1),nome_vetor='c')
                                                                print("Insira o vetor \'d\'(dim=%i): "%n)
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
                                                try: a
                                                except NameError: pass
                                                else:
                                                    break                                                                       # Quebra o laço
                                elif(choice == 3):                                                                              # Se escolheu voltar ao menu
                                    break                                                                                       # Quebra o laço e volta ao menu anterior
                                else:                                                                                           # Se escolheu encerrar o programa
                                    return                                                                                      # Encerra o programa
                                break                                                                                           # Quebra o laço e volta ao menu anterior
                    cf.solveTridi(a,b,c,d)                                                                                      # Executa script de resolução de sistema tridiagonal e guarda resultado em 'x'
                elif(choice == 3):                                                                                              # Se escolheu sistema tridiagonal cíclico
                    while True:                                                                                                 # Abre um laço e um nível de menu
                        options = {                                                                                             # Cria um menu de opções como dict
                            1: 'Inserir matriz tridiagonal cíclica \'A\' e vetor \'d\' (Ax=d)',
                            2: 'Inserir os vetores \'a,b,c,d\' (Ax=d)',
                            3: 'Voltar'
                            }
                        options = printMenu(options=options, name="MÉTODO DE ENTRADA")                                          # Imprime o menu e retorna um dict com as opções
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
                                            1: 'Digitar matriz \'A\' elementos um a um',
                                            2: 'Escolher de um arquivo .CSV',
                                            3: 'Voltar'
                                            }
                                        options = printMenu(options=options, name="MÉTODO DE ENTRADA")                          # Imprime o menu e retorna um dict com as opções
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
                                                try: A
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
                                        options = printMenu(options=options, name="MÉTODO DE ENTRADA")                          # Imprime o menu e retorna um dict com as opções
                                        try: choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))      # Recebe do usuário uma ação do menu (int)
                                        except ValueError: print("Opção não disponível. Escolha um método do menu abaixo: ")    # Imprime mensagem de erro
                                        else:
                                            try: options[choice]                                                                # Verifica se a opção é válida
                                            except KeyError: print("Opção não disponível. Escolha um método do menu abaixo: ")  # Imprime mensagem de erro
                                            else:                                                                               # Se for válida
                                                print("Opção escolhida: %s"%(options[choice]))                                  # Imprime a descrição da ação escolhida
                                                if(choice == 1):                                                                # Se escolheu entrada manual
                                                    while True:
                                                        try: n = int(input("Digite a dimensão n do sistema cíclico: "))         # Roda função para receber os valores um a um
                                                        except ValueError: print("Inserção inválida.")
                                                        else:
                                                            if n == 0:
                                                                print("Dimensão 0 inválida.")
                                                            else:
                                                                print("Insira o vetor \'a\'(dim=%i): "%n)
                                                                a = cf.recebeVetor(tamanho=n,nome_vetor='a')
                                                                print("Insira o vetor \'b\'(dim=%i): "%n)
                                                                b = cf.recebeVetor(tamanho=n,nome_vetor='b')
                                                                print("Insira o vetor \'c\'(dim=%i): "%n)
                                                                c = cf.recebeVetor(tamanho=n,nome_vetor='c')
                                                                print("Insira o vetor \'d\'(dim=%i): "%n)
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
                                                try: a
                                                except NameError: pass
                                                else:
                                                    break                                                                       # Quebra o laço
                                elif(choice == 3):                                                                              # Se escolheu voltar ao menu
                                    break                                                                                       # Quebra o laço e volta ao menu anterior
                                else:                                                                                           # Se escolheu encerrar o programa
                                    return                                                                                      # Encerra o programa
                                break                                                                                           # Quebra o laço e volta ao menu anterior
                    cf.solveCycTridi(a,b,c,d)                                                                                      # Executa script de resolução de sistema tridiagonal e guarda resultado em 'x'
                else:                                                                                                           # Se o usuário escolheu sair
                    return                                                                                                      # Encerra o programa

main()