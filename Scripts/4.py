import tkinter as tk
from tkinter import messagebox, StringVar, IntVar, Radiobutton, Checkbutton
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
    num_passwords = int(num_passwords_var.get())
    length = int(password_length_var.get())
    global passwords
    passwords = [generate_password(length) for _ in range(num_passwords)]
    passwords_text.delete(1.0, tk.END)
    passwords_text.insert(tk.END, "\n".join(passwords))

# Função chamada automaticamente quando o usuário termina de editar o campo de usuários
def on_users_text_change(event):
    global users
    users = users_text.get(1.0, tk.END).strip().split('\n')  # Pega o texto e divide por linha

    if users:
        # Gerar senhas se necessário
        if len(users) > len(passwords):
            generate_multiple_passwords()

        # Mesclar automaticamente usuários e senhas
        merge_users_passwords(users)

# Função para mesclar automaticamente usuários e senhas no formato desejado
def merge_users_passwords(users_list):
    global passwords
    if len(users_list) != len(passwords):
        messagebox.showwarning("Erro", "O número de usuários e senhas não corresponde.")
        return
    
    merged_list = []
    for user, password in zip(users_list, passwords):
        merged_list.append(f"===========||==========\n{user.strip()}\n{password}\n===========||==========")

    merged_text.delete(1.0, tk.END)
    merged_text.insert(tk.END, "\n".join(merged_list))  # Insere com um layout visual de separação

# Janela principal
root = tk.Tk()
root.title("Gerador de Senhas e Usuários")
root.geometry("800x600")  # Aumentando o tamanho da janela

# Seletor de número de caracteres
tk.Label(root, text="Número de caracteres").grid(row=0, column=0, padx=10, pady=10, sticky="w")
password_length_var = StringVar(value="12")
tk.Radiobutton(root, text="8", variable=password_length_var, value="8").grid(row=1, column=0, sticky="w")
tk.Radiobutton(root, text="12", variable=password_length_var, value="12").grid(row=1, column=1, sticky="w")
tk.Radiobutton(root, text="16", variable=password_length_var, value="16").grid(row=1, column=2, sticky="w")
tk.Radiobutton(root, text="32", variable=password_length_var, value="32").grid(row=1, column=3, sticky="w")
tk.Radiobutton(root, text="50", variable=password_length_var, value="50").grid(row=1, column=4, sticky="w")

# Campo para número de senhas
tk.Label(root, text="Quantidade de senhas a gerar").grid(row=2, column=0, padx=10, pady=10, sticky="w")
num_passwords_var = tk.StringVar(value="10")
tk.Entry(root, textvariable=num_passwords_var, width=5).grid(row=2, column=1, padx=10, pady=10)

# Botão para gerar senhas
generate_button = tk.Button(root, text="Gerar Senhas", width=20, height=2, command=generate_multiple_passwords)
generate_button.grid(row=3, column=0, padx=10, pady=10)

# Título para o primeiro quadrado "Senhas"
tk.Label(root, text="Senhas").grid(row=4, column=0, padx=10, pady=10, sticky="w")

# Campo para exibir as senhas geradas
passwords_text = tk.Text(root, height=10, width=30)
passwords_text.grid(row=5, column=0, padx=10, pady=10)

# Título para o segundo quadrado "Usuários"
tk.Label(root, text="Usuários").grid(row=4, column=1, padx=10, pady=10, sticky="w")

# Campo para inserir os usuários diretamente
users_text = tk.Text(root, height=10, width=30)
users_text.grid(row=5, column=1, padx=10, pady=10)

# Vincular o evento de alteração do campo de texto dos usuários
users_text.bind("<KeyRelease>", on_users_text_change)

# Título para o terceiro quadrado "Concatenado"
tk.Label(root, text="Concatenado").grid(row=6, column=0, padx=10, pady=10, sticky="w")

# Campo para exibir a mescla de usuários e senhas
merged_text = tk.Text(root, height=10, width=50)
merged_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Variáveis globais para armazenar os usuários e senhas
users = []
passwords = []

root.mainloop()
