from tkinter import *
from tkinter import messagebox
from configuration_scripts.scripts import createDatabase, habilitarCajones, crearAdmin, eliminarBD
import string

#Crear base de datos y tablas
try: 
    createDatabase()
except: #Si la base de datos ya existe
    desinstalar = messagebox.askyesno('Error', 'El programa ya está instalado ¿Desea desinstalarlo?')
    if desinstalar: 
        eliminarBD()
        messagebox.showinfo('Programa desinstalado', 'El programa ha sido desinstalado correctamente')
    exit()




root = Tk()
root.title('Instalación')
root.iconbitmap('panel_admin\images\iconoAzul.ico')
Label(root, text="Instalación", font=('Helvetica 17 bold'), pady=10, padx=25).grid(row=0, column=0, columnspan=4)

#Selección letras
Label(root, text='Fila máxima:').grid(row=1, column=0)
alphabet = list(string.ascii_uppercase)
variableFilas = StringVar()
variableFilas.set(alphabet[0])  # Valor por defecto de dropdown
OptionMenu(root, variableFilas, *alphabet).grid(row=1, column=1)

#Selección números
Label(root, text='Columna máxima:').grid(row=2, column=0)
r1, r2 = 1, 50
numbers = [item for item in range(r1, r2+1)]
variableColumnas = StringVar()
variableColumnas.set(numbers[0])  # Valor por defecto de dropdown
OptionMenu(root, variableColumnas, *numbers).grid(row=2, column=1)

#Usuario admin
usuarioObj = StringVar()
Label(root, text='Usuario admin').grid(row=3, column=0)
Entry(root, textvariable=usuarioObj).grid(row=3, column=1)

#Contraseña admin
contrasenaObj = StringVar()
Label(root, text='Contraseña admin', ).grid(row=4, column=0)
Entry(root, textvariable=contrasenaObj, show='*').grid(row=4, column=1)

def enviar():
    #Crear cajones
    fila = variableFilas.get()
    fila = fila.lower()
    columna = variableColumnas.get()
    columna = int(columna)
    habilitarCajones(fila, columna)

    #Crear admin
    usuario = usuarioObj.get()
    contrasena = contrasenaObj.get()
    crearAdmin(usuario, contrasena)
    messagebox.showinfo('The parking zone','Has terminado el proceso de instalación')
    root.destroy()
    
botonEnviar = Button(root, text='Configurar', command=lambda: enviar())
botonEnviar.grid(row=5, column=1, pady=10, padx=10)







root.mainloop()