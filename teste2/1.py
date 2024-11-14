import socket

# Cria um socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define o IP e a porta
host = '0.0.0.0'  # Escuta em todas as interfaces
port = 1283

# Liga o socket ao endereço e porta
server_socket.bind((host, port))

# Começa a escutar por conexões
server_socket.listen(5)
print(f'Servidor escutando na porta {port}...')

while True:
    # Aceita uma nova conexão
    client_socket, addr = server_socket.accept()
    print(f'Conexão de {addr} estabelecida!')

    # Envia uma mensagem de boas-vindas
    client_socket.sendall(b'Bem-vindo ao servidor de teste na porta 1283!\n')
    client_socket.close()
