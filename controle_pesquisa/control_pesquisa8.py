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

# Função para salvar todas as pesquisas no arquivo JSON ao clicar em "Salvar" ou ao sair do programa
def salvar_dados():
    # Pergunta o caminho onde salvar, com o caminho atual como padrão
    filepath = filedialog.asksaveasfilename(defaultextension=".json", initialfile=DATA_FILE, filetypes=[("JSON files", "*.json")])
    if filepath:
        with open(filepath, "w") as file:
            json.dump(clientes, file, indent=4)
        messagebox.showinfo("Sucesso", "Dados salvos com sucesso no arquivo JSON.")

# Função para carregar dados de um arquivo JSON específico
def carregar_json():
    filepath = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if filepath:
        with open(filepath, "r") as file:
            dados = json.load(file)
            clientes.extend(dados)  # Adiciona dados carregados à lista de clientes existente
        exibir_projetos()
        messagebox.showinfo("Sucesso", "Dados carregados com sucesso do arquivo JSON.")

# Função para atualizar a exibição dos botões e cores com base na resposta
def atualizar_botoes():
    for i, cliente in enumerate(clientes):
        color = "green" if cliente["aprovado_suporte"] else "red"
        botoes[i]["frame"].config(bg=color)
        botoes[i]["labels"]["nome_projeto"].config(bg=color, font=("Helvetica", 12, "bold"), fg="white", anchor="center")  # Título destacado e centralizado
        for label in botoes[i]["labels"].values():
            label.config(bg=color, fg="white")  # Cor uniforme para fundo e texto

# Função para marcar como respondido e mudar a cor de fundo
def marcar_como_respondido(index):
    clientes[index]["aprovado_suporte"] = True
    atualizar_botoes()

# Função para marcar como não respondido e mudar a cor de fundo
def marcar_como_nao_respondido(index):
    clientes[index]["aprovado_suporte"] = False
    atualizar_botoes()

# Função para alternar entre modo de edição e modo de exibição da pesquisa
def editar_projeto(index):
    projeto = clientes[index]
    frame = botoes[index]["frame"]
    is_editing = botoes[index].get("is_editing", False)

    # Alterna para o modo de edição
    if not is_editing:
        for key, label in botoes[index]["labels"].items():
            label.grid_forget()
            botoes[index]["entries"][key].grid(row=botoes[index]["positions"][key], column=1, sticky="w")
        botoes[index]["edit_button"].config(text="Salvar")
        botoes[index]["is_editing"] = True
    else:
        # Salva as alterações no projeto em memória
        for key in botoes[index]["entries"]:
            projeto[key] = botoes[index]["entries"][key].get()

        # Volta para o modo de exibição
        for key, entry in botoes[index]["entries"].items():
            entry.grid_forget()
            botoes[index]["labels"][key].config(text=f"{key.capitalize()}: {projeto[key]}")
            botoes[index]["labels"][key].grid(row=botoes[index]["positions"][key], column=1, sticky="w")

        botoes[index]["edit_button"].config(text="Editar")
        botoes[index]["is_editing"] = False

# Função para excluir um projeto
def excluir_projeto(index):
    if messagebox.askyesno("Confirmar Exclusão", "Tem certeza de que deseja excluir este projeto?"):
        del clientes[index]
        exibir_projetos()

# Função para adicionar um novo projeto (em memória)
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
        exibir_projetos()
        for entry in [entry_analista, entry_n_project, entry_nome_projeto, entry_nota_pesquisa, entry_nome_avaliador, entry_email_avaliador, entry_telefone]:
            entry.delete(0, tk.END)
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
        
        # Faixa para cada projeto com título destacado do nome do projeto
        frame = tk.Frame(canvas_frame, bg=color, padx=10, pady=5, relief="ridge", bd=2)
        frame.pack(fill="x", pady=5, padx=5, expand=True)

        # Campos de exibição e edição de cada atributo do projeto
        labels = {}
        entries = {}
        positions = {}
        font_label = ("Helvetica", 9, "bold")

        # Título com o nome do projeto, centralizado e em destaque
        labels["nome_projeto"] = tk.Label(frame, text=f"{projeto['nome_projeto']}", bg=color, font=("Helvetica", 12, "bold"), fg="white")
        labels["nome_projeto"].grid(row=0, column=0, columnspan=3, sticky="nsew")
        frame.grid_columnconfigure(0, weight=1)  # Centralizar o título no frame

        row = 1
        for key, value in projeto.items():
            if key not in ["aprovado_suporte", "data", "hora", "nome_projeto"]:
                labels[key] = tk.Label(frame, text=f"{key.capitalize()}: {value}", bg=color, font=font_label, fg="white")
                labels[key].grid(row=row, column=0, sticky="w")
                entries[key] = tk.Entry(frame)
                entries[key].insert(0, value)
                positions[key] = row
                row += 1

        # Botões de status, edição e exclusão no rodapé
        button_frame = tk.Frame(frame, bg=color)
        button_frame.grid(row=row, column=0, columnspan=3, pady=5, sticky="ew")

        botao_respondido = tk.Button(button_frame, text="Respondido", command=lambda idx=i: marcar_como_respondido(idx), bg="green")
        botao_respondido.pack(side="left", padx=2)

        botao_nao_respondido = tk.Button(button_frame, text="Não Respondido", command=lambda idx=i: marcar_como_nao_respondido(idx), bg="red")
        botao_nao_respondido.pack(side="left", padx=2)

        edit_button = tk.Button(button_frame, text="Editar", command=lambda idx=i: editar_projeto(idx), bg="blue", fg="white")
        edit_button.pack(side="left", padx=2)

        botao_excluir = tk.Button(button_frame, text="Excluir", command=lambda idx=i: excluir_projeto(idx), bg="red", fg="white")
        botao_excluir.pack(side="left", padx=2)

        botoes.append({"frame": frame, "labels": labels, "entries": entries, "edit_button": edit_button, "positions": positions})

# Função para rolagem do mouse no Canvas
def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# Inicializando o programa
clientes = carregar_dados()

# Interface Gráfica com Tkinter
root = tk.Tk()
root.title("Controle de Pesquisa de Satisfação")
root.geometry("1024x700")  # Ajuste da janela para mostrar tudo

# Frame para entrada de dados
frame_form = tk.Frame(root, relief="solid", bd=1, padx=10, pady=10)
frame_form.pack(side="left", fill="y", padx=10, pady=10)

# Campos de entrada de dados
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

# Botão para adicionar o projeto à lista em memória
botao_adicionar = tk.Button(frame_form, text="Adicionar Pesquisa", command=adicionar_pesquisa)
botao_adicionar.grid(row=7, columnspan=2, pady=10)

# Botões de Salvar e Carregar JSON
botao_salvar = tk.Button(frame_form, text="Salvar Dados no JSON", command=salvar_dados, bg="orange")
botao_salvar.grid(row=8, columnspan=2, pady=5)

botao_carregar = tk.Button(frame_form, text="Carregar JSON", command=carregar_json, bg="lightblue")
botao_carregar.grid(row=9, columnspan=2, pady=5)

# Frame para lista de pesquisas com barra de rolagem
frame_lista = tk.Frame(root, relief="solid", bd=1, padx=10, pady=10)
frame_lista.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Canvas e Scrollbar para exibir a lista de pesquisas
canvas = tk.Canvas(frame_lista)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_lista, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

# Frame interno do Canvas para manter a lista de pesquisas
canvas_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

# Atualizar a área de rolagem do Canvas conforme o tamanho do conteúdo
canvas_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Função para rolagem do Canvas com o mouse
canvas.bind_all("<MouseWheel>", on_mouse_wheel)

# Exibir projetos ao iniciar o programa
exibir_projetos()

root.mainloop()
