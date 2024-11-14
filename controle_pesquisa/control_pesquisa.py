import tkinter as tk
from tkinter import messagebox
import json
import os

# Nome do arquivo para armazenar dados
DATA_FILE = "clientes.json"

# Função para carregar os dados do arquivo JSON
def carregar_dados():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Função para salvar os dados no arquivo JSON
def salvar_dados():
    with open(DATA_FILE, "w") as file:
        json.dump(clientes, file, indent=4)

# Função para atualizar a cor do botão com base na resposta
def atualizar_botoes():
    for i, cliente in enumerate(clientes):
        cor = "green" if cliente["respondeu"] else "red"
        botoes[i].config(bg=cor)

# Função para marcar como respondido
def marcar_como_respondido(index):
    clientes[index]["respondeu"] = True
    salvar_dados()
    atualizar_botoes()

# Função para adicionar um novo cliente
def adicionar_cliente():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    if nome and email and telefone:
        novo_cliente = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "respondeu": False
        }
        clientes.append(novo_cliente)
        salvar_dados()
        exibir_clientes()
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

# Função para exibir os clientes
def exibir_clientes():
    for widget in frame_clientes.winfo_children():
        widget.destroy()
    global botoes
    botoes = []
    for i, cliente in enumerate(clientes):
        frame = tk.Frame(frame_clientes)
        frame.pack(fill="x", pady=2)

        label = tk.Label(frame, text=f"{cliente['nome']} - {cliente['email']} - {cliente['telefone']}")
        label.pack(side="left")

        botao_resposta = tk.Button(
            frame, text="Resposta", 
            command=lambda idx=i: marcar_como_respondido(idx),
            bg="green" if cliente["respondeu"] else "red"
        )
        botao_resposta.pack(side="right")
        botoes.append(botao_resposta)

# Inicializando o programa
clientes = carregar_dados()

# Interface Gráfica com Tkinter
root = tk.Tk()
root.title("Controle de Pesquisa de Satisfação")
root.geometry("500x400")

frame_form = tk.Frame(root)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame_form)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Email:").grid(row=1, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_form)
entry_email.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Telefone:").grid(row=2, column=0, padx=5, pady=5)
entry_telefone = tk.Entry(frame_form)
entry_telefone.grid(row=2, column=1, padx=5, pady=5)

botao_adicionar = tk.Button(frame_form, text="Adicionar Cliente", command=adicionar_cliente)
botao_adicionar.grid(row=3, columnspan=2, pady=10)

frame_clientes = tk.Frame(root)
frame_clientes.pack(fill="both", expand=True)

exibir_clientes()
root.mainloop()
