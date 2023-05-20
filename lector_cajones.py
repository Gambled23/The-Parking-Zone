# import the opencv library
import cv2
import time
from leer_ticket import desocuparCajon
from tkinter import messagebox
from tkinter import *
from panel_admin.gestionarLugares import obtenerListaLugares

def ejecutarCamara(fila, columna):
    # define a video capture object
    vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    detector = cv2.QRCodeDetector()
    while True:
        # Capture the video frame by frame
        ret, frame = vid.read()
        data, bbox, straight_qrcode = detector.detectAndDecode(frame)
        global previousData
        previousData = data
        if len(data) > 0:
            if data == f'{fila}-{columna}':
                messagebox.showinfo('Cajon correcto', f'El ticket presentado es para el cajon {data}')
            else:
                messagebox.showerror('Cajon incorrecto', f'El ticket presentado es para el cajon {data} pero se presentó en {fila}-{columna}')
            time.sleep(3)


        # Display the resulting frame
        cv2.imshow(f'The Parking Zone - Cajon {fila}-{columna}', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()







obtenerID = Tk()
obtenerID.title("Elección de cajón")
obtenerID.iconbitmap('panel_admin\images\iconoAzul.ico')
Label(obtenerID, text="Cajon: ", font=(
    'Helvetica 17 bold'), pady=10, padx=25).grid(row=0, column=0, columnspan=4)

Label(obtenerID, text='Letra:').grid(row=1, column=0)
listaFilas = obtenerListaLugares()[0]
variableFilas = StringVar()
variableFilas.set(listaFilas[0])  # Valor por defecto de dropdown
OptionMenu(obtenerID, variableFilas, *listaFilas).grid(row=1, column=1)

Label(obtenerID, text='Numero:').grid(row=1, column=2)
listaColumnas = obtenerListaLugares()[1]
variableColumnas = StringVar()
variableColumnas.set(listaColumnas[0])  # Valor por defecto de dropdown
OptionMenu(obtenerID, variableColumnas, *listaColumnas).grid(row=1, column=3)

def mandarModificar():
    fila=variableFilas.get()[2]
    aux=variableColumnas.get()
    columna = int(''.join(filter(str.isdigit, aux)))
    obtenerID.destroy()
    ejecutarCamara(fila.upper(), columna)
    
Button(obtenerID, text='Iniciar cámara',
        command=lambda: mandarModificar()).grid(row=3, column=0, columnspan=4, pady=10)




obtenerID.mainloop()