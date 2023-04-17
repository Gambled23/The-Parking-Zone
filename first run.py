from configuration_scripts.scripts import createDatabase, habilitarCajones, crearAdmin

#Crear base de datos y tablas
try: 
    createDatabase()
except: #Si la base de datos ya existe
    print('El programa ya ha sido instalado')
    exit()

#Crear cajones
print('Bienvenido a la instalacion de The Parking Zone, deberá ingresar unos datos antes del primer uso\n')
print('Los estacionamientos se componen de filas y columnas (A-21, C-12, X-03, etc)')
letra = input("Ingresa la ultima letra del estacionamiento: ")
numero = int(input("Ingresa el ultimo número del estacionamiento: "))
habilitarCajones(letra, numero)

print('Para ingresar al panel de administrador será necesario crear un usuario y una contraseña, no olvides estos datos ni los compartas con nadie externo')
usuario = input('Ingresa un usuario para el administrador:')
contrasena = input('Ingresa una contraseña:')
crearAdmin(usuario, contrasena)

print('Haz terminado el proceso de configuración, ya puedes usar el programa!')