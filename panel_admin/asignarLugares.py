import psycopg2

def obtenerUltimosDatos():
    conn = psycopg2.connect(
        database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port='5432'
    )
    conn.autocommit = True
    # Crear el cursor
    cursor = conn.cursor()
    sql = '''SELECT * FROM cajon ORDER BY id_cajon desc LIMIT 1'''
    cursor.execute(sql)
    cajon = cursor.fetchone()
    conn.close()
    ultimoCajon = [cajon[1], cajon[2]]
    print(ultimoCajon)
    return cajon

def insertarFila(letraStr, numeroStr):
    letra = letraStr.lower()
    numero = int(numeroStr)
    conn = psycopg2.connect(
        database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port='5432'
    )
    conn.autocommit = True
    # Crear el cursor
    cursor = conn.cursor()
    j = 1
    bandera = True
    while bandera:
        sql = ''f"INSERT into cajon (fila, columna) values ('{letra}', '{j}')"''
        cursor.execute(sql)
        j = j + 1
        if j == numero + 1:
            bandera = False
    conn.close()
