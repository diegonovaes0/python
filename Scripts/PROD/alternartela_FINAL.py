import pyautogui
import time
import subprocess

def abrir_chrome():
    # Comando para abrir o Google Chrome
    # Se necessário, ajuste o caminho ou comando dependendo do seu sistema operacional.
    subprocess.Popen("start chrome", shell=True)
    time.sleep(5)  # Aguarda 5 segundos para o Chrome abrir completamente

def manter_tela_ativa():
    while True:
        # Simula um clique em uma posição específica (ajuste conforme necessário)
        pyautogui.moveTo(300, 200)  # Move o mouse para a posição (300, 200)
        pyautogui.click()
        time.sleep(2)  # Aguarda 2 segundos

        # Simula rolar a página para baixo
        pyautogui.scroll(-500)  # Rola a página para baixo
        time.sleep(2)  # Aguarda 2 segundos

        # Você pode descomentar estas partes se precisar abrir uma nova aba no Chrome ou alternar janelas
        # Simula a abertura de uma nova aba no Chrome
        # pyautogui.hotkey('ctrl', 't')
        # time.sleep(2)  # Aguarda 2 segundos para a nova aba abrir

        # Alterna de volta para outra janela usando Alt + Tab
        # pyautogui.hotkey('alt', 'tab')
        # time.sleep(30)  # Aguarda 30 segundos antes de repetir o ciclo

if __name__ == "__main__":
    abrir_chrome()
    manter_tela_ativa()
