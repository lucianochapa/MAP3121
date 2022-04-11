# Universidade de São Paulo
## Instituto de Matemática e Estatística - Departamento de Matemática Aplicada
## Escola Politécnica
# MAP3121 - Métodos Numéricos e Aplicações - 2022.1
## Exercício-programa 01
# Bruno Prasinos Bernal
# Luciano Chaparin Luisi


# Importação de libs
import numpy as np
# import matplotlib.pyplot as plt
# import sys, time, datetime, math
import os
import custom_functions as cf

def printMenu():    # Apresenta ao usuário um menu de opções
        print("MENU", 60 * "-")                                                                             # MENU--------------------------------------------
        options = {}                                                                                        # Cria um dict para guardar os nomes dos arquivos
        options[0] = {'index':1,'info':'Decomposição LU de matriz'}                                         # Salva entrada no dict
        options[1] = {'index':2,'info':'Resolução de sistema tridiagonal usando decomposição de matriz LU'} # Salva entrada no dict
        options[2] = {'index':3,'info':'Encerrar programa'}                                                 # Salva entrada no dict
        for i in options:                                                                                   # Itera nas opções do menu
            print("%s. %s"%(options[i]['index'],options[i]['info']))                                        # Imprime o número e descrição da opção
        print(67 * "-")                                                                                     # ------------------------------------------------
        return options                                                                                      # Retorna o dict 'options'

def main():
    loop = True                                                                             # Cria variável booleana para condicional do laço
    while loop:                                                                             # Abre o laço e mantém enquanto 'loop'
        options = printMenu()                                                               # Imprime o menu e retorna um dict com as opções
        choice = int(input("Digite o número da ação desejada (1 a %i): "%(len(options))))   # Recebe do usuário uma ação do menu (int)
        try: options[choice-1]['index']                                                     # Verifica se a opção é válida
        except NameError:                                                                   # Se não for, mantém o laço e retorna ao menu
            print("Opção não disponível. Escolha a ação desejada do menu abaixo: ")         # Imprime mensagem de erro
        else:                                                                               # Se for válida
            print("Opção escolhida: %s"%(options[choice-1]['info']))                        # Imprime a descrição da ação escolhida
            if(options[choice-1]['index'] == 1):                                            # Se escolheu uma função
                A = [[1,1,0,3],[2,1,-1,1],[3,-1,-1,2],[-1,2,3,-1]]
                # cf.decompLU(cf.recebeA())                                                   # Executa script de decomposição LU
                cf.decompLU(A)                                                              # Executa script de decomposição LU
            elif(options[choice-1]['index'] == 2):                                          # Se escolheu uma função
                cf.solveTridi(A)                                                            # Executa script de resolução de sistema tridiagonal
            else:                                                                           # Se o usuário escolheu sair
                loop = False                                                                # Inversão booleana para quebrar o laço

main()