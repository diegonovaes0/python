import requests
from docx import Document
from io import BytesIO
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import re

def get_file_id_from_url(url):
    match = re.search(r'd/([a-zA-Z0-9_-]+)|id=([a-zA-Z0-9_-]+)', url)
    if match:
        return match.group(1) or match.group(2)
    else:
        messagebox.showerror("Erro", "URL inválida. Certifique-se de que é um link do Google Drive.")
        return None

def download_docx_from_google_docs(file_id):
    download_url = f"https://docs.google.com/document/d/{file_id}/export?format=docx"
    response = requests.get(download_url, stream=True)
    if response.status_code == 200:
        print("Download concluído com sucesso.")
        return BytesIO(response.content)
    else:
        messagebox.showerror("Erro", "Falha ao baixar o arquivo. Verifique as permissões do documento.")
        return None

def read_docx_content(docx_file):
    doc = Document(docx_file)
    content = []

    for paragraph in doc.paragraphs:
        if paragraph.text.strip():  # Apenas parágrafos não vazios
            paragraph_content = {
                "text": paragraph.text,
                "bold": any(run.bold for run in paragraph.runs),
                "italic": any(run.italic for run in paragraph.runs),
                "type": "paragraph"
            }
            content.append(paragraph_content)

    for rel in doc.part.rels.values():
        if "image" in rel.target_ref:
            img_data = rel.target_part.blob
            content.append({"type": "image", "data": img_data})

    return content

def display_document_content(content):
    root = tk.Tk()
    root.title("Visualizador de Documento")
    root.geometry("800x600")
    canvas = tk.Canvas(root, width=800, height=600)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Exibe parágrafos e imagens
    for item in content:
        if item["type"] == "paragraph":
            text_label = tk.Label(scrollable_frame, text=item["text"], wraplength=750, justify="left", anchor="w")
            text_label.pack(fill="x", pady=5, padx=5)

            # Define formatação
            if item["bold"] and item["italic"]:
                text_label.config(font=("Helvetica", 12, "bold italic"))
            elif item["bold"]:
                text_label.config(font=("Helvetica", 12, "bold"))
            elif item["italic"]:
                text_label.config(font=("Helvetica", 12, "italic"))
            else:
                text_label.config(font=("Helvetica", 12))

        elif item["type"] == "image":
            img = Image.open(BytesIO(item["data"]))
            img.thumbnail((400, 300))
            img_tk = ImageTk.PhotoImage(img)
            img_label = tk.Label(scrollable_frame, image=img_tk)
            img_label.image = img_tk
            img_label.pack(pady=10)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    root.mainloop()

url = input("Por favor, insira a URL do documento no Google Drive: ")
file_id = get_file_id_from_url(url)

if file_id:
    docx_file = download_docx_from_google_docs(file_id)
    if docx_file:
        content = read_docx_content(docx_file)
        display_document_content(content)
