from tkinter import *

def iniciarSesion(usuario, contrasena):
    pass

root = Tk()
root.title('The parking zone - Login')
root.resizable(False, False)
root.config(width=800, height=500)
root.iconbitmap('panel_admin\images\icono.ico')
root.config(bg='black')

#Logo izquierdo
logoImagen = PhotoImage(file='panel_admin\\images\\logoGde.gif')
labelImagen = Label(root, image=logoImagen)
labelImagen.config(width=400, height=500, bg='black')
labelImagen.place(x=0, y=0)

#Login derecha
usuario = StringVar()
contrasena = StringVar()
Label(root, text='USUARIO', bg='black', fg='#f4eb49', font=('Helvetica', 14, 'bold'),).place(x=500, y=125)
entryUsuario = Entry(textvariable=usuario, fg='black', bg='white', width=25)
Label(root, text='CONTRASEÑA', bg='black', fg='#f4eb49', font=('Helvetica', 14, 'bold'),).place(x=500, y=225)
entryContrasena = Entry(textvariable=contrasena, fg='black', bg='white', width=25)

entryUsuario.config(highlightbackground='#f4eb49', highlightthickness=3, font=('Helvetica', 12, 'bold'))
entryUsuario.place(x=500, y=160)

entryContrasena.config(show='*', highlightbackground='#f4eb49', highlightthickness=3, font=('Helvetica', 12, 'bold'))
entryContrasena.place(x=500, y=260)

botonLogin = Button(root, text='INICIAR SESIÓN', command=lambda:iniciarSesion(usuario, contrasena))
botonLogin.config(padx=10, fg='black', bg='#f4eb49', font=('Helvetica', 12, 'bold'))
botonLogin.place(x=538, y=350)

barraIzquierda = PhotoImage(file='panel_admin\\images\\barraIzquierdaGde.gif')
labelImagen = Label(root, image=barraIzquierda, bg='black')
labelImagen.place(x=0, y=20)

barraDerecha = PhotoImage(file='panel_admin\\images\\barraDerechaGde.gif')
labelImagen = Label(root, image=barraDerecha, bg='black')
labelImagen.place(x=0, y=450)


root.mainloop()
