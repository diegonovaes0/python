import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import string

# Função para gerar uma senha de 14 caracteres
def generate_password(length=14):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Função para gerar várias senhas
def generate_multiple_passwords():
    num_passwords = simpledialog.askinteger("Quantas Senhas?", "Quantas senhas você deseja gerar?")
    
    if num_passwords:
        global passwords
        passwords = [generate_password() for _ in range(num_passwords)]
        passwords_text.delete(1.0, tk.END)
        passwords_text.insert(tk.END, "\n".join(passwords))

# Função para inserir usuários
def insert_users():
    global users
    users = simpledialog.askstring("Usuários", "Digite os nomes dos usuários separados por vírgula")
    
    if users:
        users_list = users.split(',')
        users_text.delete(1.0, tk.END)
        users_text.insert(tk.END, "\n".join(users_list))

# Função para mesclar usuários e senhas
def merge_users_passwords():
    if not users or not passwords:
        messagebox.showwarning("Aviso", "Por favor, insira os usuários e gere as senhas primeiro.")
        return
    
    users_list = users.split(',')
    if len(users_list) != len(passwords):
        messagebox.showwarning("Erro", "O número de usuários e senhas não corresponde.")
        return
    
    merged_list = [f"{user.strip()}: {password}" for user, password in zip(users_list, passwords)]
    merged_text.delete(1.0, tk.END)
    merged_text.insert(tk.END, "\n".join(merged_list))

# Janela principal
root = tk.Tk()
root.title("Gerador de Senhas e Usuários")
root.geometry("600x400")

# Botão para gerar senhas
generate_button = tk.Button(root, text="Gerar Senhas", width=20, height=2, command=generate_multiple_passwords)
generate_button.grid(row=0, column=0, padx=10, pady=10)

# Campo para exibir as senhas geradas
passwords_text = tk.Text(root, height=10, width=30)
passwords_text.grid(row=1, column=0, padx=10, pady=10)

# Botão para inserir usuários
users_button = tk.Button(root, text="Inserir Usuários", width=20, height=2, command=insert_users)
users_button.grid(row=0, column=1, padx=10, pady=10)

# Campo para exibir os usuários inseridos
users_text = tk.Text(root, height=10, width=30)
users_text.grid(row=1, column=1, padx=10, pady=10)

# Botão para mesclar usuários e senhas
merge_button = tk.Button(root, text="Mesclar Usuários e Senhas", width=20, height=2, command=merge_users_passwords)
merge_button.grid(row=2, column=0, padx=10, pady=10)

# Campo para exibir a mescla de usuários e senhas
merged_text = tk.Text(root, height=10, width=30)
merged_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Variáveis globais para armazenar os usuários e senhas
users = ""
passwords = []

root.mainloop()
