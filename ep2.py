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
                    a = 0
                    b = 1
                    for n in range(6,11,2):
                        c = 0
                        d = 1
                        def f(x): return np.cos(x)
                        # f = lambda x: 1
                        F = cf.gaussIntegrate2(f,c,d,n)
                        # I = cf.gaussIntegrate2(f(F),c,d,n)
                        # I = cf.gaussIntegrate2(F,a,b,n)
                        # II = cf.gaussIntegrate2(I,a,b,n)
                        print("n: %i"%(n))
                        print("Volume do cubo: %f"%(F))
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