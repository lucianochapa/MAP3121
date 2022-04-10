# Universidade de São Paulo
## Instituto de Matemática e Estatística - Departamento de Matemática Aplicada
## Escola Politécnica
# MAP3121 - Métodos Numéricos e Aplicações - 2022.1
## Exercício-programa 01
# Bruno Prasinos Bernal
# Luciano Chaparin Luisi


# Importação de libs
# import numpy as np
# import matplotlib.pyplot as plt
# import sys, time, datetime, math
import os

def printMenu():    # Apresenta ao usuário um menu de opções
        print("MENU", 60 * "-")                                         # MENU--------------------------------------------
        options = {}                                                    # Cria um dict para guardar os nomes dos arquivos
        count = 0                                                       # Contador para posição de 'options'
        for i in os.listdir("functions/"):                              # Lista os arquivos no diretório /functions
            with open("functions/"+i, encoding="utf-8") as f:           # Abre o arquivo 'i'
                first_line = f.readline().rstrip().replace("# ","")     # Lê a primeira linha, remove caracteres '\n' e '#'
                options[count] = {'file_name':i,'comment':first_line}   # Salva o nome do arquivo e comentário num nested dict
            count +=1                                                   # Roda o contador
            print("%i. %s"%(count,first_line))                          # Imprime a opção do menu
        options[count] = {'file_name':'exit','comment':"Encerrar programa"} # Salva última entrada no dict
        print("%i. Encerrar programa"%(count+1))                        # Imprime a última opção
        print(67 * "-")                                                 # ------------------------------------------------
        return options                                                  # Retorna o dict 'options'

def main():
    loop = True                                                                             # Cria variável booleana para condicional do laço
    while loop:                                                                             # Abre o laço e mantém enquanto 'loop'
        options = printMenu()                                                               # Imprime o menu e retorna um dict com as opções
        choice = int(input("Digite o número da ação desejada (1 a %i): "%(len(options))))   # Recebe do usuário uma ação do menu (int)
        try: options[choice-1]['file_name']                                                 # Verifica se a opção é válida
        except NameError:                                                                   # Se não for, mantém o laço e retorna ao menu
            print("Opção não disponível. Escolha a ação desejada do menu abaixo: ")         # Imprime mensagem de erro
        else:                                                                               # Se for válida
            print("Opção escolhida: %s"%(options[choice-1]['comment']))                     # Imprime a descrição da ação escolhida
            if(options[choice-1]['file_name'] == 'exit'):                                   # Se o usuário escolheu sair
                loop = False                                                                # Inversão booleana para quebrar o laço
            else:                                                                           # Se escolheu uma função
                exec(open("functions/" + options[choice-1]['file_name']).read())            # Executa o programa selecionado

main()