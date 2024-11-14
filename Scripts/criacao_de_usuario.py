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

# Função para criar usuários automaticamente com senhas
def create_users_with_passwords():
    num_users = simpledialog.askinteger("Número de Usuários", "Quantos usuários deseja criar?")
    client_name = simpledialog.askstring("Nome do Cliente", "Digite o nome do cliente")
    
    if not num_users or not client_name:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
        return

    global users, passwords
    users = [f"{client_name}Usuario{i+1}" for i in range(num_users)]
    passwords = [generate_password() for _ in range(num_users)]

    merge_users_passwords(users)

# Função para mesclar automaticamente usuários e senhas no formato desejado
def merge_users_passwords(users_list):
    global passwords
    merged_list = []
    for user, password in zip(users_list, passwords):
        merged_list.append(f"--------------------------\n{user}\n{password}\n--------------------------")

    merged_text.delete(1.0, tk.END)
    merged_text.insert(tk.END, "\n".join(merged_list))  # Insere com layout visual de separação

# Janela principal
root = tk.Tk()
root.title("Gerador de Usuários e Senhas")
root.geometry("600x500")  # Aumentando o tamanho da janela

# Botão para gerar usuários e senhas com base no cliente
create_button = tk.Button(root, text="Criar Usuários", width=20, height=2, command=create_users_with_passwords)
create_button.grid(row=0, column=0, padx=10, pady=10)

# Campo para exibir a mescla de usuários e senhas
merged_text = tk.Text(root, height=20, width=60)
merged_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Variáveis globais para armazenar os usuários e senhas
users = []
passwords = []

root.mainloop()
