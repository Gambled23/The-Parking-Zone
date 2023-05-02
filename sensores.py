import serial
import time
import tkinter as tk
#import comprobarSensores

ser = serial.Serial('COM3', 9600, timeout = 1)
time.sleep(2)
canSens = 5
datos = []

def tecla(evento):
    datos.clear()
    ser.write(b't')
    for i in range(canSens):
        datos.append(int(ser.read()))

    ser.read()
    	
    print(datos)
    #Datos es 1 si está ocupado, 0 si se desocupa
    #comprobarSensores.comprobarCajon(datos)


raiz = tk.Tk()
raiz.bind('<t>', tecla)
raiz.mainloop()
ser.close()