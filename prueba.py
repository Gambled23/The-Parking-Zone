from datetime import datetime

fecha = datetime.today().date()
hora = datetime.today().hour
minuto = datetime.today().minute

print(f'{fecha} {hora}:{minuto}')