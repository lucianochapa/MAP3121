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
# # Usado para selecionar arquivos .csv a partir do explorador
# import tkinter
# from tkinter import filedialog
# from math import cos, pi
# import matplotlib.pyplot as plt
# import sys, time, datetime, os

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
                        I = cf.gaussDoubleIntegrate(f,a,b,c,d,n,n)
                        print("Volume de um cubo com arestas de comprimento 1")
                        print("(n=%i nós): Vol.cubo = %f"%(n,I))
                    # Volume de um teraedro com vértices (0, 0, 0), (1, 0, 0), (0, 1, 0) e (0, 0, 1)
                    for n in range(6,11,2):     # Itera para (n=6, 8 e 10) nós
                        a = 0
                        b = 1
                        c = 0
                        d = 1
                        # definir a função de x e y para o tetraedro
                        # def f(x, y): return 1
                        I = cf.gaussDoubleIntegrate(f,a,b,c,d,n,n)
                        print("Volume de um tetraedro com vértices (0,0,0), (1,0,0), (0,1,0) e (0,0,1)")
                        print("(n=%i nós): Vol.tetraedro = %f"%(n,I))
                # # Se escolheu Exemplo 2
                # elif(choice == 2):
                # # Se escolheu Exemplo 3
                # elif(choice == 3):
                # # Se escolheu Exemplo 4
                # elif(choice == 4):
                # Se escolheu sair
                else:
                    return

main()