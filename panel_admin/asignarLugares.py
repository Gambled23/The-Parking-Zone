import psycopg2
import string

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
    global ultimoCajon
    ultimoCajon = [cajon[1], cajon[2]]
    return cajon

def insertarFila(letra, numero):
   numero = int(numero)
   letra = letra.lower()
   alphabet = list(string.ascii_lowercase)
   alphabet = alphabet[alphabet.index(ultimoCajon[0]) + 1:alphabet.index(letra) + 1]
   conn = psycopg2.connect(
      database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port= '5432'
   )
   conn.autocommit = True
   #Crear el cursor
   cursor = conn.cursor()

   for i in alphabet:
      j = 1
      bandera = True
      while bandera:
         sql = ''f"INSERT into cajon (fila, columna) values ('{i}', '{j}')"'';
         cursor.execute(sql)
         j = j + 1
         if j == numero + 1:
            bandera = False
      if i == letra:
         return
