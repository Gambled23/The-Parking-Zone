import psycopg2

def obtenerListaLugares():
    conn = psycopg2.connect(
        database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port='5432'
    )
    conn.autocommit = True

    cursor = conn.cursor()
    sql = '''SELECT DISTINCT fila FROM cajon ORDER BY fila asc'''
    cursor.execute(sql)
    listaFilas = cursor.fetchall()

    sql = '''SELECT DISTINCT cast(columna as integer) FROM cajon order by columna asc'''
    cursor.execute(sql)
    listaColumnas = cursor.fetchall()
    conn.close()

    listas = [listaFilas, listaColumnas]

    return listas

def modificarCajon(letra, numero, discapacitado, ocupado):
    conn = psycopg2.connect(
        database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port='5432'
    )
    conn.autocommit = True

    cursor = conn.cursor()
    #obtener cajon
    sql = f"select id_cajon from cajon where fila = '{letra}' and columna = '{numero}'"
    cursor.execute(sql)
    id_cajon = cursor.fetchone()[0]
    #actualizar cajon
    sql = f"UPDATE cajon SET discapacitados = cast({discapacitado} as boolean) WHERE id_cajon = {id_cajon}"
    cursor.execute(sql)
    sql = f"UPDATE cajon SET ocupado = cast({ocupado} as boolean) WHERE id_cajon = {id_cajon}"
    cursor.execute(sql)
    conn.close()

def obtenerFilasPosibles():
    conn = psycopg2.connect(
        database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port='5432'
    )
    conn.autocommit = True

    cursor = conn.cursor()
    sql = 'SELECT fila FROM cajon ORDER BY id_cajon desc LIMIT 1' #obtener ultima fila
    cursor.execute(sql)
    filasExistentes = cursor.fetchone()
    #obtener lista de letras del abecedario despues de la letra 'A'
    filasPosibles = [chr(i) for i in range(ord(filasExistentes[0].upper()) + 1, ord('Z') + 1)]
    conn.close()

    return filasPosibles
