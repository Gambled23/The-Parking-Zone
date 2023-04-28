import algoritmo_asignacion
from tkinter import messagebox

def comprobarCajon(listaCajones):
    cursor = algoritmo_asignacion.conectar()
    cajonStr = ''
    j = 1
    for i in listaCajones:
        sql = f"SELECT ocupado from cajon WHERE id_cajon = '{j}'"
        cursor.execute(sql)
        cajon = cursor.fetchone()[0]
        if not cajon == i:
            cajonStr = cajonStr + f'Cajon con ID {j} no coincide\n'
        j+=1
    messagebox.showwarning('Cajones inconsistentes', cajonStr)
    cursor.close()

#comprobarCajon([1,1,1,0,0,1,1])