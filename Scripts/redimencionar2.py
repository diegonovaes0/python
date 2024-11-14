import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

def abrir_imagem():
    # Abre um diálogo para o usuário selecionar o arquivo
    global img, img_original, img_path
    img_path = filedialog.askopenfilename()
    
    if img_path:
        # Abre e exibe a imagem
        img_original = Image.open(img_path)
        atualizar_imagem(img_original)

def atualizar_imagem(img):
    # Atualiza a imagem no canvas
    global img_tk, canvas
    img_tk = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor='nw', image=img_tk)
    canvas.config(width=img.width, height=img.height)

def redimensionar_imagem():
    # Redimensiona a imagem de acordo com os valores dos sliders
    largura = int(largura_slider.get())
    altura = int(altura_slider.get())
    
    img_redimensionada = img_original.resize((largura, altura))
    atualizar_imagem(img_redimensionada)

def salvar_imagem():
    # Salva a imagem redimensionada no mesmo local
    if img_path:
        directory, filename = os.path.split(img_path)
        new_filename = f"resized_{filename}"
        new_img_path = os.path.join(directory, new_filename)
        
        # Redimensiona e salva a imagem
        largura = int(largura_slider.get())
        altura = int(altura_slider.get())
        img_redimensionada = img_original.resize((largura, altura))
        img_redimensionada.save(new_img_path)
        print(f"Imagem salva em: {new_img_path}")

# Configuração da janela principal
root = tk.Tk()
root.title("Redimensionador de Imagens")

# Criação do Canvas para exibir a imagem
canvas = tk.Canvas(root, width=400, height=400)
canvas.grid(row=0, column=0, columnspan=3)

# Botão para abrir a imagem
btn_abrir = tk.Button(root, text="Abrir Imagem", command=abrir_imagem)
btn_abrir.grid(row=1, column=0)

# Sliders para ajuste da largura e altura
largura_slider = tk.Scale(root, from_=50, to_=800, orient='horizontal', label="Largura", command=lambda x: redimensionar_imagem())
largura_slider.grid(row=2, column=0)

altura_slider = tk.Scale(root, from_=50, to_=800, orient='horizontal', label="Altura", command=lambda x: redimensionar_imagem())
altura_slider.grid(row=2, column=1)

# Botão para salvar a imagem redimensionada
btn_salvar = tk.Button(root, text="Salvar Imagem", command=salvar_imagem)
btn_salvar.grid(row=1, column=2)

# Executa a aplicação
root.mainloop()
