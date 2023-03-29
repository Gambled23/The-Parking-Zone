import jinja2
import pdfkit
import qrcode
from datetime import datetime
import algoritmo_asignacion

def generarPDF (discapacitado):
    fecha = datetime.today().date()
    hora = f'{datetime.today().hour}:{datetime.today().minute}'
    file_path = 'H:\Codigos\The Parking Zone\qrticket.png'
    #obtener cajon asignado
    cajon = algoritmo_asignacion.obtenerCajon(discapacitado)
    letra = cajon[1].upper()
    numero = cajon[2]
    context = {'fecha': fecha, 'hora': hora, 'file_path': file_path, 'letra':letra, 'numero':numero}

    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template('ticket/boleto.html')
    output_text = template.render(context)
    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template('ticket/boleto.html')
    output_text = template.render(context)
    config = pdfkit.configuration(wkhtmltopdf='C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe')
    pdfkit.from_string(output_text, './ticket/ticket.pdf', configuration=config, css='ticket\style.css', options={"enable-local-file-access": ""})

def generarQR(discapacitado):
    cajon = algoritmo_asignacion.obtenerCajon(discapacitado)
    letra = cajon[1].upper()
    numero = cajon[2]
    data = f'{letra}{numero}'
    img = qrcode.make(data)
    img.save('./ticket/qrticket.png')

generarQR(True)
generarPDF(True)