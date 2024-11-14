import tkinter as tk
from tkinter import messagebox
import json
import os

# Nome do arquivo para armazenar dados
DATA_FILE = "clientes.json"

# Função para carregar os dados do arquivo JSON e adicionar campos ausentes
def carregar_dados():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            dados = json.load(file)
            # Verifica e adiciona campos ausentes
            for cliente in dados:
                if "analista" not in cliente:
                    cliente["analista"] = ""
                if "n_project" not in cliente:
                    cliente["n_project"] = ""
                if "nome_projeto" not in cliente:
                    cliente["nome_projeto"] = ""
                if "aprovado_suporte" not in cliente:
                    cliente["aprovado_suporte"] = False
                if "nota_pesquisa" not in cliente:
                    cliente["nota_pesquisa"] = ""
                if "email_avaliador" not in cliente:
                    cliente["email_avaliador"] = ""
            return dados
    return []

# Função para salvar os dados no arquivo JSON
def salvar_dados():
    with open(DATA_FILE, "w") as file:
        json.dump(clientes, file, indent=4)

# Resto do código continua igual...


# Função para atualizar a cor dos botões com base na aprovação do suporte
def atualizar_botoes():
    for i, cliente in enumerate(clientes):
        cor = "green" if cliente["aprovado_suporte"] else "red"
        botoes[i]["botao_aprovado"].config(bg="green" if cliente["aprovado_suporte"] else "gray")
        botoes[i]["botao_nao_aprovado"].config(bg="gray" if cliente["aprovado_suporte"] else "red")

# Função para marcar como aprovado
def marcar_como_aprovado(index):
    clientes[index]["aprovado_suporte"] = True
    salvar_dados()
    atualizar_botoes()

# Função para marcar como não aprovado
def marcar_como_nao_aprovado(index):
    clientes[index]["aprovado_suporte"] = False
    salvar_dados()
    atualizar_botoes()

# Função para adicionar um novo projeto
def adicionar_projeto():
    analista = entry_analista.get()
    n_project = entry_n_project.get()
    nome_projeto = entry_nome_projeto.get()
    nota_pesquisa = entry_nota_pesquisa.get()
    email_avaliador = entry_email_avaliador.get()

    if analista and n_project and nome_projeto and nota_pesquisa and email_avaliador:
        novo_projeto = {
            "analista": analista,
            "n_project": n_project,
            "nome_projeto": nome_projeto,
            "aprovado_suporte": False,
            "nota_pesquisa": nota_pesquisa,
            "email_avaliador": email_avaliador
        }
        clientes.append(novo_projeto)
        salvar_dados()
        exibir_projetos()
        entry_analista.delete(0, tk.END)
        entry_n_project.delete(0, tk.END)
        entry_nome_projeto.delete(0, tk.END)
        entry_nota_pesquisa.delete(0, tk.END)
        entry_email_avaliador.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

# Função para exibir os projetos
def exibir_projetos():
    for widget in frame_projetos.winfo_children():
        widget.destroy()
    global botoes
    botoes = []
    for i, projeto in enumerate(clientes):
        frame = tk.Frame(frame_projetos)
        frame.pack(fill="x", pady=2)

        label = tk.Label(
            frame, 
            text=f"{projeto['analista']} - {projeto['n_project']} - {projeto['nome_projeto']} - Nota: {projeto['nota_pesquisa']} - Avaliador: {projeto['email_avaliador']}"
        )
        label.pack(side="left")

        botao_aprovado = tk.Button(
            frame, text="Aprovado",
            command=lambda idx=i: marcar_como_aprovado(idx),
            bg="green" if projeto["aprovado_suporte"] else "gray"
        )
        botao_aprovado.pack(side="right", padx=2)

        botao_nao_aprovado = tk.Button(
            frame, text="Não Aprovado",
            command=lambda idx=i: marcar_como_nao_aprovado(idx),
            bg="gray" if projeto["aprovado_suporte"] else "red"
        )
        botao_nao_aprovado.pack(side="right", padx=2)

        botoes.append({"botao_aprovado": botao_aprovado, "botao_nao_aprovado": botao_nao_aprovado})

# Inicializando o programa
clientes = carregar_dados()

# Interface Gráfica com Tkinter
root = tk.Tk()
root.title("Controle de Pesquisa de Satisfação")
root.geometry("600x500")

frame_form = tk.Frame(root)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Analista:").grid(row=0, column=0, padx=5, pady=5)
entry_analista = tk.Entry(frame_form)
entry_analista.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="N° Project:").grid(row=1, column=0, padx=5, pady=5)
entry_n_project = tk.Entry(frame_form)
entry_n_project.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Nome do Projeto:").grid(row=2, column=0, padx=5, pady=5)
entry_nome_projeto = tk.Entry(frame_form)
entry_nome_projeto.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Nota da Pesquisa:").grid(row=3, column=0, padx=5, pady=5)
entry_nota_pesquisa = tk.Entry(frame_form)
entry_nota_pesquisa.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame_form, text="E-mail do Avaliador:").grid(row=4, column=0, padx=5, pady=5)
entry_email_avaliador = tk.Entry(frame_form)
entry_email_avaliador.grid(row=4, column=1, padx=5, pady=5)

botao_adicionar = tk.Button(frame_form, text="Adicionar Projeto", command=adicionar_projeto)
botao_adicionar.grid(row=5, columnspan=2, pady=10)

frame_projetos = tk.Frame(root)
frame_projetos.pack(fill="both", expand=True)

exibir_projetos()
root.mainloop()
