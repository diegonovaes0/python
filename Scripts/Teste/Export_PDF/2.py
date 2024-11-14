import json

def load_document_content(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        document_content = json.load(file)
    return document_content

# Caminho do arquivo JSON exportado
input_json_file = 'C:/document_content.json'
content = load_document_content(input_json_file)

# Exibindo o conteúdo importado
for paragraph in content:
    print(paragraph)
