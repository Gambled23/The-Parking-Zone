import string
import os
from prettytable import PrettyTable
from algoritmo_asignacion import conectar

def ver_estacionamiento():
    os.system('cls')
    #obtener el ultimo lugar
    cursor = conectar()
    sql = '''SELECT id_cajon, fila, columna, ocupado FROM cajon ORDER BY id_cajon DESC limit 1''';
    cursor.execute(sql)
    cajon = cursor.fetchone()
    letra = cajon[1].lower()
    numero = int(cajon[2])

    estacionamiento = PrettyTable()
    listaNumeros = [] #El header de la tabla
    for i in range(0, numero + 1):
        listaNumeros.insert(i, i)
    estacionamiento.field_names = listaNumeros

    alphabet = list(string.ascii_lowercase)
    for j in alphabet:
        listaDisponibles = [j]
        sql = ''f"SELECT id_cajon, fila, columna, ocupado FROM cajon WHERE fila = '{j}' ORDER BY id_cajon"'';
        cursor.execute(sql)
        cajon = cursor.fetchall()
        for i in range(numero):
            if cajon[i][3] == True:
                listaDisponibles.append('■')
            else:
                listaDisponibles.append('□')
        estacionamiento.add_row(listaDisponibles)
        if j == letra:
            break
    print(estacionamiento)

    cursor.close