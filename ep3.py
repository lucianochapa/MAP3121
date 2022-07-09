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
# import matplotlib.pyplot as plt
# import sys, time, datetime, os

def main():

    # def f(x): return 2*(np.pi**2)*np.sin(np.pi*x)   # Livro Burden Faires
    # def q(x): return np.pi**2                       # Livro Burden Faires
    # def k(x): return 1                              # Livro Burden Faires
    # def solucaoExata(x): return np.sin(np.pi*x)     # Livro Burden Faires

    def f(x): return 12*x*(1-x)-2                   # Exemplo do EP3
    def q(x): return 0                              # Exemplo do EP3
    def k(x): return 1                              # Exemplo do EP3
    def solucaoExata(x): return (x**2)*((1-x)**2)   # Exemplo do EP3
    L = 0.02

    # def f(x): return np.exp(x)+1                        # Exemplo do EP3
    # def q(x): return 0                                  # Exemplo do EP3
    # def k(x): return np.exp(x)                          # Exemplo do EP3
    # def solucaoExata(x): return (x-1)*(np.exp(-x)-1)    # Exemplo do EP3

    # L = 1       # Espessura total do chip
    # D = 0.2     # Espessura do silício
    # def f(x): return 12*x*(1-x)-2                   # Exemplo do EP3
    # def q(x): return 0                              # Exemplo do EP3
    # def k(x):
    #     if(x > L/2 - D) and (x < L/2 + D):
    #         return 3.6                              # Exemplo do EP3
    #     else:
    #         return 60
    # def solucaoExata(x): return (x**2)*((1-x)**2)   # Exemplo do EP3

    nos = [2**i -1 for i in range(3,4)]
    for n in nos:
        # xi, u = cf.solveElemFinitos(f,n,L,q=q)
        xi, u = cf.solveElemFinitos(f,n,q=q)
        u = np.insert(u, 0, 0)
        u = np.append(u, 0)
        u_bar = np.array([solucaoExata(xi[i+1]) for i in range(n)], float)
        u_bar = np.insert(u_bar,0,0)
        u_bar = np.append(u_bar, 0)
        u += 20
        u_bar += 20
        print("Para %i nós:" %(n))
        print("(%i nós) Abcissas: %s"%(n, xi))
        print("(%i nós) Vetor de soluções u(x): %s"%(n, u))
        print("(%i nós) Vetor de soluções exatas u_bar(x): %s"%(n, u_bar))
        dif = abs(u-u_bar)
        print("(%i nós) Vetor diferença absoluta u-u_bar(x): %s"%(n, dif))
        print("(%i nós) Erro máximo: %f"%(n, max(dif)))
        print("\n")

    # Q_zero_mais = 15000     # 
    # Q_zero_menos = 5000     # 
    # L = 0.02                # Em metros
    # sigma = 0.001           # Concentração de distribuição de aquecimento
    # theta = 0.001           # Concentração de distribuição de resfriamento
    # T_ext = 20              # Temperatura externa
    # def Qmais(x, sigma): return Q_zero_mais*np.exp(-((x-(L/2))**2)/(sigma**2))
    # def Qmenos(x, theta): return Q_zero_menos*(np.exp(-(x**2)/(theta**2)) + np.exp(-((x-L)**2)/(theta**2)))
    # def f(x, sigma, theta): return Qmais(x, sigma) - Qmenos(x, theta)   # Exemplo 4.3 do EP3
    # def q(x): return 0                                                  # Exemplo 4.3 do EP3
    # def k(x): return 3.6                                                # Exemplo 4.3 do EP3
    # nos = [2**i -1 for i in range(3,7)]
    # for n in nos:
    #     xi, u = cf.solveElemFinitos(lambda x: f(x, sigma, theta),n,L,q)
    #     u = np.insert(u, 0, 0)
    #     u = np.append(u, 0)
    #     u += T_ext
    #     print("Para %i nós:" %(n))
    #     print("(%i nós) Abcissas: %s"%(n, xi))
    #     print("(%i nós) Vetor de soluções u(x): %s"%(n, u))
    #     print("\n")

main()