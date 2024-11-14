import tkinter as tk
from tkinter import messagebox, filedialog
import json
import os
from datetime import datetime

# Nome do arquivo principal para armazenar todos os dados dos clientes
DATA_FILE = "clientes.json"
# Diretório para armazenar pesquisas salvas individualmente
PESQUISAS_DIR = "pesquisas_salvas"
os.makedirs(PESQUISAS_DIR, exist_ok=True)

# Função para carregar as pesquisas do arquivo JSON principal
def carregar_dados():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Função para salvar todas as pesquisas no arquivo principal
def salvar_dados():
    with open(DATA_FILE, "w") as file:
        json.dump(clientes, file, indent=4)
    messagebox.showinfo("Sucesso", "Dados salvos com sucesso no arquivo JSON.")

# Função para salvar uma pesquisa individual em um arquivo separado
def salvar_pesquisa_individual(pesquisa):
    filename = f"{PESQUISAS_DIR}/{pesquisa['n_project']}_{pesquisa['data']}.json"
    with open(filename, "w") as file:
        json.dump(pesquisa, file, indent=4)

# Função para atualizar a exibição dos botões e cores com base na resposta
def atualizar_botoes():
    for i, cliente in enumerate(clientes):
        color = "green" if cliente["aprovado_suporte"] else "red"
        botoes[i]["frame"].config(bg=color)

# Função para marcar como respondido e mudar a cor de fundo
def marcar_como_respondido(index):
    clientes[index]["aprovado_suporte"] = True
    salvar_dados()
    atualizar_botoes()

# Função para marcar como não respondido e mudar a cor de fundo
def marcar_como_nao_respondido(index):
    clientes[index]["aprovado_suporte"] = False
    salvar_dados()
    atualizar_botoes()

# Função para alternar entre modo de edição e modo de exibição da pesquisa
def editar_projeto(index):
    projeto = clientes[index]
    frame = botoes[index]["frame"]
    is_editing = botoes[index].get("is_editing", False)

    # Alterna para o modo de edição
    if not is_editing:
        botoes[index]["labels"]["analista"].grid_forget()
        botoes[index]["entries"]["analista"].grid(row=1, column=1)
        
        botoes[index]["labels"]["n_project"].grid_forget()
        botoes[index]["entries"]["n_project"].grid(row=2, column=1)
        
        botoes[index]["labels"]["nome_projeto"].grid_forget()
        botoes[index]["entries"]["nome_projeto"].grid(row=3, column=1)
        
        botoes[index]["labels"]["nota_pesquisa"].grid_forget()
        botoes[index]["entries"]["nota_pesquisa"].grid(row=4, column=1)
        
        botoes[index]["labels"]["nome_avaliador"].grid_forget()
        botoes[index]["entries"]["nome_avaliador"].grid(row=5, column=1)
        
        botoes[index]["labels"]["email_avaliador"].grid_forget()
        botoes[index]["entries"]["email_avaliador"].grid(row=6, column=1)
        
        botoes[index]["labels"]["telefone"].grid_forget()
        botoes[index]["entries"]["telefone"].grid(row=7, column=1)

        botoes[index]["edit_button"].config(text="Salvar")
        botoes[index]["is_editing"] = True
    else:
        # Salva as alterações no projeto
        projeto["analista"] = botoes[index]["entries"]["analista"].get()
        projeto["n_project"] = botoes[index]["entries"]["n_project"].get()
        projeto["nome_projeto"] = botoes[index]["entries"]["nome_projeto"].get()
        projeto["nota_pesquisa"] = botoes[index]["entries"]["nota_pesquisa"].get()
        projeto["nome_avaliador"] = botoes[index]["entries"]["nome_avaliador"].get()
        projeto["email_avaliador"] = botoes[index]["entries"]["email_avaliador"].get()
        projeto["telefone"] = botoes[index]["entries"]["telefone"].get()

        salvar_dados()

        # Volta para o modo de exibição
        botoes[index]["entries"]["analista"].grid_forget()
        botoes[index]["labels"]["analista"].config(text=f"Analista: {projeto['analista']}")
        botoes[index]["labels"]["analista"].grid(row=1, column=1)
        
        botoes[index]["entries"]["n_project"].grid_forget()
        botoes[index]["labels"]["n_project"].config(text=f"N° Project: {projeto['n_project']}")
        botoes[index]["labels"]["n_project"].grid(row=2, column=1)
        
        botoes[index]["entries"]["nome_projeto"].grid_forget()
        botoes[index]["labels"]["nome_projeto"].config(text=f"Nome do Projeto: {projeto['nome_projeto']}")
        botoes[index]["labels"]["nome_projeto"].grid(row=3, column=1)
        
        botoes[index]["entries"]["nota_pesquisa"].grid_forget()
        botoes[index]["labels"]["nota_pesquisa"].config(text=f"Nota da Pesquisa: {projeto['nota_pesquisa']}")
        botoes[index]["labels"]["nota_pesquisa"].grid(row=4, column=1)
        
        botoes[index]["entries"]["nome_avaliador"].grid_forget()
        botoes[index]["labels"]["nome_avaliador"].config(text=f"Avaliador: {projeto['nome_avaliador']}")
        botoes[index]["labels"]["nome_avaliador"].grid(row=5, column=1)
        
        botoes[index]["entries"]["email_avaliador"].grid_forget()
        botoes[index]["labels"]["email_avaliador"].config(text=f"Email: {projeto['email_avaliador']}")
        botoes[index]["labels"]["email_avaliador"].grid(row=6, column=1)
        
        botoes[index]["entries"]["telefone"].grid_forget()
        botoes[index]["labels"]["telefone"].config(text=f"Telefone: {projeto['telefone']}")
        botoes[index]["labels"]["telefone"].grid(row=7, column=1)

        botoes[index]["edit_button"].config(text="Editar")
        botoes[index]["is_editing"] = False

# Função para adicionar um novo projeto
def adicionar_pesquisa():
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

# Função para exibir os projetos de forma organizada
def exibir_projetos():
    for widget in canvas_frame.winfo_children():
        widget.destroy()
    global botoes
    botoes = []
    for i, projeto in enumerate(clientes):
        color = "green" if projeto["aprovado_suporte"] else "red"
        
        # Faixa para cada projeto
        frame = tk.Frame(canvas_frame, bg=color, padx=10, pady=5, relief="ridge", bd=2)
        frame.pack(fill="x", pady=5, padx=5)

        # Campos de exibição e edição de cada atributo do projeto
        labels = {}
        entries = {}

        font_label = ("Helvetica", 9, "bold")
        labels["analista"] = tk.Label(frame, text=f"Analista: {projeto['analista']}", bg=color, font=font_label, fg="white")
        labels["analista"].grid(row=1, column=0, sticky="w")
        entries["analista"] = tk.Entry(frame)
        entries["analista"].insert(0, projeto["analista"])

        labels["n_project"] = tk.Label(frame, text=f"N° Project: {projeto['n_project']}", bg=color, font=font_label, fg="white")
        labels["n_project"].grid(row=2, column=0, sticky="w")
        entries["n_project"] = tk.Entry(frame)
        entries["n_project"].insert(0, projeto["n_project"])

        labels["nome_projeto"] = tk.Label(frame, text=f"Nome do Projeto: {projeto['nome_projeto']}", bg=color, font=font_label, fg="white")
        labels["nome_projeto"].grid(row=3, column=0, sticky="w")
        entries["nome_projeto"] = tk.Entry(frame)
        entries["nome_projeto"].insert(0, projeto["nome_projeto"])

        labels["nota_pesquisa"] = tk.Label(frame, text=f"Nota da Pesquisa: {projeto['nota_pesquisa']}", bg=color, font=font_label, fg="white")
        labels["nota_pesquisa"].grid(row=4, column=0, sticky="w")
        entries["nota_pesquisa"] = tk.Entry(frame)
        entries["nota_pesquisa"].insert(0, projeto["nota_pesquisa"])

        labels["nome_avaliador"] = tk.Label(frame, text=f"Avaliador: {projeto['nome_avaliador']}", bg=color, font=font_label, fg="white")
        labels["nome_avaliador"].grid(row=5, column=0, sticky="w")
        entries["nome_avaliador"] = tk.Entry(frame)
        entries["nome_avaliador"].insert(0, projeto["nome_avaliador"])

        labels["email_avaliador"] = tk.Label(frame, text=f"Email: {projeto['email_avaliador']}", bg=color, font=font_label, fg="white")
        labels["email_avaliador"].grid(row=6, column=0, sticky="w")
        entries["email_avaliador"] = tk.Entry(frame)
        entries["email_avaliador"].insert(0, projeto["email_avaliador"])

        labels["telefone"] = tk.Label(frame, text=f"Telefone: {projeto['telefone']}", bg=color, font=font_label, fg="white")
        labels["telefone"].grid(row=7, column=0, sticky="w")
        entries["telefone"] = tk.Entry(frame)
        entries["telefone"].insert(0, projeto["telefone"])

        # Botões de status, edição e exclusão
        botao_respondido = tk.Button(frame, text="Respondido", command=lambda idx=i: marcar_como_respondido(idx), bg="green")
        botao_respondido.grid(row=0, column=1, padx=2)

        botao_nao_respondido = tk.Button(frame, text="Não Respondido", command=lambda idx=i: marcar_como_nao_respondido(idx), bg="red")
        botao_nao_respondido.grid(row=0, column=2, padx=2)

        edit_button = tk.Button(frame, text="Editar", command=lambda idx=i: editar_projeto(idx), bg="blue", fg="white")
        edit_button.grid(row=0, column=3, padx=2)

        botoes.append({"frame": frame, "labels": labels, "entries": entries, "edit_button": edit_button})

# Função para rolagem do mouse no Canvas
def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# Inicializando o programa
clientes = carregar_dados()

# Interface Gráfica com Tkinter
root = tk.Tk()
root.title("Controle de Pesquisa de Satisfação")
root.geometry("800x600")

frame_form = tk.Frame(root)
frame_form.pack(pady=10)

# Campos de entrada
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

# Botões para adicionar e salvar projetos
botao_adicionar = tk.Button(frame_form, text="Adicionar Pesquisa", command=adicionar_pesquisa)
botao_adicionar.grid(row=7, columnspan=2, pady=10)

botao_salvar = tk.Button(root, text="Salvar Dados no JSON", command=salvar_dados, bg="orange")
botao_salvar.pack(pady=5)

# Frame para conter o canvas com a barra de rolagem
scroll_frame = tk.Frame(root)
scroll_frame.pack(fill="both", expand=True)

# Canvas e Scrollbar
canvas = tk.Canvas(scroll_frame)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

# Frame para conter os projetos
canvas_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

canvas_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.bind_all("<MouseWheel>", on_mouse_wheel)

# Exibir projetos ao iniciar o programa
exibir_projetos()

root.mainloop()
