from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import iniciarSesion
import string
from panel_admin.asignarLugares import obtenerUltimosDatos, insertarFila
from panel_admin.gestionarLugares import obtenerListaLugares, modificarCajon
from notificaciones import obtenerCajonesSospechosos, verificarCajonUnico
from verEstacionamiento import obtenerFilasColumnas, obtenerOcupados

def asignar():
    ventanaAsignar = Toplevel(root)
    ventanaAsignar.title("Asignar")
    ventanaAsignar.iconbitmap('panel_admin\images\iconoAzul.ico')
    # Create a Label in New window
    letraFila = StringVar()

    Label(ventanaAsignar, text="Crear nuevas columnas", font=(
        'Helvetica 17 bold'), pady=10, padx=25).grid(row=0, column=0, columnspan=2)
    Label(ventanaAsignar, text='Letra de la fila: ').grid(row=1, column=0)
    Entry(ventanaAsignar, textvariable=letraFila).grid(row=1, column=1)
    ultimoLugar = obtenerUltimosDatos()
    Label(ventanaAsignar, text='Numero máximo de la fila: ').grid(row=2, column=0)
    ultimoNumero = Label(ventanaAsignar, text=ultimoLugar[2])
    ultimoNumero.grid(row=2, column=1)

    def obtenerDatos():
        insertarFila(letraFila.get(), ultimoLugar[2])
        messagebox.showinfo(
            'Fila agregada', f'Se ha agregado hasta el cajon {letraFila.get()}-{ultimoLugar[2]}')
        ventanaAsignar.destroy()

    Button(ventanaAsignar, text='Agregar fila',
           command=lambda: obtenerDatos()).grid(row=3, column=0, columnspan=2)


def modificar():
    ventanaModificar = Toplevel(root)
    ventanaModificar.title("Modificar")
    ventanaModificar.iconbitmap('panel_admin\images\iconoAzul.ico')
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

def visualizar():
    VisualizarRoot = Toplevel(root)
    VisualizarRoot.title("Visualizar")
    VisualizarRoot.iconbitmap('panel_admin\images\iconoAzul.ico')
    VisualizarRoot.resizable(False,False)
    VisualizarRoot.geometry("845x800")

    main_frame = Frame(VisualizarRoot)
    main_frame.pack(fill=BOTH,expand=1)

    #Frame para X Scrollbar
    sec = Frame(main_frame)
    sec.pack(fill=X,side=BOTTOM)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    #Agregar scrollbars al canvas
    x_scrollbar = ttk.Scrollbar(sec,orient=HORIZONTAL,command=my_canvas.xview)
    x_scrollbar.pack(side=BOTTOM,fill=X)
    y_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    y_scrollbar.pack(side=RIGHT,fill=Y)

    #Configuraciones del canvas
    my_canvas.configure(xscrollcommand=x_scrollbar.set)
    my_canvas.configure(yscrollcommand=y_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox(ALL))) 

    #Crear frame secundario DENTRO del canvas
    second_frame = Frame(my_canvas)

    #Agregar una window al nuevo frame
    my_canvas.create_window((0,0),window= second_frame, anchor="nw")

    filas, columnas = obtenerFilasColumnas()
    #Imprimir filas superiores
    i = 1
    for fila in filas:
        Label(second_frame,text=fila[0].upper(), font=('Helvetica 10 bold')).grid(row= 0, column= i, padx=8)
        i +=1
    #Imprimir columnas
    i = 1
    for columna in columnas:
        Label(second_frame,text=columna[0], font=('Helvetica 10 bold')).grid(row= i, column= 0, pady=4)
        i +=1
    #Imprimir filas inferiores
    j = len(columnas) + 1
    i = 1
    for fila in filas:
        Label(second_frame,text=fila[0].upper(), font=('Helvetica 10 bold')).grid(row= j, column= i, padx=8)
        i +=1

    #Imprimir cajones
    cajones = obtenerOcupados()
    for cajon in cajones:
        if cajon[2] == False:
            #Comprobar si es de discapacitados
            if cajon[4]:
                Label(second_frame,text='⬜', fg='blue').grid(row= int(cajon[1]), column= string.ascii_lowercase.index(cajon[0]) + 1, pady=4)
            else:
                Label(second_frame,text='⬜').grid(row= int(cajon[1]), column= string.ascii_lowercase.index(cajon[0]) + 1, pady=4)
        else:
            #Comprobar si no es un cajón sospechoso
            sospechoso = verificarCajonUnico(cajon[3])
            if sospechoso:
                Label(second_frame,text='⬛', fg='red').grid(row= int(cajon[1]), column= string.ascii_lowercase.index(cajon[0]) + 1, pady=4)
            else:
                Label(second_frame,text='⬛').grid(row= int(cajon[1]), column= string.ascii_lowercase.index(cajon[0]) + 1, pady=4)
    



def ventanaPrincipal():
    global root 
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

    notificacionesBoton = Button(root, text='CAJONES SOSPECHOSOS', command=lambda:obtenerCajonesSospechosos())
    notificacionesBoton.config(bg='#f4eb49', fg='black', padx=30, borderwidth=0)
    notificacionesBoton.place(x=505, y=115)

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
    botonVizualizar = Button(root, image=photo3, borderwidth=0, command=visualizar)
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

def verificarDatos():
    usuarioData = usuario.get()
    contrasenaData = contrasena.get()
    datosCorrectos = iniciarSesion.consultarBD(usuarioData, contrasenaData)

    if datosCorrectos:
        raizLogin.destroy()
        ventanaPrincipal()
        
    else:
        messagebox.showerror('Datos erroneos', 'Hay un error en el usuario o contraseña')


raizLogin = Tk()
raizLogin.title('The parking zone - Login')
raizLogin.resizable(False, False)
raizLogin.config(width=800, height=500)
raizLogin.iconbitmap('panel_admin\images\icono.ico')
raizLogin.config(bg='black')

#Logo izquierdo
logoImagen = PhotoImage(file='panel_admin\\images\\logoGde.gif')
labelImagen = Label(raizLogin, image=logoImagen)
labelImagen.config(width=400, height=500, bg='black')
labelImagen.place(x=0, y=0)

#Login derecha
usuario = StringVar()
contrasena = StringVar()
Label(raizLogin, text='USUARIO', bg='black', fg='#f4eb49', font=('Helvetica', 14, 'bold'),).place(x=500, y=125)
entryUsuario = Entry(textvariable=usuario, fg='black', bg='white', width=25)
Label(raizLogin, text='CONTRASEÑA', bg='black', fg='#f4eb49', font=('Helvetica', 14, 'bold'),).place(x=500, y=225)
entryContrasena = Entry(textvariable=contrasena, fg='black', bg='white', width=25)

entryUsuario.config(highlightbackground='#f4eb49', highlightthickness=3, font=('Helvetica', 12, 'bold'))
entryUsuario.place(x=500, y=160)

entryContrasena.config(show='*', highlightbackground='#f4eb49', highlightthickness=3, font=('Helvetica', 12, 'bold'))
entryContrasena.place(x=500, y=260)

botonLogin = Button(raizLogin, text='INICIAR SESIÓN', command=lambda:verificarDatos())
botonLogin.config(padx=10, fg='black', bg='#f4eb49', font=('Helvetica', 12, 'bold'))
botonLogin.place(x=538, y=350)

barraIzquierda = PhotoImage(file='panel_admin\\images\\barraIzquierdaGde.gif')
labelImagen = Label(raizLogin, image=barraIzquierda, bg='black')
labelImagen.place(x=0, y=20)

barraDerecha = PhotoImage(file='panel_admin\\images\\barraDerechaGde.gif')
labelImagen = Label(raizLogin, image=barraDerecha, bg='black')
labelImagen.place(x=0, y=450)


raizLogin.mainloop()