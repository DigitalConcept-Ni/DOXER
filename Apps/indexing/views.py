from django.core.files import File
from django.http import JsonResponse
from django.shortcuts import render
import os
import shutil

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from Apps.indexing.forms import IndexingDocumentsForm
from Apps.indexing.extrac_pages import extract_page


# def IndexacionView(request):
#     path = 'C:/repositorios/hemco2/hemco/media/migration'
#     archivo = os.listdir(path)
#     archi = []
#     for l in archivo:
#         archi.append(l)
#     data = {
#         'nombre': 'bryan',
#         'title': 'Indexar documentos',
#         'form': IndexadoForms(),
#         'archivos': archi
#     }
#     return render(request, 'index_doc/index.html', data)



class IndexacionDoc(TemplateView):
    template_name = 'index_doc/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        folder = 'ACTUALIZACION'
        try:
            action = request.POST['action']
            path = 'C:/repositorios/hemco2/hemco/media/'
            # path = '/home/ubuntu/hemco2/hemco/media/'
            if action == 'search_directory':
                carpetas = []
                id = 0
                for c in os.listdir(os.path.join(path, 'migration')):
                    id += 1
                    if os.path.isdir(os.path.join(path)):
                        carpetas.append({'id': id, 'name': c})
                data['carpetas'] = carpetas
            elif action == 'indexar':
                print(request.POST)
                dat = extract_page(request.POST)
                data['no_render'] = dat['no_render']
                data['openFile'] = dat['openFile']
                print(data)
            elif action == 'refresh':
                carpeta = request.POST['carpeta']
                archivo = os.listdir(os.path.join(path, 'migration', carpeta))
                data['archivos'] = archivo
                data['files'] = len(archivo)
            elif action == 'next':

                doc_name = request.POST['doc_name']
                carpeta = request.POST['carpeta']
                shutil.move(path + 'migration/' + carpeta + '/' + doc_name, path + 'workup')
            elif action == 'search_section_id':
                # data = [{'id': '', 'text': '----------'}]
                for i in Documentos.objects.filter(pk=request.POST['id']):
                    # print(i.seccion.id)
                    data['id'] = i.seccion.id
                return JsonResponse(data, safe=False)
            elif action == 'insert_file':
                try:
                    file = request.FILES['file']
                    exist = os.path.exists(path + '/migration/' + folder)
                    # print(exist)
                    if exist == False:
                        os.mkdir(path + '/migration/' + folder)
                    with open('C:/repositorios/hemco2/hemco/media/migration/'+ folder +'/{}'.format(file), 'wb+') as des:
                    # with open('/home/ubuntu/hemco2/hemco/media/migration/'+ folder +'/{}'.format(file), 'wb+') as des:
                        for chunk in file.chunks():
                            des.write(chunk)
                    data['info'] = 'El archivo ha sido cargado correctamente. Seleccione la carpeta ACTUALIZACION.'
                except Exception as e:
                    data['error'] = str(e)
            elif action == 'delete_file':
                file = request.POST['docname']
                try:
                    os.remove('C:/repositorios/hemco2/hemco/media/migration/' + folder + '/' + file )
                    # os.remove('/home/ubuntu/hemco2/hemco/media/migration/'+folder + '/' + file )
                    data['info'] = 'Archivio eliminado correctamente'
                    return JsonResponse(data)
                except Exception as e:
                    data['error'] = str(e)
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Indexar documentos'
        data['form'] = IndexingDocumentsForm()
        data['action'] = 'indexar'
        return data
