import jinja2
import pdfkit
import qrcode
from datetime import datetime

def generarPDF ():
    my_name = "Cesar"
    today_date = datetime.today().strftime("%d %b, %Y")
    file_path = 'H:\Codigos\The Parking Zone\qrticket.png'

    context = {'my_name': my_name,'today_date': today_date, 'file_path': file_path}
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

def generarQR(data):
    img = qrcode.make(data)
    img.save('./ticket/qrticket.png')

generarQR('A-22')
generarPDF()