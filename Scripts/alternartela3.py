import pyautogui
import time

def manter_tela_ativa():
    while True:
        # Simula um clique em uma posição específica na janela aberta (ajuste conforme necessário)
        pyautogui.moveTo(300, 200)  # Move o mouse para a posição (300, 200)
        pyautogui.click()
        time.sleep(2)  # Aguarda 2 segundos

        # Simula rolar a página para baixo
        pyautogui.scroll(-500)  # Rola a página para baixo
        time.sleep(2)  # Aguarda 2 segundos

        # Simula uma pequena movimentação do mouse para manter a tela ativa
        pyautogui.moveTo(300, 200)
        pyautogui.moveTo(305, 205)  # Pequeno movimento do mouse
        time.sleep(30)  # Aguarda 30 segundos antes de repetir o ciclo

if __name__ == "__main__":
    manter_tela_ativa()
