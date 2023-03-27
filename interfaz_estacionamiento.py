import string
import prettytable
from algoritmo_asignacion import conectar

def ver_estacionamiento():
    #obtener todos los lugares
    cursor = conectar()
    sql = '''SELECT id_cajon, fila, columna, ocupado FROM cajon ORDER BY id_cajon DESC limit 1''';
    cursor.execute(sql)
    cajon = cursor.fetchone()
    letra = cajon[1].lower()
    numero = int(cajon[2])
    sql = '''SELECT id_cajon, fila, columna, ocupado FROM cajon ORDER BY id_cajon''';
    cursor.execute(sql)
    cajon = cursor.fetchall()
    #print(cajon) #Todo el cajon
    print(cajon[0])
    print(cajon[0][3]) #estado de cajon true false
    #imprimir los datos
    longitud = len(cajon)
    
    alphabet = list(string.ascii_lowercase)
    #imprimir numeros y letras
    for i in range(numero + 1):
        print(i, end="    ")
    print("")
    print('a', end="    ")
    k = 1
    j = 1
    #Imprimir lugares vacios/ocupados
    for i in range(longitud):
        if cajon[i][3] == False:
            if j == numero:
                print('□')
                print(alphabet[k], end="    ")
                k = k + 1
                j = 0
            else:
                print('□', end = "    ")
        else:
            if j == numero:
                print('■')
                print(alphabet[k], end="    ")
                k = k + 1
                j = 0
            else:
                print('■', end = "    ")
        j = j+1
    cursor.close

ver_estacionamiento()