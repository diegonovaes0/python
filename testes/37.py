from PIL import Image
import os

def testar_caminho_e_abrir_imagem():
    img_path_header = os.path.join("img", "cabec_new.jpg")
    img_path_footer = os.path.join("img", "rodape_new.jpg")

    try:
        # Testa imagem do cabeçalho
        if os.path.exists(img_path_header):
            img_header = Image.open(img_path_header)
            img_header.show()  # Abre a imagem para verificação
            print("Imagem de cabeçalho carregada com sucesso.")
        else:
            print("Imagem de cabeçalho não encontrada no caminho:", img_path_header)

        # Testa imagem do rodapé
        if os.path.exists(img_path_footer):
            img_footer = Image.open(img_path_footer)
            img_footer.show()  # Abre a imagem para verificação
            print("Imagem de rodapé carregada com sucesso.")
        else:
            print("Imagem de rodapé não encontrada no caminho:", img_path_footer)
    
    except Exception as e:
        print("Erro ao carregar a imagem:", e)

testar_caminho_e_abrir_imagem()
