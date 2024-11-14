import os
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk

def load_image(filename, width=None, height=None):
    """Carrega e redimensiona uma imagem para exibição."""
    img_path = os.path.join("img", filename)
    if os.path.exists(img_path):
        img = Image.open(img_path)
        if width and height:
            img = img.resize((width, height), Image.LANCZOS)  # Substitua ANTIALIAS por LANCZOS
        return ImageTk.PhotoImage(img)
    else:
        print(f"Imagem {filename} não encontrada.")
        return None


def display_document_content():
    # Cria a janela principal
    root = tk.Tk()
    root.title("Visualizador de Documento")
    root.geometry("800x900")
    
    # Área de rolagem
    canvas = tk.Canvas(root, width=780)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Adiciona a capa
    capa_img = load_image("capa_doc_autosky.png", width=800, height=1132)
    if capa_img:
        capa_label = tk.Label(scrollable_frame, image=capa_img)
        capa_label.image = capa_img
        capa_label.pack(pady=10)
    
    # Adiciona o cabeçalho
    cabec_img = load_image("cabec_new.jpg", width=800, height=121)
    if cabec_img:
        cabec_label = tk.Label(scrollable_frame, image=cabec_img)
        cabec_label.image = cabec_img
        cabec_label.pack(pady=10)

    # Título centralizado
    title_label = tk.Label(scrollable_frame, text="LIBERAÇÃO PROJETO CLOUD AUTOSKY", font=("Helvetica", 14, "bold"))
    title_label.pack(pady=5)

    # Corpo do texto com formatação justificada
    text_content = [
        "Este documento tem como objetivo apresentar as informações sobre arquitetura do projeto e as credenciais de acesso aos servidores.",
        "O ambiente Autosky é composto por um servidor de aplicação, onde sua principal finalidade é armazenar a instalação das aplicações client-server, e a virtualização para acesso dos usuários através do Autosky Platform.",
        "Demais finalidades como Banco de Dados, Serviços WEB, File Server, assim como outros serviços específicos, serão implantados conforme o modelo de arquitetura contemplado no escopo deste projeto, podendo ou não ocorrer a existência de mais servidores na arquitetura.",
        "Durante o período de implantação, treinamentos serão ministrados para adequar parceiro / cliente ao universo cloud Autosky, capacitando-os na aderência das melhores práticas e usabilidade dos recursos e serviços oferecidos pela Skyone.",
        "Os servidores são compostos por dois endereços de IP, sendo Público e Privado, assim como um endereço de DNS no qual poderá ser utilizado no lugar do IP público. Para acessar as instâncias via terminal server (RDP ou SSH), deverá ser utilizado o IP Público.",
        "No entanto, se a arquitetura deste projeto contempla serviços de VPN, após o fechamento e configuração das rotas, é possível realizar o acesso também pelo IP privado."
    ]
    
    for paragraph in text_content:
        text_label = tk.Label(scrollable_frame, text=paragraph, wraplength=750, justify="left", anchor="w", font=("Helvetica", 12))
        text_label.pack(pady=5, padx=5)

    # Rodapé
    rodape_img = load_image("rodape_new.jpg", width=800, height=102)
    if rodape_img:
        rodape_label = tk.Label(scrollable_frame, image=rodape_img)
        rodape_label.image = rodape_img
        rodape_label.pack(pady=10)

    # Mais cabeçalhos e seções
    outro_cabec_img = load_image("cabec_new.jpg", width=800, height=121)
    if outro_cabec_img:
        outro_cabec_label = tk.Label(scrollable_frame, image=outro_cabec_img)
        outro_cabec_label.image = outro_cabec_img
        outro_cabec_label.pack(pady=10)

    # Seção de observações
    obs_label = tk.Label(scrollable_frame, text="OBSERVAÇÕES IMPORTANTES", font=("Helvetica", 14, "bold"), fg="#0f0053")
    obs_label.pack(pady=10)

    obs_content = [
        "Para acessar os servidores Cloud, é necessária a liberação do seu IP de saída ou link de internet.",
        "Você pode acessar o site meuip.com.br para descobri-lo! Informe seu endereço IP ao arquiteto responsável pelo projeto para liberação de acesso.",
        "Sobre as portas de Inbound e Outbound dos servidores: Por padrão, e seguindo as melhores práticas de segurança da informação, a Skyone não libera portas de entrada (Inbound) como Anywhere (0.0.0.0/0). Caso seja necessária a liberação de uma porta neste formato, é preciso enviar a solicitação por e-mail para análise interna.",
        "As portas de saída (Outbound) já estão liberadas no formato Anywhere (0.0.0.0/0). Recomendamos a não liberação de portas para serviços de banco de dados no formato anywhere (0.0.0.0/0). Caso seja realmente necessário esse tipo de liberação, uma carta de riscos será enviada após análise jurídica e de governança da Skyone."
    ]
    
    for obs in obs_content:
        obs_label = tk.Label(scrollable_frame, text=obs, wraplength=750, justify="left", anchor="w", font=("Helvetica", 12))
        obs_label.pack(pady=5, padx=5)

    # Configurações finais da interface
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    root.mainloop()

display_document_content()
