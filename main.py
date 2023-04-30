from generar_boleto import generarPDF
import os

while True:
    os.system('cls')
    discapacitado = int(input('-------THE PARKING ZONE-------\n    1) Discapacitado\n    2) Normal\n'))

    if discapacitado == 1:
        try:
            generarPDF(True)
        except:
            input('Ya no hay cajones especiales disponibles, intente con un cajón normal')
    else:
        try:
            generarPDF(False)
        except:
            print('Ya no hay cajones normales disponibles')
            input('Lamentamos las molestias')
