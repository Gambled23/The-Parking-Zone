from tkinter import *

# Ventana de 14 x 6
root = Tk()
root.title('The parking zone - Administrador')
root.resizable(False, False)
root.config(width=1200, height=650)
root.iconbitmap('panel_admin\images\icono.ico')
# --------------------Header--------------------
header = Label(root, text='')
header.config(bg='black', width=1200, height=6)
header.place(x=0, y=0)

logoImagen = PhotoImage(file='panel_admin\\images\\logo.gif')
labelImagen =Label(root, image=logoImagen)
labelImagen.config(width=100, height=70, bg='black')
labelImagen.place(x=550, y=10)

barraIzquierda = PhotoImage(file='panel_admin\\images\\barraIzquierda.gif')
labelImagen =Label(root, image=barraIzquierda, bg='black')
labelImagen.place(x=3, y=60)

barraDerecha = PhotoImage(file='panel_admin\\images\\barraDerecha.gif')
labelImagen =Label(root, image=barraDerecha, bg='black')
labelImagen.place(x=758, y=60)
# --------------------Body--------------------
# parte superior
administradorLabel = Label(root, text='ADMINISTRADOR')
administradorLabel.config(font=('Arial', 25))
administradorLabel.place(x=10, y=100)

crudLabel = Label(root, text='CRUD')
crudLabel.config(font=('Arial', 12))
crudLabel.place(x=10, y=140)

salirBoton = Button(root, text='SALIR')
salirBoton.config(bg='#f4eb49', fg='black', padx=30, borderwidth=0)
salirBoton.place(x=1050, y=115)

separadorImagen = PhotoImage(file='panel_admin\\images\\separador.gif')
separadorLabel =Label(root, image=separadorImagen)
separadorLabel.config(width=1200, height=10)
separadorLabel.place(x=0, y=165)

# botones principales
# boton asignar
photo = PhotoImage(file = "panel_admin\\images\\flecha.gif")
botonAsignar = Button(root, image = photo, borderwidth=0)
botonAsignar.place(x=172, y=315)

Label(root, text='Asignar', font=('Arial, 20')).place(x=208, y=500)
Label(root, text='nuevos lugares', font=('Arial, 12'), fg='gray').place(x=202, y=545)

# boton modificar
photo2 = PhotoImage(file = "panel_admin\\images\\check.gif")
botonModificar = Button(root, image = photo2, borderwidth=0)
botonModificar.place(x=514, y=315)

Label(root, text='Modificar', font=('Arial, 20')).place(x=545, y=500)
Label(root, text='lugares existentes', font=('Arial, 12'), fg='gray').place(x=538, y=545)

# boton visualizar
photo3 = PhotoImage(file = "panel_admin\\images\\lupa.gif")
botonVizualizar = Button(root, image = photo3, borderwidth=0)
botonVizualizar.place(x=856, y=315)

Label(root, text='Visualizar', font=('Arial, 20')).place(x=880, y=500)
Label(root, text='estacionamiento completo', font=('Arial, 12'), fg='gray').place(x=848, y=545)

# --------------------Footer--------------------
empresaLabel = Label(root, text='THE PARKING ZONE')
empresaLabel.config(bg='black', fg='white', font=('Helvetica', 18, 'bold'), width=80, height=1)
empresaLabel.place(x=0, y=617)


root.mainloop()
