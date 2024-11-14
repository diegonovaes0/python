import tkinter as tk
from tkinter import messagebox

# Função para gerar o conteúdo formatado
def generate_content(users_passwords):
    content = ""
    for user, password in users_passwords:
        content += f"Usuário: {user}\nSenha: {password}\n\n"
    return content

# Função para exibir o conteúdo gerado em uma janela
def show_content_in_window(content):
    window = tk.Toplevel()
    window.title("Conteúdo Gerado")
    
    text_area = tk.Text(window, wrap='word', height=20, width=60)
    text_area.pack(padx=10, pady=10)
    
    text_area.insert(tk.END, content)
    
    # Permite selecionar e copiar o texto
    text_area.config(state=tk.NORMAL)
    text_area.focus()

# Função chamada quando o botão é clicado
def generate_and_show_content():
    users_passwords_text = text_input.get("1.0", tk.END).strip()

    if not users_passwords_text:
        messagebox.showerror("Erro", "Por favor, insira os usuários e senhas.")
        return

    users_passwords = []
    current_user = None
    current_password = None

    lines = users_passwords_text.splitlines()

    for line in lines:
        line = line.strip()

        if not line:  # Se houver uma linha vazia, pula
            continue

        if current_user is None:
            current_user = line  # Considera a primeira linha não vazia como o nome do usuário
        elif current_password is None:
            current_password = line  # Considera a segunda linha como a senha

        if current_user and current_password:
            users_passwords.append((current_user, current_password))
            current_user = None  # Reseta para o próximo par
            current_password = None

    # Se sobrar um último usuário sem senha, adiciona ao final
    if current_user is not None:
        users_passwords.append((current_user, "(sem senha)"))

    content = generate_content(users_passwords)
    show_content_in_window(content)

# Interface gráfica usando Tkinter
root = tk.Tk()
root.title("Gerador de Conteúdo de Usuário e Senha")
root.geometry("600x400")

# Label para instrução
label_instruction = tk.Label(root, text="Insira usuários e senhas (um por linha):")
label_instruction.pack(pady=10)

# Caixa de texto para inserir os usuários e senhas
text_input = tk.Text(root, height=10, width=50)
text_input.pack(pady=10)

# Botão para gerar o conteúdo
generate_button = tk.Button(root, text="Gerar Conteúdo", command=generate_and_show_content)
generate_button.pack(pady=20)

# Inicia a interface gráfica
root.mainloop()
