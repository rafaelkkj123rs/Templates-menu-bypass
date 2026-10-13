# CODE BY STOCK
# TEMPLATE BY STOCK
# CREDITS FOR STOCK
# Fiz esse template de menu de bypass quando eu tava sem internet ai resolvi fazer um menu de bypass sem injeção real.
# Caso modifique deixe os creditos do criado original @rafaelkkj123rs

# BIBLIOTECAS
import time
import os
import platform
from colorama import Fore,Style

# CONFIGURAÇÃO 
os.system('cls')
os.system('title bypass')
Key = '2026'

# FUNÇÕES

def limpar():
    os.system('cls')


def bypass():
    key = input('Digite a key: ')

    if key == Key:
        print(Fore.LIGHTGREEN_EX+'Executando bypass'+Style.RESET_ALL)
        time.sleep(0.7)
        limpar()
        bypass_run()
    else:
        print(Fore.RED+'key Errada!'+Style.RESET_ALL)

def bypass_run():
    print('Limpando temp...')
    time.sleep(2)
    print('Injetando...')
    time.sleep(1)
    print('Aguardando resposta do servidor...')
    time.sleep(4)
    print(Fore.GREEN+'OK\n'+Style.RESET_ALL)
    input('Pressione qualquer tecla\n')
    limpar()

def bypass_retira():
    print('Retirando Bypass executavel...')
    time.sleep(2)
    print('Limpando...')
    time.sleep(1)
    print('Aguardando resposta do servidor...')
    time.sleep(4)
    print(Fore.GREEN+'Bypass Retirado com sucesso\n'+Style.RESET_ALL)
    input('Pressione qualquer tecla')
    limpar()

def get_key():
    with open('Key.txt', 'w', encoding='utf-8') as s:
        s.write(Key)
        

# MENU
try:
    while True:
        print(Fore.RED+'v1.0'+Style.RESET_ALL,Fore.RED+platform.system(), platform.version()+Style.RESET_ALL,'\n')

        print(Fore.RED+'[1] Bypass [2] Retira Bypass [3] Minha key\n'+Style.RESET_ALL)

        select = input(Fore.LIGHTRED_EX+'Escolha a opção: '+Style.RESET_ALL)

        if select == '1':
            limpar()
            bypass()
        elif select == '2':
            limpar()
            bypass_retira()
        elif select == '3':
            get_key()
            limpar()
        elif select == '0':
            limpar()
            break
        else:
            print('Selecione uma opção que esteja no menu!')
            time.sleep(0.5)
            limpar()
except ValueError:
    print('algo no codigo deu erro')