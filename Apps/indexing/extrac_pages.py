import os.path

from PyPDF2 import PdfFileReader, PdfFileWriter
# from Aplicaciones.RRHH.models import Indexaciones
# from Aplicaciones.masivo.resources import ActualizacionResource
from django.db import transaction

from Apps.administration.models import Documents
from config import settings


def extract_page(request):
    data = {}
    try:
        doc_name = request['name_file']
        pages = request.getlist('page')
        carpeta = request['directory']

        #  HERE WE SELECT THE FILE FROM ITS FOLDER
        path = os.path.join(settings.BASE_DIR, 'media')
        openfilepath = os.path.join(path, 'indexation', carpeta, doc_name)

        pdf_reader = PdfFileReader(open(openfilepath, 'rb'))
        pdf_writer = PdfFileWriter()

        num_pages = ''
        no_render = []
        for p in pages:
            num_pages += '_' + p
            n = int(p)
            no_render.append(n)
            pdf_writer.addPage(pdf_reader.getPage(n))

        name, type = os.path.splitext(doc_name)

        # here we confirm if the folder exists where we will save the files
        confirmpathfolder = path + '/pages'
        exist = os.path.exists(confirmpathfolder)
        if not exist:
            os.mkdir(confirmpathfolder)
        with open('{}/{}{}.pdf'.format(confirmpathfolder, name, num_pages), 'wb') as salida:
            pdf_writer.write(salida)

        new_pdf = 'pages/' + name + num_pages + '.pdf'

        with transaction.atomic():
            dc = Documents()
            dc.expedients_id = request['expedientsAdministration']
            dc.document_type_id = request['document_type']
            dc.date = request['date']
            dc.file = new_pdf
            dc.save()

        index_file = request['num_file']
        data['no_render'] = no_render
        data['openFile'] = index_file
    except Exception as e:
        data['error'] = str(e)
    return data
