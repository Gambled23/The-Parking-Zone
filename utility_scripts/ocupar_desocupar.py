import psycopg2

#Si recibe true ocupa todos los espacios, si es false los desocupa
def ocuparTodo(ocupar):
    conn = psycopg2.connect(
        database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    if ocupar:
        sql = 'UPDATE cajon SET ocupado = True'
    else:
        sql = 'UPDATE cajon SET ocupado = False'
    cursor.execute(sql)
    conn.close()

ocuparTodo(False)