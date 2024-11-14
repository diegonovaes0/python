from PIL import Image
import os

# Solicita o caminho da imagem e o redimensionamento
img_path = input("Informe o caminho da imagem: ")
width = int(input("Informe a largura desejada: "))
height = int(input("Informe a altura desejada: "))

# Abre a imagem
img = Image.open(img_path)

# Redimensiona a imagem
img_resized = img.resize((width, height))

# Extrai o diretório e nome do arquivo original
directory, filename = os.path.split(img_path)

# Cria um novo nome para o arquivo redimensionado
new_filename = f"resized_{filename}"

# Salva a nova imagem no mesmo diretório
new_img_path = os.path.join(directory, new_filename)
img_resized.save(new_img_path)

print(f"Imagem salva com sucesso em: {new_img_path}")
