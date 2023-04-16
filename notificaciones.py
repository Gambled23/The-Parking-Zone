import psycopg2

def obtenerCajonesSospechosos():
    conn = psycopg2.connect(
        database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    sql = "SELECT * from ticket WHERE hora_entrada < NOW() - INTERVAL '48 hours'"
    cursor.execute(sql)
    cajones = cursor.fetchall()
    conn.close()
    return cajones