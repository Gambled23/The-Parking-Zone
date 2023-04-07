from tkinter import *

#Ventana de 14 x 6
root = Tk()
root.title('The parking zone - Administrador')
root.resizable(False,False)
root.config(width=1200, height=650)

framePrincipal = Frame(root, width=1200, height=650)
framePrincipal.pack()

#--------------------Header--------------------
frameHeader = Frame(framePrincipal, width=1200, height=100)
frameHeader.config(bg='black')
frameHeader.pack()

#--------------------Body--------------------
frameBody = Frame(framePrincipal, width=1200, height=550)
frameBody.pack()

administradorLabel = Label(frameBody, text='ADMINISTRADOR')
administradorLabel.grid(row=0, column=0, columnspan=2)

salirBoton = Button(frameBody, text='SALIR')
salirBoton.config(bg='yellow', fg='black', padx=30)
salirBoton.grid(row=0, column=14)

#botones principales

#--------------------Footer--------------------
empresaLabel = Label(frameBody, text='THE PARKING ZONE')
empresaLabel.config(bg='black', fg='yellow')
empresaLabel.grid(row=5, column=7, columnspan=14)



root.mainloop()