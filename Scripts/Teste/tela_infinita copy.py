import time

interval = 30  # Intervalo de 30 segundos

try:
    while True:
        print("Mantendo a sessão ativa...")
        time.sleep(interval)
except KeyboardInterrupt:
    print("Script interrompido.")
