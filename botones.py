import serial
from pynput import keyboard as kb
import time

avanzar = True
ser = serial.Serial('COM4', 9600, timeout = 1)
time.sleep(1)

def parar(tecla):
    global avanzar

    if tecla == kb.KeyCode.from_char('q'):
        avanzar = False

while avanzar:
    tipo = 0
    estado = 0
    time.sleep(0.5)
    if avanzar:
        lectura = ser.read()
        if len(lectura) > 0:
            tipo = int(lectura)
            ser.readline()
            ser.readline()
            ser.readline()
            ser.readline()
            estado = int(ser.read())
            ser.readline()
    else:
        print("Cerrar")
        ser.close()

    if tipo == 1:
        print("Estandar")
    elif tipo == 2:
        print("Discapacitado")

    if estado == 1:
        print("Disponible")
    elif estado == 2:
        print("Ocupado")

    kb.Listener(parar).start()