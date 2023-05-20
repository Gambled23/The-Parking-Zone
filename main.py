from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from _tkinter import TclError
from generar_boleto import generarPDF


def boletos(discapacitado):
    if discapacitado:
        try:
            generarPDF(True)
        except:
            TIME_TO_WAIT = 3500
            root = Tk() 
            root.withdraw()
            try:
                root.after(TIME_TO_WAIT, root.destroy) 
                messagebox.Message(title="Cajones no disponibles", message="Ya no hay cajones especiales disponibles", master=root).show()
            except TclError:
                pass
    else:
        try:
            generarPDF(False)
        except:
            TIME_TO_WAIT = 3500
            root = Tk() 
            root.withdraw()
            try:
                root.after(TIME_TO_WAIT, root.destroy) 
                messagebox.Message(title="Cajones no disponibles", message="Ya no hay cajones normales disponibles", master=root).show()
            except TclError:
                pass

root = Tk()
root.title('THE PARKING ZONE')
root.iconbitmap('panel_admin\images\icono.ico')
root.resizable(False, False)
root.config(width=500, height=300)

# --------------------Header--------------------
header = Label(root, text='')
header.config(bg='black', width=1200, height=6)
header.place(x=0, y=0)

logoImagen = PhotoImage(file='panel_admin\\images\\logo.gif')
labelImagen = Label(root, image=logoImagen)
labelImagen.config(width=100, height=70, bg='black')
labelImagen.place(x=200, y=10)

# --------------------Body----------------------
botonDiscapacitado = Button(root, padx=10, fg='black', bg='#C3E0FC', font=('Helvetica', 30, 'bold'), text='Especial', command=lambda: boletos(True))
botonDiscapacitado.place(x=20, y=155)

botonNormal = Button(root, padx=10, fg='black', bg='#FDFF8E', font=('Helvetica', 30, 'bold'), text='Normal', command=lambda: boletos(False))
botonNormal.place(x=300, y=155)

root.mainloop()