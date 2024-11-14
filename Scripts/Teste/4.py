import tkinter as tk
from tkinter import messagebox
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import random
import string

# Funções de manipulação do documento e formatação dos usuários e senhas

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

# Função para formatar os nomes dos usuários
def format_username(username):
    words = username.split()
    return ''.join(word.capitalize() for word in words)

# Função para atualizar a lista de usuários e acionar a mesclagem
def on_users_text_change(event):
    global users
    users = [format_username(user.strip()) for user in users_text.get(1.0, tk.END).strip().split('\n') if user.strip()]
    generate_multiple_passwords()

# Interface gráfica
root = tk.Tk()
root.title("Gerador de Documento com Usuário e Senha")
root.geometry("650x600")

tk.Label(root, text="Comprimento da Senha:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
password_length_spinbox = tk.Spinbox(root, from_=8, to=20, width=5)
password_length_spinbox.grid(row=0, column=1, padx=10, pady=5)

generate_button = tk.Button(root, text="Gerar Senhas", width=20, height=2, command=generate_multiple_passwords)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Senhas Geradas").grid(row=2, column=0, padx=10, pady=5)
passwords_text = tk.Text(root, height=10, width=30)
passwords_text.grid(row=3, column=0, padx=10, pady=10)

# Título para o campo de usuários
tk.Label(root, text="Usuários").grid(row=2, column=1, padx=10, pady=5)
users_text = tk.Text(root, height=10, width=30)
users_text.grid(row=3, column=1, padx=10, pady=(0, 5))  # Ajustado para reduzir o espaçamento inferior
users_text.bind("<KeyRelease>", on_users_text_change)

# Legenda em vermelho logo abaixo do campo "Usuários"
tk.Label(root, text="Cole aqui os usuários para serem mesclados", fg="red", font=("TkDefaultFont", 8)).grid(row=4, column=1, padx=10, pady=(0, 15), sticky="n")

# Campo para exibir a mesclagem
tk.Label(root, text="Mesclagem de Usuários e Senhas").grid(row=5, column=0, columnspan=2, padx=10, pady=5)
merged_text = tk.Text(root, height=10, width=50)
merged_text.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

doc_button = tk.Button(root, text="Gerar Documento", command=generate_doc)
doc_button.grid(row=7, column=0, columnspan=2, pady=20)

users = []
passwords = []

root.mainloop()
