import tkinter as tk
from tkinter import filedialog, messagebox
from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def export_to_docx(content):
    doc = Document()
    doc.add_paragraph(content)
    filename = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word files", "*.docx")])
    if filename:
        doc.save(filename)
        messagebox.showinfo("Exportação", "Documento salvo com sucesso em formato DOCX!")

def export_to_pdf(content):
    filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
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

def export_content():
    # Conteúdo a ser exportado, aqui como exemplo de string, inclua seu HTML processado aqui
    content = """Este documento tem como objetivo apresentar as informações sobre arquitetura do projeto
    e as credenciais de acesso aos servidores.
    
    O ambiente Autosky é composto por um servidor de aplicação, onde sua principal finalidade é armazenar
    a instalação das aplicações client-server, e a virtualização para acesso dos usuários através do Autosky Platform.
    """
    export_to_docx(content)
    export_to_pdf(content)

# Interface Gráfica
root = tk.Tk()
root.title("Exportar Documento")
root.geometry("300x150")

button_export = tk.Button(root, text="Exportar para DOCX e PDF", command=export_content)
button_export.pack(pady=20)

root.mainloop()
