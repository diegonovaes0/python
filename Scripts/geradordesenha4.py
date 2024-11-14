import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import string

# Função para gerar uma senha forte com os critérios necessários
def generate_password(length=14):
    if length < 8:
        length = 8  # Garantir que a senha tenha pelo menos 8 caracteres
    
    # Garantir ao menos uma letra maiúscula, uma minúscula, um número e um caractere especial
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)
    
    # Preencher o restante com uma combinação de todos os caracteres
    remaining_length = length - 4
    all_characters = string.ascii_letters + string.digits + string.punctuation
    remaining_chars = ''.join(random.choice(all_characters) for _ in range(remaining_length))
    
    # Combinar todos os caracteres e embaralhar
    password = upper + lower + digit + special + remaining_chars
    password = ''.join(random.sample(password, len(password)))  # Embaralhar a senha
    
    return password

# Função para gerar várias senhas
def generate_multiple_passwords():
    num_passwords = simpledialog.askinteger("Quantas Senhas?", "Quantas senhas você deseja gerar?")
    
    if num_passwords:
        global passwords
        passwords = [generate_password() for _ in range(num_passwords)]
        passwords_text.delete(1.0, tk.END)
        passwords_text.insert(tk.END, "\n".join(passwords))

# Função para inserir usuários (usando quebra de linha em vez de vírgulas)
def insert_users():
    global users
    global passwords
    users = simpledialog.askstring("Usuários", "Digite os nomes dos usuários, um por linha")
    
    if users:
        users_list = users.split('\n')  # Quebra cada linha e usa como um novo usuário
        users_text.delete(1.0, tk.END)
        users_text.insert(tk.END, "\n".join(users_list))

        # Gerar senhas automaticamente se o número de usuários for maior que o número de senhas
        if len(users_list) > len(passwords):
            passwords = [generate_password() for _ in range(len(users_list))]

        # Mesclar automaticamente usuários e senhas
        merge_users_passwords(users_list)

# Função para mesclar automaticamente usuários e senhas
def merge_users_passwords(users_list):
    global passwords
    if len(users_list) != len(passwords):
        messagebox.showwarning("Erro", "O número de usuários e senhas não corresponde.")
        return
    
    merged_list = [f"{user.strip()}: {password}" for user, password in zip(users_list, passwords)]
    merged_text.delete(1.0, tk.END)
    merged_text.insert(tk.END, "\n".join(merged_list))

# Janela principal
root = tk.Tk()
root.title("Gerador de Senhas e Usuários")
root.geometry("600x500")  # Aumentando o tamanho da janela

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

# Campo para exibir a mescla de usuários e senhas
merged_text = tk.Text(root, height=10, width=50)
merged_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Variáveis globais para armazenar os usuários e senhas
users = ""
passwords = []

root.mainloop()
