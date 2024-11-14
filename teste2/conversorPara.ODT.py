from odf.opendocument import OpenDocumentText
from odf.text import P
from odf.table import Table, TableRow, TableCell
from odf.style import Style, TextProperties, TableColumnProperties

# Função para gerar conteúdo e salvar em arquivo ODT (LibreOffice)
def create_libreoffice_document(users_passwords):
    # Cria um documento ODT
    doc = OpenDocumentText()

    # Estilo para o título "OPEN VPN"
    title_style = Style(name="TitleStyle", family="paragraph")
    title_style.addElement(TextProperties(attributes={'fontsize': "13pt", 'fontweight': "bold", 'color': "#0064af"}))
    doc.styles.addElement(title_style)

    # Adiciona o título
    p = P(stylename=title_style, text="OPEN VPN")
    doc.text.addElement(p)

    # Criação da tabela
    table = Table()

    # Adiciona as linhas de cabeçalho da tabela
    header_row = TableRow()
    headers = ["Aplicação", "Usuário", "Senha"]
    for header in headers:
        cell = TableCell()
        cell.addElement(P(text=header))
        header_row.addElement(cell)
    table.addElement(header_row)

    # Adiciona os usuários e senhas na tabela
    for user, password in users_passwords:
        row = TableRow()

        # Adiciona "Aplicação"
        cell_app = TableCell()
        cell_app.addElement(P(text="Open VPN"))
        row.addElement(cell_app)

        # Adiciona "Usuário"
        cell_user = TableCell()
        cell_user.addElement(P(text=user))
        row.addElement(cell_user)

        # Adiciona "Senha"
        cell_password = TableCell()
        cell_password.addElement(P(text=password if password else "(sem senha)"))
        row.addElement(cell_password)

        table.addElement(row)

    # Adiciona a tabela ao documento
    doc.text.addElement(table)

    # Salva o documento ODT
    doc.save("Usuarios_Senhas_LibreOffice.odt")

# Exemplo de uso:
users_passwords = [("usuario1", "senha1"), ("usuario2", "senha2")]

# Gera o documento ODT compatível com LibreOffice
create_libreoffice_document(users_passwords)
