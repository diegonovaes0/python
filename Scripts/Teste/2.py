import tkinter as tk
from tkinter import messagebox
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

# Função para gerar várias senhas com o comprimento selecionado
def generate_multiple_passwords():
    num_passwords = len(users)
    password_length = int(password_length_spinbox.get())
    global passwords
    passwords = [generate_password(password_length) for _ in range(num_passwords)]
    passwords_text.delete(1.0, tk.END)
    passwords_text.insert(tk.END, "\n".join(passwords))

# Função chamada automaticamente quando o usuário termina de editar o campo de usuários
def on_users_text_change(event):
    global users
    global passwords
    # Captura os usuários, removendo linhas em branco
    users = [user.strip() for user in users_text.get(1.0, tk.END).strip().split('\n') if user.strip()]

    # Limpa as senhas e gera novas se o número de usuários mudar
    passwords = []
    if users:
        generate_multiple_passwords()
        merge_users_passwords(users)

# Função para mesclar automaticamente usuários e senhas no formato desejado
def merge_users_passwords(users_list):
    global passwords
    if len(users_list) != len(passwords):
        messagebox.showwarning("Erro", "O número de usuários e senhas não corresponde.")
        return
    
    merged_list = []
    for user, password in zip(users_list, passwords):
        merged_list.append(f"{user}\n{password}\n")

    merged_text.delete(1.0, tk.END)
    merged_text.insert(tk.END, "\n".join(merged_list))  # Insere com uma linha em branco entre os pares

# Janela principal
root = tk.Tk()
root.title("Gerador de Senhas e Usuários")
root.geometry("650x600")  # Aumentando o tamanho da janela

# Botão Spinbox para selecionar o comprimento das senhas
tk.Label(root, text="Comprimento da Senha:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
password_length_spinbox = tk.Spinbox(root, from_=8, to=20, width=5)  # Limite de comprimento entre 8 e 20 caracteres
password_length_spinbox.grid(row=0, column=1, padx=10, pady=5)

# Botão para gerar senhas manualmente, se necessário
generate_button = tk.Button(root, text="Gerar Senhas", width=20, height=2, command=generate_multiple_passwords)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Título para campo de senhas
tk.Label(root, text="Senhas Geradas").grid(row=2, column=0, padx=10, pady=5)
# Campo para exibir as senhas geradas
passwords_text = tk.Text(root, height=10, width=30)
passwords_text.grid(row=3, column=0, padx=10, pady=10)

# Título para campo de usuários
tk.Label(root, text="Usuários").grid(row=2, column=1, padx=10, pady=5)
# Campo para inserir os usuários diretamente
users_text = tk.Text(root, height=10, width=30)
users_text.grid(row=3, column=1, padx=10, pady=10)

# Vincular o evento de alteração do campo de texto dos usuários
users_text.bind("<KeyRelease>", on_users_text_change)

# Título para campo de mesclagem
tk.Label(root, text="Mesclagem de Usuários e Senhas").grid(row=4, column=0, columnspan=2, padx=10, pady=5)
# Campo para exibir a mescla de usuários e senhas
merged_text = tk.Text(root, height=10, width=50)
merged_text.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# Variáveis globais para armazenar os usuários e senhas
users = []
passwords = []

root.mainloop()
