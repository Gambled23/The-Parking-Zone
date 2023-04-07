import psycopg2

def conectar():
    conn = psycopg2.connect(
        database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True
    #Crear el cursor
    cursor = conn.cursor()
    return cursor

def obtenerCajon(discapacitado):
    cursor = conectar()
    #Obtener el cajón más cercano desocupado
    if discapacitado:
        sql = '''SELECT * FROM cajon WHERE ocupado IS NOT TRUE and discapacitados IS TRUE ORDER BY id_cajon ASC LIMIT 1'''
    else:
        sql = '''SELECT * FROM cajon WHERE ocupado IS NOT TRUE and discapacitados IS NOT TRUE ORDER BY id_cajon ASC LIMIT 1'''
    cursor.execute(sql)
    cajon = cursor.fetchone()
    cursor.close()
    return cajon
