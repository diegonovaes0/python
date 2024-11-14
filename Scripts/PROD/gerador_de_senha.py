import tkinter as tk
from tkinter import messagebox, simpledialog, IntVar, Checkbutton
import random
import string

# Função para gerar uma senha com os critérios selecionados
def generate_password(length, use_upper, use_lower, use_digits, use_special, exclude_confusing):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*()_+-=[]{}|;:',.<>/?~"
    
    if exclude_confusing:
        characters = characters.replace('I', '').replace('l', '').replace('1', '')
        characters = characters.replace('O', '').replace('o', '').replace('0', '')

    if len(characters) == 0:
        return ""
    
    return ''.join(random.choice(characters) for _ in range(length))

# Função para gerar várias senhas
def generate_multiple_passwords():
    num_passwords = int(num_passwords_var.get())
    length = int(password_length_var.get())
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()
    exclude_confusing = exclude_confusing_var.get()

    global passwords
    passwords = [generate_password(length, use_upper, use_lower, use_digits, use_special, exclude_confusing) for _ in range(num_passwords)]
    
    passwords_text.delete(1.0, tk.END)
    passwords_text.insert(tk.END, "\n".join(passwords))

# Função para copiar todas as senhas geradas para a área de transferência
def copy_all_passwords():
    root.clipboard_clear()
    root.clipboard_append("\n".join(passwords))
    messagebox.showinfo("Copiar", "Senhas copiadas para a área de transferência!")

# Janela principal
root = tk.Tk()
root.title("Gerador de Senhas Personalizadas")
root.geometry("800x600")  # Aumentando o tamanho da janela

# Labels e Widgets para as opções de personalização das senhas
tk.Label(root, text="Número de caracteres").grid(row=0, column=0, padx=10, pady=10, sticky="w")

password_length_var = tk.StringVar(value="12")
tk.Radiobutton(root, text="8", variable=password_length_var, value="8").grid(row=1, column=0, sticky="w")
tk.Radiobutton(root, text="12", variable=password_length_var, value="12").grid(row=1, column=1, sticky="w")
tk.Radiobutton(root, text="16", variable=password_length_var, value="16").grid(row=1, column=2, sticky="w")
tk.Radiobutton(root, text="32", variable=password_length_var, value="32").grid(row=1, column=3, sticky="w")
tk.Radiobutton(root, text="50", variable=password_length_var, value="50").grid(row=1, column=4, sticky="w")

# Caracteres para incluir
tk.Label(root, text="Caracteres para incluir").grid(row=2, column=0, padx=10, pady=10, sticky="w")

upper_var = IntVar(value=1)
Checkbutton(root, text="Letras maiúsculas", variable=upper_var).grid(row=3, column=0, sticky="w")

lower_var = IntVar(value=1)
Checkbutton(root, text="Letras minúsculas", variable=lower_var).grid(row=3, column=1, sticky="w")

digits_var = IntVar(value=1)
Checkbutton(root, text="Números", variable=digits_var).grid(row=3, column=2, sticky="w")

special_var = IntVar(value=1)
Checkbutton(root, text="Símbolos", variable=special_var).grid(row=3, column=3, sticky="w")

exclude_confusing_var = IntVar(value=0)
Checkbutton(root, text="Excluir caracteres confusos (por exemplo, I1l0Oo)", variable=exclude_confusing_var).grid(row=4, column=0, columnspan=2, sticky="w")

# Selecionar número de senhas
tk.Label(root, text="Número de senhas a gerar").grid(row=5, column=0, padx=10, pady=10, sticky="w")
num_passwords_var = tk.StringVar(value="10")
tk.Entry(root, textvariable=num_passwords_var, width=5).grid(row=5, column=1, padx=10, pady=10)

# Botão para gerar senhas
generate_button = tk.Button(root, text="Gerar Senhas", width=20, height=2, command=generate_multiple_passwords)
generate_button.grid(row=6, column=0, padx=10, pady=10)

# Botão para copiar todas as senhas
copy_button = tk.Button(root, text="Copiar Tudo", width=20, height=2, command=copy_all_passwords)
copy_button.grid(row=6, column=1, padx=10, pady=10)

# Campo para exibir as senhas geradas
passwords_text = tk.Text(root, height=20, width=50)
passwords_text.grid(row=7, column=0, columnspan=5, padx=10, pady=10)

# Variáveis globais para armazenar as senhas
passwords = []

root.mainloop()
