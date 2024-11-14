import random
import string
import pandas as pd

# Função para gerar uma senha de 14 caracteres, contendo letras e números
def generate_password(length=14):
    characters = string.ascii_letters + string.digits  # Letras maiúsculas, minúsculas e números
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Função para mesclar usuários e senhas ou gerar apenas senhas
def create_passwords(num_passwords, users=None):
    passwords = [generate_password() for _ in range(num_passwords)]
    
    # Se forem fornecidos usuários, mesclar com as senhas
    if users:
        data = {"Usuário": users, "Senha": passwords}
        return pd.DataFrame(data)
    
    # Se não, retornar apenas as senhas
    return "\n".join(passwords)

# Exemplo de função interativa
def main():
    # Perguntar ao usuário se ele quer mesclar usuários ou apenas gerar senhas
    choice = input("Você quer mesclar usuários e senhas (1) ou gerar apenas senhas (2)? Digite 1 ou 2: ")
    
    if choice == "1":
        num_users = int(input("Quantos usuários você quer inserir? "))
        users = []
        for i in range(num_users):
            user = input(f"Digite o nome do usuário {i + 1}: ")
            users.append(user)
        df = create_passwords(num_users, users)
        print(df)
    
    elif choice == "2":
        num_passwords = int(input("Quantas senhas você deseja gerar? "))
        passwords = create_passwords(num_passwords)
        print("Senhas geradas:")
        print(passwords)
    else:
        print("Escolha inválida. Tente novamente.")

# Executar o programa principal
main()
