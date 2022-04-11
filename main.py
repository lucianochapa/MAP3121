# Universidade de São Paulo
## Instituto de Matemática e Estatística - Departamento de Matemática Aplicada
## Escola Politécnica
# MAP3121 - Métodos Numéricos e Aplicações - 2022.1
## Exercício-programa 01
# Bruno Prasinos Bernal
# Luciano Chaparin Luisi


# Importação de libs
import numpy as np
import custom_functions as cf
# import matplotlib.pyplot as plt
# import sys, time, datetime, math, os

def printMenu(options, name):    # Apresenta ao usuário um menu de opções
        options[len(options)+1] = {'index':len(options)+1,'info':'Encerrar programa'}
        print(name, (66 - len(name))*"-")                                               # MENU--------------------------------------------
        for i in options:                                                               # Itera nas opções do menu
            print("%s. %s"%(options[i]['index'],options[i]['info']))                    # Imprime o número e descrição da opção
        print(67 * "-")                                                                 # ------------------------------------------------
        return options                                                                  # Retorna o dict 'options'

def main():
    while True:                                                                             
        menu = {                                                                            # Cria um menu de opções como dict
            1: {'index':1,'info':'Decomposição LU de matriz'},
            2: {'index':2,'info':'Resolução de sistema tridiagonal usando decomposição de matriz LU'}
            }
        options = printMenu(options=menu, name="MENU")                                      # Imprime o menu e retorna um dict com as opções
        choice = int(input("Digite o número da ação desejada (1 a %i): "%(len(options))))   # Recebe do usuário uma ação do menu (int)
        try: options[choice]                                                                # Verifica se a opção é válida
        except KeyError:                                                                    # Se não for, mantém o laço e retorna ao menu
            print("Opção não disponível. Escolha a ação desejada do menu abaixo: ")         # Imprime mensagem de erro
        else:                                                                               # Se for válida
            print("Opção escolhida: %s"%(options[choice]['info']))                          # Imprime a descrição da ação escolhida
            if(choice == 1):                                                                # Se escolheu decomp LU
                while True:
                    entradas = {                                                                    # Cria um menu de opções como dict
                        1: {'index':1,'info':'Digitar elementos um a um'},
                        2: {'index':2,'info':'Escolher de um arquivo'},
                        3: {'index':3,'info':'Voltar'}
                        }
                    options = printMenu(options=entradas, name="MÉTODO DE ENTRADA")                 # Imprime o menu e retorna um dict com as opções
                    choice = int(input("Escolha um método de entrada (1 a %i): "%(len(options))))   # Recebe do usuário uma ação do menu (int)
                    print("Opção escolhida: %s"%(options[choice]['info']))                          # Imprime a descrição da ação escolhida
                    try: options[choice]                                                            # Verifica se a opção é válida
                    except KeyError:                                                                # Se não for, mantém o laço e retorna ao menu
                        print("Opção não disponível. Escolha um método do menu abaixo: ")           # Imprime mensagem de erro
                    else:                                                                           # Se for válida
                        if(choice == 1):                                                            # Se escolheu entrada manual
                            A = cf.recebeA()                                                        # Roda função para receber os valores um a um
                        elif(choice == 2):                                                          # Se escolheu entrada por arquivo
                            A = np.genfromtxt('matriz.csv', delimiter=',')                          # Importa os valores do csv para um ndarray
                        elif(choice == 3):                                                          # Se escolheu voltar ao menu
                            break                                                                   # Quebra o laço e volta ao menu anterior
                        else:                                                                       # Se escolheu encerrar o programa
                            return                                                                  # Encerra o programa
                        cf.decompLU(A)                                                              # Executa script de decomposição LU
                        break                                                                       # Quebra o laço e volta ao menu anterior
            elif(choice == 2):                                                                      # Se escolheu sistema tridi
                a = [0,-1,-1,-1]                                                                    # Subdiagonal da matriz de coeficientes
                b = [2,2,2,2]                                                                       # Diagonal da matriz de coeficientes
                c = [-1,-1,-1,0]                                                                    # Sobrediagonal da matriz de coeficientes
                d = [1,0,0,1]                                                                       # Coeficientes independentes do sistema
                x = cf.solveTridi(a,b,c,d)                                                          # Executa script de resolução de sistema tridiagonal e guarda resultado em 'x'
                print(x)                                                                            # Imprime 'x'
            else:                                                                                   # Se o usuário escolheu sair
                return                                                                              # Encerra o programa

main()