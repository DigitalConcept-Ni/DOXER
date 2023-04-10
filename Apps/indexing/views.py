# from django.http import JsonResponse
# import os
# import shutil
#
# # Create your views here.
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from django.views.generic import TemplateView
# from Apps.indexing.forms import IndexingDocumentsForm
# from Apps.indexing.extrac_pages import extract_page
#
# # def IndexacionView(request):
# #     path = 'C:/repositorios/hemco2/hemco/media/migration'
# #     archivo = os.listdir(path)
# #     archi = []
# #     for l in archivo:
# #         archi.append(l)
# #     data = {
# #         'nombre': 'bryan',
# #         'title': 'Indexar documentos',
# #         'form': IndexadoForms(),
# #         'archivos': archi
# #     }
# #     return render(request, 'index_doc/index.html', data)
# from config import settings
#
#
# class IndexacionDoc(TemplateView):
#     template_name = 'index_doc/index.html'
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         folder = 'indexation'
#         path = os.path.join(settings.BASE_DIR, 'media')
#         pathsave = os.path.join(path, folder)
#         action = request.POST['action']
#
#         try:
#             if action == 'search_directory':
#                 carpetas = []
#                 id = 0
#                 for c in os.listdir(os.path.join(path, 'indexation')):
#                     id += 1
#                     if os.path.isdir(os.path.join(path)):
#                         carpetas.append({'id': id, 'name': c})
#                 data['carpetas'] = carpetas
#             elif action == 'indexar':
#                 dat = extract_page(request.POST)
#                 data['no_render'] = dat['no_render']
#                 data['openFile'] = dat['openFile']
#             elif action == 'refresh':
#                 carpeta = request.POST['carpeta']
#                 archivo = os.listdir(os.path.join(pathsave, carpeta))
#                 data['archivos'] = archivo
#                 data['files'] = len(archivo)
#             elif action == 'next':
#                 doc_name = request.POST['doc_name']
#                 carpeta = request.POST['carpeta']
#                 parthdelete = os.path.join(pathsave, carpeta, doc_name)
#                 # Se toma le desicion que al darle sigueinte documento
#                 # el documento sea eliminado y no movido de carpeta
#                 # shutil.move(path + 'migration/' + carpeta + '/' + doc_name, path + 'workup')
#                 os.remove(parthdelete)
#             elif action == 'insert_file':
#                 try:
#                     file = request.FILES['file']
#                     pathway = os.path.join(pathsave, 'upload')
#                     exist = os.path.exists(pathway)
#                     if not exist:
#                         os.mkdir(pathway)
#                     with open(pathway + '/{}'.format(file), 'wb+') as des:
#                         for chunk in file.chunks():
#                             des.write(chunk)
#                     data['info'] = 'El archivo ha sido cargado correctamente. Seleccione la carpeta Upload'
#                 except Exception as e:
#                     data['error'] = str(e)
#                     print(data)
#             elif action == 'delete_file':
#                 file = request.POST['docname']
#                 directory = request.POST['directory']
#                 pathremove = os.path.join(pathsave, directory, file)
#                 try:
#                     os.remove(pathremove)
#                     # os.remove('/home/ubuntu/hemco2/hemco/media/migration/'+folder + '/' + file )
#                     data['info'] = 'Archivio eliminado correctamente'
#                 except Exception as e:
#                     data['error'] = str(e)
#                 return JsonResponse(data)
#         except Exception as e:
#             data['error'] = str(e)
#             print(data)
#         return JsonResponse(data, safe=False)
#
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         data['title'] = 'Indexar documentos'
#         data['form'] = IndexingDocumentsForm()
#         data['action'] = 'indexar'
#         return data
