import tkinter as tk
from tkinter import messagebox
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import random
import string

# Função para gerar senha forte
def generate_password(length=14):
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)
    
    remaining_length = length - 4
    all_characters = string.ascii_letters + string.digits + string.punctuation
    remaining_chars = ''.join(random.choice(all_characters) for _ in range(remaining_length))
    
    password = upper + lower + digit + special + remaining_chars
    password = ''.join(random.sample(password, len(password)))
    
    return password

# Função para gerar múltiplas senhas
def generate_multiple_passwords():
    num_passwords = len(users)
    password_length = int(password_length_spinbox.get())
    global passwords
    passwords = [generate_password(password_length) for _ in range(num_passwords)]
    passwords_text.delete(1.0, tk.END)
    passwords_text.insert(tk.END, "\n".join(passwords))
    merge_users_passwords(users)

# Função para mesclar automaticamente usuários e senhas
def merge_users_passwords(users_list):
    global passwords
    if len(users_list) != len(passwords):
        messagebox.showwarning("Erro", "O número de usuários e senhas não corresponde.")
        return
    
    merged_list = []
    for user, password in zip(users_list, passwords):
        merged_list.append(f"{user}\n{password}\n")

    merged_text.delete(1.0, tk.END)
    merged_text.insert(tk.END, "\n".join(merged_list))

# Função para formatar nomes de usuários com a empresa e o sufixo
def format_username(index):
    company_name = company_entry.get().strip()
    return f"{company_name}{str(index).zfill(2)}@pfsense.local"

# Função para criar usuários automaticamente com base na quantidade especificada
def create_users():
    global users
    company_name = company_entry.get().strip()
    num_users = int(num_users_spinbox.get())

    if not company_name:
        messagebox.showwarning("Atenção", "Por favor, insira o nome da empresa.")
        return
    
    users = [format_username(i + 1) for i in range(num_users)]
    users_text.delete(1.0, tk.END)
    users_text.insert(tk.END, "\n".join(users))
    generate_multiple_passwords()

# Função chamada quando o botão é clicado para gerar documento
def generate_doc():
    users_passwords_text = merged_text.get("1.0", tk.END).strip()

    if not users_passwords_text:
        messagebox.showerror("Erro", "Por favor, insira os usuários e senhas.")
        return

    users_passwords = []
    current_user = None
    current_password = None

    lines = users_passwords_text.splitlines()

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if current_user is None:
            current_user = line
        elif current_password is None:
            current_password = line

        if current_user and current_password:
            users_passwords.append((current_user, current_password))
            current_user = None
            current_password = None

    if current_user is not None:
        users_passwords.append((current_user, "(sem senha)"))

    create_vpn_doc(users_passwords)

# Interface gráfica
root = tk.Tk()
root.title("Gerador de Documento com Usuário e Senha")
root.geometry("750x600")

# Linha para configuração do nome da empresa e quantidade de usuários
tk.Label(root, text="Nome da Empresa:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
company_entry = tk.Entry(root, width=15)
company_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

create_users_button = tk.Button(root, text="Criar Usuários", command=create_users)
create_users_button.grid(row=0, column=4, padx=10, pady=5, sticky="w")

tk.Label(root, text="Quantidade de Usuários:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
num_users_spinbox = tk.Spinbox(root, from_=1, to=100, width=5)
num_users_spinbox.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Linha para configuração do comprimento da senha e botão de geração
tk.Label(root, text="Comprimento da Senha:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
password_length_spinbox = tk.Spinbox(root, from_=8, to=20, width=5)
password_length_spinbox.grid(row=2, column=1, padx=5, pady=5, sticky="w")

generate_button = tk.Button(root, text="Gerar Senhas", command=generate_multiple_passwords)
generate_button.grid(row=2, column=4, padx=10, pady=5, sticky="w")

# Campos de texto e labels
tk.Label(root, text="Senhas Geradas").grid(row=3, column=0, padx=10, pady=5)
passwords_text = tk.Text(root, height=10, width=30)
passwords_text.grid(row=4, column=0, padx=10, pady=10)

# Título e campo de usuários com a legenda em vermelho
tk.Label(root, text="Usuários").grid(row=3, column=1, padx=10, pady=(5, 0))
users_text = tk.Text(root, height=10, width=30)
users_text.grid(row=4, column=1, padx=10, pady=(0, 5))
tk.Label(root, text="Cole aqui os usuários para serem mesclados", fg="red", font=("TkDefaultFont", 8)).grid(row=5, column=1, padx=10, pady=(0, 5), sticky="n")

# Campo para exibir a mesclagem
tk.Label(root, text="Mesclagem de Usuários e Senhas").grid(row=6, column=0, columnspan=2, padx=10, pady=5)
merged_text = tk.Text(root, height=10, width=50)
merged_text.grid(row=7, column=0, columnspan=5, padx=10, pady=10)

# Botão para gerar o documento final
doc_button = tk.Button(root, text="Gerar Documento", command=generate_doc)
doc_button.grid(row=8, column=0, columnspan=5, pady=20)

users = []
passwords = []

root.mainloop()
