import pyautogui
import time

def manter_tela_ativa():
    while True:
        # Move o mouse para uma posição dentro da janela do Chrome e clica
        pyautogui.moveTo(300, 200)  # Ajuste a posição conforme necessário
        pyautogui.click()
        time.sleep(2)  # Aguarda 2 segundos

        # Simula rolar a página para baixo
        pyautogui.scroll(-500)  # Rola a página para baixo
        time.sleep(60)  # Aguarda 60 segundos antes de repetir o ciclo

if __name__ == "__main__":
    manter_tela_ativa()
