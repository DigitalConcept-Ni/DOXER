import os.path

from PyPDF2 import PdfFileReader, PdfFileWriter
# from tablib import Dataset

# from Aplicaciones.RRHH.models import Indexaciones
# from Aplicaciones.masivo.resources import ActualizacionResource


def extract_page(request):
    data = {}
    doc_name = request['name_file']
    pages = request.getlist('page')

    carpeta = request['directory']
    path = 'C:/repositorios/hemco2/hemco/media/migration/' + carpeta + '/' + doc_name
    # path = '/home/ubuntu/hemco2/hemco/media/migration/' + carpeta + '/' + doc_name
    pdf_reader = PdfFileReader(open(path, 'rb'))
    pdf_writer = PdfFileWriter()

    num_pages = ''
    no_render = []
    for p in pages:
        num_pages += '_' + p
        n = int(p)
        no_render.append(n)
        pdf_writer.addPage(pdf_reader.getPage(n))

    name, type = os.path.splitext(doc_name)

    with open('C:/repositorios/hemco2/hemco/media/pages/{}{}.pdf'.format(name, num_pages), 'wb') as salida:
    # with open('/home/ubuntu/hemco2/hemco/media/pages/{}{}.pdf'.format(name, num_pages), 'wb') as salida:
        pdf_writer.write(salida)

    new_pdf = 'pages/'+name+num_pages+'.pdf'

    cedula = request['cedula']
    seccion = request['seccion']
    documento = request['documento']
    fecha_documento = request['fecha_documento']

    dataset = Dataset()
    dataset.headers = ['id', 'cedula', 'seccion', 'documento', 'fecha_documento', 'archivo']
    dataset.append(['', cedula, seccion, documento, fecha_documento, new_pdf])

    actualizacion = ActualizacionResource()
    result = actualizacion.import_data(dataset, dry_run=True)  # Test the data import
    # print('problemas: ', result.has_errors())
    print(result.invalid_rows)
    if result.has_errors():
        print('error')
        data['error'] = 'No ha ingresado ninguna opcion'
    if not result.has_errors():
        print('no error')
        if result.invalid_rows:
            result.append_invalid_row()
            data['error'] = 'Hay valores invalidos'
        else:
            actualizacion.import_data(dataset, dry_run=False)  # Actually import now
    index_file = request['num_file']
    data['no_render'] = no_render
    data['openFile'] = index_file
    return data
