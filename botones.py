import serial
from pynput import keyboard as kb
import time
from generar_boleto import generarPDF
import os

avanzar = True
ser = serial.Serial('COM4', 9600, timeout = 1)
time.sleep(1)

def parar(tecla):
    global avanzar

    if tecla == kb.KeyCode.from_char('q'):
        avanzar = False

#auxiliares
bandera = False
while avanzar:
    os.system('cls')
    print('-------THE PARKING ZONE-------\n    Presione el boleto que necesite\n')
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
            #estado = int(ser.read())
            ser.readline()
    else:
        print("Cerrar")
        ser.close()

    if bandera:
        bandera = False
    elif (not bandera) and tipo != 0:
        if tipo == 1:
            print("\nImprimiendo boleto estandar...")
            try:
                generarPDF(False)
            except:
                print('Ya no hay cajones normales disponibles')
                print('Lamentamos las molestias')
            time.sleep(5)
        elif tipo == 2:
            print("\nImprimiendo boleto especial...")
            try:
                generarPDF(True)
            except:
                print('Ya no hay cajones especiales disponibles, intente con un cajón normal')
            time.sleep(5)
        bandera = True
    

    kb.Listener(parar).start()