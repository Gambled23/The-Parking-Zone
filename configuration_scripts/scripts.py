import psycopg2
import string

def createDatabase():
   conn = psycopg2.connect(
      database="postgres", user='postgres', password='usuario', host='127.0.0.1', port= '5432'
   )
   conn.autocommit = True

   #Crear el cursor
   cursor = conn.cursor()

   sql = '''CREATE database parkingzone''';

   #Ejecutar query de crear BD
   cursor.execute(sql)
   print("Base de datos creada")

   #crear las tablas
   createTables()

   conn.close()

def createTables():
   conn = psycopg2.connect(
      database="parkingzone", user='postgres', password='usuario', host='127.0.0.1', port= '5432'
   )
   conn.autocommit = True

   #Crear el cursor
   cursor = conn.cursor()

   #Crear tabla cajon
   sql = '''CREATE TABLE cajon (id_cajon SERIAL, PRIMARY KEY(id_cajon), fila VARCHAR(4), columna VARCHAR(4), discapacitados BOOL DEFAULT false, estado BOOL DEFAULT null)''';
   cursor.execute(sql)
   print("Tabla cajon creada")

   #Crear tabla ticket
   sql = '''CREATE TABLE ticket (id_ticket SERIAL, PRIMARY KEY(id_ticket), id_cajon INTEGER, CONSTRAINT fk_cajon FOREIGN KEY(id_cajon) REFERENCES cajon(id_cajon), hora_entrada TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP, hora_salida TIMESTAMP WITH TIME ZONE)''';
   cursor.execute(sql)
   print("Tabla ticket creada")

   #Crear tabla admin
   sql = '''CREATE TABLE administrador(id_administrador SERIAL, PRIMARY KEY(id_administrador), usuario TEXT, contrasena TEXT)''';
   cursor.execute(sql)
   print("Tabla administrador creada")

   conn.close()

def habilitarCajones(letra, numero):
   alphabet = list(string.ascii_lowercase)
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
