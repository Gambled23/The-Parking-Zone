import psycopg2
import string

def obtenerFilasColumnas():
    conn = psycopg2.connect(database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    sql = 'SELECT DISTINCT fila FROM cajon ORDER BY fila ASC'
    cursor.execute(sql)
    fila = cursor.fetchall()
    sql = 'SELECT DISTINCT columna::INTEGER FROM cajon ORDER BY columna ASC'
    cursor.execute(sql)
    columna = cursor.fetchall()
    conn.close()
    return fila, columna

def obtenerOcupados():
    conn = psycopg2.connect(database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()
    sql = 'SELECT fila, columna, ocupado from cajon'
    cursor.execute(sql)
    cajones = cursor.fetchall()
    print(cajones[40][0])
    
    print(string.ascii_lowercase.index(cajones[40][0]) + 1) 
    conn.close()
    return cajones


obtenerOcupados()