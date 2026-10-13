# CODE BY STOCK
# TEMPLATE BY STOCK
# CREDITS FOR STOCK
# Fiz esse template de menu de bypass quando eu tava sem internet ai resolvi fazer um menu de bypass sem injeção real.
# Caso modifique deixe os creditos do criado original @rafaelkkj123rs

import tkinter as tk
import time
from colorama import Fore,Style
from tkinter import messagebox

# CONFIGURAÇÃO
window = tk.Tk()
window.geometry('400x177')
window.title('bypass')
window.resizable(False,False)
Key = 2026

# FUNÇÕES

def bypass():
    try:
        key = float(textbox.get())

        if key == Key:
            messagebox.showinfo('Sucesso','Key valida!')
            time.sleep(0.7)
            bypass_run()
        else:
            messagebox.showerror('Error','Key invalida!')
    except ValueError:
        messagebox.showwarning('Aviso','Digite uma key valida!')

def bypass_run():
    injeçao.configure(text='Iniciando')

    window.after(2000, lambda: injeçao.configure(text='Limpando temp...'))
    
    window.after(4000, lambda: injeçao.configure(text='Injetando...'))

    window.after(6000, lambda: injeçao.configure(text='Aguardando resposta do servidor...'))

    window.after(8000, lambda: messagebox.showinfo('Sucesso','OK'))

    window.after(9000, lambda: injeçao.configure(text='Bypass Injetado'))

textbox = tk.Entry(window,width=40)
textbox.pack(pady='20px')

confirm = tk.Button(window, text='Run', command=bypass,padx='50px')
confirm.pack(pady='21px')

injeçao = tk.Label(window, text='Nada Injetado')
injeçao.pack()
window.mainloop()