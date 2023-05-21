import psycopg2

def desocuparCajon(cajon):
    conn = psycopg2.connect(database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()

    #obtener id_cajon
    sql = f"SELECT id_cajon FROM cajon WHERE fila = '{cajon[0].lower()}' and columna = '{cajon[1]}'"
    cursor.execute(sql)
    id_cajon = cursor.fetchone()[0]

    #Actualizar tabla ticket con hora_Salida
    sql = f"UPDATE ticket SET hora_salida = CURRENT_TIMESTAMP where id_cajon = {id_cajon}"
    cursor.execute(sql)

    #Actualizar tabla cajon como disponible
    sql = f"UPDATE cajon SET ocupado = False where id_cajon = {id_cajon}"
    cursor.execute(sql)

    #Eliminar notificaciones
    sql = f"DELETE from notificaciones where id_cajon = {id_cajon}"
    cursor.execute(sql)

    conn.close()

def notificarCajonIncorrecto(fila, columna):
    conn = psycopg2.connect(database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port= '5432')
    conn.autocommit = True
    cursor = conn.cursor()

    #obtener id_cajon
    sql = f"SELECT id_cajon FROM cajon where fila = '{fila.lower()}' and columna = '{columna}'"
    cursor.execute(sql)
    id_cajon = cursor.fetchone()[0]
    print(id_cajon)

    #generar nueva notificación
    sql = f"INSERT into notificaciones (id_cajon) values ({id_cajon})"
    cursor.execute(sql)
    conn.close()