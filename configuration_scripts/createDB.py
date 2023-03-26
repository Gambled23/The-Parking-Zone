import psycopg2

#Establecer conexión con datos default

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

   conn.close()