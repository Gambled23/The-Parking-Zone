import psycopg2
import os

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
    if not listaSospechosos:
        print('No hay autos sospechosos')
    for i in listaSospechosos:
        sql = f"SELECT fila, columna from cajon WHERE id_cajon = {i[1]}"
        cursor.execute(sql)
        cajonSospechoso = cursor.fetchone()
        print(f'El auto en el cajón {cajonSospechoso[0].upper()}-{cajonSospechoso[1]} lleva estacionado desde: {i[2]}')
    conn.close()
