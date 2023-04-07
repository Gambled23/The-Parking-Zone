from tkinter import *

# Ventana de 14 x 6
root = Tk()
root.title('The parking zone - Administrador')
root.resizable(False, False)
root.config(width=1200, height=650)
# --------------------Header--------------------
header = Label(root, text='')
header.config(bg='black', width=1200, height=6)
header.place(x=0, y=0)

logoImagen = PhotoImage(file='panel_admin\\images\\logo.gif')
labelImagen =Label(root, image=logoImagen)
labelImagen.config(width=100, height=70, bg='black')
labelImagen.place(x=550, y=10)
# --------------------Body--------------------
# parte superior
administradorLabel = Label(root, text='ADMINISTRADOR')
administradorLabel.config(font=('Arial', 25))
administradorLabel.place(x=10, y=100)

crudLabel = Label(root, text='CRUD')
crudLabel.config(font=('Arial', 12))
crudLabel.place(x=10, y=140)

salirBoton = Button(root, text='SALIR')
salirBoton.config(bg='yellow', fg='black', padx=30)
salirBoton.place(x=1050, y=115)

separadorImagen = PhotoImage(file='panel_admin\\images\\separador.gif')
separadorLabel =Label(root, image=separadorImagen)
separadorLabel.config(width=1200, height=10)
separadorLabel.place(x=0, y=165)
# botones principales

# --------------------Footer--------------------
empresaLabel = Label(root, text='THE PARKING ZONE')
empresaLabel.config(bg='black', fg='white', font=('Helvetica', 18, 'bold'), width=80, height=1)
empresaLabel.place(x=0, y=617)


root.mainloop()
