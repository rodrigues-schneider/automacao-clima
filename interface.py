from leitura_clima import consultar_clima
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from ttkbootstrap.constants import *

app = ttk.Window(themename="superhero")
app.title("Consultar Clima - São Paulo")
app.geometry("400x150")

#Chama a função e adiciona uma mensagem de sucesso
def chamar_funcao():
    consultar_clima() 
    messagebox.showinfo(f"Sucesso!", "O dados foram coletados e salvos")  # pop-up de sucesso

# Botão que chama a função
botao = ttk.Button(app, text="Consultar Clima", command=chamar_funcao, bootstyle=PRIMARY)
botao.pack(pady=40)

# Inicia a interface
app.mainloop()