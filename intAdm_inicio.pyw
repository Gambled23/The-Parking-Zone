from tkinter import *
from tkinter import messagebox
from panel_admin.asignarLugares import obtenerUltimosDatos, insertarFila
from panel_admin.gestionarLugares import obtenerListaLugares, modificarCajon
from interfaz_estacionamiento import ver_estacionamiento

root = Tk()
root.title('The parking zone - Administrador')
root.resizable(False, False)
root.config(width=1200, height=650)
root.iconbitmap('panel_admin\images\icono.ico')

# funciones submenus


def asignar():
    ventanaAsignar = Toplevel(root)
    ventanaAsignar.title("Asignar")
    # Create a Label in New window
    letraFila = StringVar()
    numeroFila = StringVar()

    Label(ventanaAsignar, text="Crear nuevos cajones", font=(
        'Helvetica 17 bold'), pady=10, padx=25).grid(row=0, column=0, columnspan=2)
    Label(ventanaAsignar, text='Letra de la fila: ').grid(row=1, column=0)
    Entry(ventanaAsignar, textvariable=letraFila).grid(row=1, column=1)
    ultimoLugar = obtenerUltimosDatos()
    Label(ventanaAsignar, text='Numero máximo de la fila: ').grid(row=2, column=0)
    ultimoNumero = Entry(ventanaAsignar, textvariable=numeroFila)
    ultimoNumero.insert(END, ultimoLugar[2])
    ultimoNumero.grid(row=2, column=1)

    def obtenerDatos():
        insertarFila(letraFila.get(), numeroFila.get())
        messagebox.showinfo(
            'Fila agregada', f'Se ha agregado hasta el cajon {letraFila.get()}-{numeroFila.get()}')
        ventanaAsignar.destroy()

    Button(ventanaAsignar, text='Agregar fila',
           command=lambda: obtenerDatos()).grid(row=3, column=0, columnspan=2)


def modificar():
    ventanaModificar = Toplevel(root)
    ventanaModificar.title("Modificar")
    Label(ventanaModificar, text="Cajon a modificar: ", font=(
        'Helvetica 17 bold'), pady=10, padx=25).grid(row=0, column=0, columnspan=4)
    
    Label(ventanaModificar, text='Letra:').grid(row=1, column=0)
    listaFilas = obtenerListaLugares()[0]
    variableFilas = StringVar()
    variableFilas.set(listaFilas[0])  # Valor por defecto de dropdown
    OptionMenu(ventanaModificar, variableFilas, *listaFilas).grid(row=1, column=1)

    Label(ventanaModificar, text='Numero:').grid(row=1, column=2)
    listaColumnas = obtenerListaLugares()[1]
    variableColumnas = StringVar()
    variableColumnas.set(listaColumnas[0])  # Valor por defecto de dropdown
    OptionMenu(ventanaModificar, variableColumnas, *listaColumnas).grid(row=1, column=3)

    discapacitado = IntVar()
    ocupado = IntVar()
    Checkbutton(ventanaModificar, text='Discapacitado', variable=discapacitado).grid(row=2, column=0, columnspan=2)
    Checkbutton(ventanaModificar, text='Ocupado', variable=ocupado).grid(row=2, column=2, columnspan=2, pady=10)

    def mandarModificar():
        fila=variableFilas.get()[2]
        aux=variableColumnas.get()
        columna = int(''.join(filter(str.isdigit, aux)))
        modificarCajon(fila, columna, discapacitado.get(), ocupado.get())
       
    Button(ventanaModificar, text='Modificar cajon',
           command=lambda: mandarModificar()).grid(row=3, column=0, columnspan=4, pady=10)
    
# --------------------Header--------------------
header = Label(root, text='')
header.config(bg='black', width=1200, height=6)
header.place(x=0, y=0)

logoImagen = PhotoImage(file='panel_admin\\images\\logo.gif')
labelImagen = Label(root, image=logoImagen)
labelImagen.config(width=100, height=70, bg='black')
labelImagen.place(x=550, y=10)

barraIzquierda = PhotoImage(file='panel_admin\\images\\barraIzquierda.gif')
labelImagen = Label(root, image=barraIzquierda, bg='black')
labelImagen.place(x=3, y=60)

barraDerecha = PhotoImage(file='panel_admin\\images\\barraDerecha.gif')
labelImagen = Label(root, image=barraDerecha, bg='black')
labelImagen.place(x=758, y=60)
# --------------------Body--------------------
# parte superior
administradorLabel = Label(root, text='ADMINISTRADOR')
administradorLabel.config(font=('Arial', 25))
administradorLabel.place(x=10, y=100)

crudLabel = Label(root, text='CRUD')
crudLabel.config(font=('Arial', 12))
crudLabel.place(x=10, y=140)

salirBoton = Button(root, text='SALIR', command=root.destroy)
salirBoton.config(bg='#f4eb49', fg='black', padx=30, borderwidth=0)
salirBoton.place(x=1050, y=115)

separadorImagen = PhotoImage(file='panel_admin\\images\\separador.gif')
separadorLabel = Label(root, image=separadorImagen)
separadorLabel.config(width=1200, height=10)
separadorLabel.place(x=0, y=165)

# botones principales
# boton asignar
photo = PhotoImage(file="panel_admin\\images\\flecha.gif")
botonAsignar = Button(root, image=photo, borderwidth=0, command=asignar)
botonAsignar.place(x=172, y=315)

Label(root, text='Asignar', font=('Arial, 20')).place(x=208, y=500)
Label(root, text='nuevos lugares', font=(
    'Arial, 12'), fg='gray').place(x=202, y=545)

# boton modificar
photo2 = PhotoImage(file="panel_admin\\images\\check.gif")
botonModificar = Button(root, image=photo2, borderwidth=0, command=modificar)
botonModificar.place(x=514, y=315)

Label(root, text='Modificar', font=('Arial, 20')).place(x=545, y=500)
Label(root, text='lugares existentes', font=(
    'Arial, 12'), fg='gray').place(x=538, y=545)

# boton visualizar
photo3 = PhotoImage(file="panel_admin\\images\\lupa.gif")
botonVizualizar = Button(root, image=photo3, borderwidth=0, command=lambda:ver_estacionamiento())
botonVizualizar.place(x=856, y=315)

Label(root, text='Visualizar', font=('Arial, 20')).place(x=880, y=500)
Label(root, text='estacionamiento completo', font=(
    'Arial, 12'), fg='gray').place(x=848, y=545)

# --------------------Footer--------------------
empresaLabel = Label(root, text='THE PARKING ZONE')
empresaLabel.config(bg='black', fg='white', font=(
    'Helvetica', 18, 'bold'), width=80, height=1)
empresaLabel.place(x=0, y=617)


root.mainloop()
