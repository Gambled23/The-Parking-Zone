import jinja2
import pdfkit
import qrcode
from datetime import datetime
import algoritmo_asignacion

#Actualizar a ocupado registro de tabla cajon
def actualizarTablas(cajon):
    cursor = algoritmo_asignacion.conectar();
    sql = ''f"UPDATE cajon SET ocupado = True WHERE id_cajon = '{cajon[0]}'"'';
    cursor.execute(sql)
    
    #Insertar registro a tabla ticket
    sql = ''f"INSERT into ticket(id_cajon) values ({cajon[0]})"'';
    cursor.execute(sql)
    cursor.close()

#GenerarPDF requiere saber si es de discapacitados o no
def generarPDF (discapacitado):
    fecha = datetime.today().date()
    hora = f'{datetime.today().hour}:{datetime.today().minute}'
    #generar qr
    cajon = algoritmo_asignacion.obtenerCajon(discapacitado)
    letra = cajon[1].upper()
    numero = cajon[2]
    generarQR(cajon)
    file_path = 'H:\Codigos\The Parking Zone\qrticket.png'
    context = {'fecha': fecha, 'hora': hora, 'file_path': file_path, 'letra':letra, 'numero':numero}

    #Toda la madre para generar el pdf
    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template('ticket/boleto.html')
    output_text = template.render(context)
    config = pdfkit.configuration(wkhtmltopdf='C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe')
    pdfkit.from_string(output_text, './ticket/ticket.pdf', configuration=config, css='ticket\style.css', options={"enable-local-file-access": ""})
    
    actualizarTablas(cajon)

def generarQR(cajon):
    letra = cajon[1].upper()
    numero = cajon[2]
    data = f'{letra}{numero}'
    img = qrcode.make(data)
    img.save('./ticket/qrticket.png')

generarPDF(False)