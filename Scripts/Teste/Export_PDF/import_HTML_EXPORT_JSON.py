import json
from bs4 import BeautifulSoup

def convert_html_to_json(file_path, output_json):
    # Lê o arquivo HTML e converte o conteúdo para uma lista de parágrafos
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = [p.get_text() for p in soup.find_all('p')]
    
    # Salva os parágrafos em um arquivo JSON
    with open(output_json, 'w', encoding='utf-8') as json_file:
        json.dump(paragraphs, json_file, ensure_ascii=False, indent=4)

    print(f"Documento exportado para {output_json} com sucesso.")

# Caminho do HTML exportado do Google Docs e o JSON de saída
input_html_file = 'C:/teste/output_google_doc.html'
output_json_file = 'C:/teste/document_content.json'
convert_html_to_json(input_html_file, output_json_file)
