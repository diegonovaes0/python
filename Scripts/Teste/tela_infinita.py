import time
import os

# Defina um intervalo de tempo para enviar o comando e manter a tela ativa (em segundos)
interval = 30  # 5 minutos, você pode ajustar conforme necessário

try:
    while True:
        # Simula uma tecla "Shift" pressionada
        os.system("xdotool key Shift_L")
        time.sleep(interval)
except KeyboardInterrupt:
    print("Script interrompido.")
