import psycopg2
import os
from tkinter import messagebox
from datetime import datetime

def verificarCajonUnico(id_cajon):
    conn = psycopg2.connect(
        database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    sql = f"SELECT hora_entrada, hora_salida from ticket WHERE id_cajon = {id_cajon}"
    cursor.execute(sql)
    cajon = cursor.fetchone()
    conn.close()

    #Si es cajon sospechoso
    try:
        intervalo = datetime.now() - cajon[0]
        if intervalo.days >= 2:
            return True
        else:
            return False
    except:
        return False
    
def obtenerCajonesSospechosos():
    os.system('cls')
    conn = psycopg2.connect(
        database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    sql = "SELECT * from ticket WHERE hora_entrada < NOW() - INTERVAL '48 hours' and hora_salida IS NULL"
    cursor.execute(sql)
    listaSospechosos = cursor.fetchall()
    autosStr = ''
    if not listaSospechosos:
        autosStr = 'No hay cajones sospechosos'
    for i in listaSospechosos:
        sql = f"SELECT fila, columna from cajon WHERE id_cajon = {i[1]}"
        cursor.execute(sql)
        cajonSospechoso = cursor.fetchone()
        autosStr = autosStr + f"El auto en el cajón {cajonSospechoso[0].upper()}-{cajonSospechoso[1]} lleva estacionado desde: {i[2]}\n"
    messagebox.showinfo('Cajones sospechosos ', autosStr)
    conn.close()