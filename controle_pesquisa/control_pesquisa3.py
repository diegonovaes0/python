import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
from datetime import datetime

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
                if "nome_avaliador" not in cliente:
                    cliente["nome_avaliador"] = ""
                if "email_avaliador" not in cliente:
                    cliente["email_avaliador"] = ""
                if "telefone" not in cliente:
                    cliente["telefone"] = ""
                if "data" not in cliente:
                    cliente["data"] = ""
                if "hora" not in cliente:
                    cliente["hora"] = ""
            return dados
    return []

# Função para salvar os dados no arquivo JSON
def salvar_dados():
    with open(DATA_FILE, "w") as file:
        json.dump(clientes, file, indent=4)

# Função para atualizar a cor dos botões com base na resposta
def atualizar_botoes():
    for i, cliente in enumerate(clientes):
        botoes[i]["botao_respondido"].config(bg="green" if cliente["aprovado_suporte"] else "gray")
        botoes[i]["botao_nao_respondido"].config(bg="gray" if cliente["aprovado_suporte"] else "red")

# Função para marcar como respondido
def marcar_como_respondido(index):
    clientes[index]["aprovado_suporte"] = True
    salvar_dados()
    atualizar_botoes()

# Função para marcar como não respondido
def marcar_como_nao_respondido(index):
    clientes[index]["aprovado_suporte"] = False
    salvar_dados()
    atualizar_botoes()

# Função para editar um projeto
def editar_projeto(index):
    projeto = clientes[index]

    # Abre uma janela de diálogo para editar os campos
    projeto["analista"] = simpledialog.askstring("Editar Analista", "Analista:", initialvalue=projeto["analista"])
    projeto["n_project"] = simpledialog.askstring("Editar N° Project", "N° Project:", initialvalue=projeto["n_project"])
    projeto["nome_projeto"] = simpledialog.askstring("Editar Nome do Projeto", "Nome do Projeto:", initialvalue=projeto["nome_projeto"])
    projeto["nota_pesquisa"] = simpledialog.askstring("Editar Nota da Pesquisa", "Nota da Pesquisa:", initialvalue=projeto["nota_pesquisa"])
    projeto["nome_avaliador"] = simpledialog.askstring("Editar Nome do Avaliador", "Nome do Avaliador:", initialvalue=projeto["nome_avaliador"])
    projeto["email_avaliador"] = simpledialog.askstring("Editar E-mail do Avaliador", "E-mail do Avaliador:", initialvalue=projeto["email_avaliador"])
    projeto["telefone"] = simpledialog.askstring("Editar Telefone", "Telefone:", initialvalue=projeto["telefone"])

    # Atualiza e salva as alterações
    salvar_dados()
    exibir_projetos()

# Função para excluir um projeto
def excluir_projeto(index):
    if messagebox.askyesno("Confirmar Exclusão", "Tem certeza de que deseja excluir este projeto?"):
        del clientes[index]
        salvar_dados()
        exibir_projetos()

# Função para adicionar um novo projeto
def adicionar_projeto():
    analista = entry_analista.get()
    n_project = entry_n_project.get()
    nome_projeto = entry_nome_projeto.get()
    nota_pesquisa = entry_nota_pesquisa.get()
    nome_avaliador = entry_nome_avaliador.get()
    email_avaliador = entry_email_avaliador.get()
    telefone = entry_telefone.get()
    data_atual = datetime.now()
    data = data_atual.strftime("%d/%m/%Y")
    hora = data_atual.strftime("%H:%M")

    if analista and n_project and nome_projeto and nota_pesquisa and nome_avaliador and email_avaliador and telefone:
        novo_projeto = {
            "analista": analista,
            "n_project": n_project,
            "nome_projeto": nome_projeto,
            "aprovado_suporte": False,
            "nota_pesquisa": nota_pesquisa,
            "nome_avaliador": nome_avaliador,
            "email_avaliador": email_avaliador,
            "telefone": telefone,
            "data": data,
            "hora": hora
        }
        clientes.append(novo_projeto)
        salvar_dados()
        exibir_projetos()
        entry_analista.delete(0, tk.END)
        entry_n_project.delete(0, tk.END)
        entry_nome_projeto.delete(0, tk.END)
        entry_nota_pesquisa.delete(0, tk.END)
        entry_nome_avaliador.delete(0, tk.END)
        entry_email_avaliador.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

# Função para exibir os projetos
def exibir_projetos():
    for widget in frame_projetos.winfo_children():
        widget.destroy()
    global botoes
    botoes = []
    for i, projeto in enumerate(clientes):
        # Faixa para cada projeto
        frame = tk.Frame(frame_projetos, bg="#d9d9d9", padx=10, pady=10, relief="groove", bd=2)
        frame.pack(fill="x", pady=5)

        # Exibindo informações organizadas em rótulos
        tk.Label(frame, text=f"Data: {projeto['data']}  Hora: {projeto['hora']}", bg="#d9d9d9").pack(anchor="w")
        tk.Label(frame, text=f"Analista: {projeto['analista']}", bg="#d9d9d9").pack(anchor="w")
        tk.Label(frame, text=f"N° Project: {projeto['n_project']}", bg="#d9d9d9").pack(anchor="w")
        tk.Label(frame, text=f"Nome do Projeto: {projeto['nome_projeto']}", bg="#d9d9d9").pack(anchor="w")
        tk.Label(frame, text=f"Nota da Pesquisa: {projeto['nota_pesquisa']}", bg="#d9d9d9").pack(anchor="w")
        tk.Label(frame, text=f"Avaliador: {projeto['nome_avaliador']} - Email: {projeto['email_avaliador']} - Telefone: {projeto['telefone']}", bg="#d9d9d9").pack(anchor="w")

        # Botões de status, edição e exclusão
        botao_respondido = tk.Button(
            frame, text="Respondido",
            command=lambda idx=i: marcar_como_respondido(idx),
            bg="green" if projeto["aprovado_suporte"] else "gray"
        )
        botao_respondido.pack(side="right", padx=2)

        botao_nao_respondido = tk.Button(
            frame, text="Não Respondido",
            command=lambda idx=i: marcar_como_nao_respondido(idx),
            bg="gray" if projeto["aprovado_suporte"] else "red"
        )
        botao_nao_respondido.pack(side="right", padx=2)

        botao_editar = tk.Button(frame, text="Editar", command=lambda idx=i: editar_projeto(idx), bg="blue", fg="white")
        botao_editar.pack(side="right", padx=2)

        botao_excluir = tk.Button(frame, text="Excluir", command=lambda idx=i: excluir_projeto(idx), bg="red", fg="white")
        botao_excluir.pack(side="right", padx=2)

        botoes.append({"botao_respondido": botao_respondido, "botao_nao_respondido": botao_nao_respondido})

# Inicializando o programa
clientes = carregar_dados()

# Interface Gráfica com Tkinter
root = tk.Tk()
root.title("Controle de Pesquisa de Satisfação")
root.geometry("700x600")

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

tk.Label(frame_form, text="Nome do Avaliador:").grid(row=4, column=0, padx=5, pady=5)
entry_nome_avaliador = tk.Entry(frame_form)
entry_nome_avaliador.grid(row=4, column=1, padx=5, pady=5)

tk.Label(frame_form, text="E-mail do Avaliador:").grid(row=5, column=0, padx=5, pady=5)
entry_email_avaliador = tk.Entry(frame_form)
entry_email_avaliador.grid(row=5, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Telefone:").grid(row=6, column=0, padx=5, pady=5)
entry_telefone = tk.Entry(frame_form)
entry_telefone.grid(row=6, column=1, padx=5, pady=5)

botao_adicionar = tk.Button(frame_form, text="Adicionar Projeto", command=adicionar_projeto)
botao_adicionar.grid(row=7, columnspan=2, pady=10)

frame_projetos = tk.Frame(root)
frame_projetos.pack(fill="both", expand=True)

exibir_projetos()
root.mainloop()
