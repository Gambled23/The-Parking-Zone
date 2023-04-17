from generar_boleto import generarPDF
import os

while True:
    os.system('cls')
    discapacitado = int(input('-------THE PARKING ZONE-------\n    1) Discapacitado\n    2) Normal\n'))

    if discapacitado == 1:
        generarPDF(True)
    else:
        generarPDF(False)
