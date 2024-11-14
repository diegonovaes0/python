import pyautogui
import time

def mover_mouse():
    while True:
        # Move o mouse 10 pixels para a direita e depois 10 pixels para a esquerda
        pyautogui.move(10, 0)
        time.sleep(5)  # Aguarda 5 segundos
        pyautogui.move(-10, 0)
        time.sleep(5)

if __name__ == "__main__":
    mover_mouse()
