import psycopg2

def consultarBD(usuario, contrasena):
    #Conectar
    usuarioRegistrado = False
    conn = psycopg2.connect(
        database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()

    #Obtener todos los admin
    sql = f'SELECT * FROM administrador ORDER BY id_administrador ASC'
    cursor.execute(sql)
    admins = cursor.fetchall()

    #comprobar cada usuario de admin
    for i in admins:
        if usuario == i[1] and contrasena == i[2]: #Si usuario y contraseña coinciden
            usuarioRegistrado = True

    conn.close()
    return usuarioRegistrado