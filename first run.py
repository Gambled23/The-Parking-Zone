from configuration_scripts.scripts import createDatabase, habilitarCajones

#Crear base de datos y tablas
createDatabase()

#Crear cajones
print('Bienvenido a la instalacion de The Parking Zone, deberá ingresar unos datos antes del primer uso\n')
print('Los estacionamientos se componen de filas y columnas (A-21, C-12, X-03, etc)')
letra = input("Ingresa la ultima letra del estacionamiento: ")
numero = int(input("Ingresa el ultimo número del estacionamiento: "))
habilitarCajones(letra, numero)
