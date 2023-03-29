import psycopg2

# Toda desocupado y sin discapacitados


def casoBase():
    conn = psycopg2.connect(
        database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port='5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    sql = '''UPDATE cajon SET ocupado = False'''
    cursor.execute(sql)
    sql = ''"UPDATE cajon SET discapacitados = False"''
    cursor.execute(sql)
    conn.close()

# Toda la fila de A es discapacitados, ocupados del 1-5
def caso1():
    conn = psycopg2.connect(
        database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port='5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    sql = '''UPDATE cajon SET ocupado = True WHERE id_cajon < 6'''
    cursor.execute(sql)
    sql = ''"UPDATE cajon SET discapacitados = True WHERE fila = 'a'"''
    cursor.execute(sql)
    conn.close()

# Discapacitados toda A y ocupados random
def caso2():
    conn = psycopg2.connect(
        database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port='5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    sql = '''UPDATE cajon SET ocupado = True WHERE id_cajon = 2;
UPDATE cajon SET ocupado = True WHERE id_cajon = 6;
UPDATE cajon SET ocupado = True WHERE id_cajon = 12;
UPDATE cajon SET ocupado = True WHERE id_cajon = 32;
UPDATE cajon SET ocupado = True WHERE id_cajon = 4;
UPDATE cajon SET ocupado = True WHERE id_cajon = 5;
UPDATE cajon SET ocupado = True WHERE id_cajon = 31;
UPDATE cajon SET ocupado = True WHERE id_cajon = 33;'''
    cursor.execute(sql)
    sql = ''"UPDATE cajon SET discapacitados = True WHERE fila = 'a'"''
    cursor.execute(sql)
    conn.close()

