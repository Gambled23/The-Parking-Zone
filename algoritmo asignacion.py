import psycopg2

def conectar():
    conn = psycopg2.connect(
        database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True
    #Crear el cursor
    cursor = conn.cursor()
    return cursor

def obtenerUltimoRegistro():
    cursor = conectar()
    #Obtener el cajón más cercano desocupado
    sql = '''SELECT * FROM cajon WHERE ocupado IS NOT TRUE ORDER BY id_cajon ASC LIMIT 1''';
    cursor.execute(sql)
    cajon = cursor.fetchone()
    print(cajon)
    print(cajon[0])
    cursor.close()

obtenerUltimoRegistro()
