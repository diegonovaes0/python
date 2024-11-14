from bs4 import BeautifulSoup
from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import tkinter as tk
from tkinter import filedialog, messagebox

# Função para carregar e ler o conteúdo HTML
def load_html_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text(separator='\n')

# Função para exportar conteúdo para DOCX
def export_to_docx(content):
    doc = Document()
    doc.add_paragraph(content)
    filename = filedialog.asksaveasfilename(
        defaultextension=".docx",
        filetypes=[("Word files", "*.docx")],
        initialfile="Parceiro - Cliente - Liberação de Informações Técnicas VPN"
    )
    if filename:
        doc.save(filename)
        messagebox.showinfo("Exportação", "Documento salvo com sucesso em formato DOCX!")

# Função para exportar conteúdo para PDF
def export_to_pdf(content):
    filename = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        initialfile="Parceiro - Cliente - Liberação de Informações Técnicas VPN"
    )
    if filename:
        c = canvas.Canvas(filename, pagesize=A4)
        width, height = A4
        text = c.beginText(40, height - 40)
        text.setFont("Times-Roman", 12)
        text.setLeading(14)
        
        for line in content.split('\n'):
            text.textLine(line)
        c.drawText(text)
        c.showPage()
        c.save()
        messagebox.showinfo("Exportação", "Documento salvo com sucesso em formato PDF!")

# Funções de interface
def export_content_to_docx():
    content = load_html_content('output_google_doc.html')  # Substitua pelo caminho do arquivo HTML
    export_to_docx(content)

def export_content_to_pdf():
    content = load_html_content('output_google_doc.html')  # Substitua pelo caminho do arquivo HTML
    export_to_pdf(content)

# Interface Gráfica
root = tk.Tk()
root.title("Exportar Documento")
root.geometry("300x200")

# Botão para exportar como DOCX
button_export_docx = tk.Button(root, text="Exportar para DOCX", command=export_content_to_docx)
button_export_docx.pack(pady=10)

# Botão para exportar como PDF
button_export_pdf = tk.Button(root, text="Exportar para PDF", command=export_content_to_pdf)
button_export_pdf.pack(pady=10)

root.mainloop()
