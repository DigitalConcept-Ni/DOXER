# import os
#
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# import json
# from django.db import transaction
# from django.http import JsonResponse
# from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from django.views.generic import CreateView, UpdateView, DeleteView, ListView
#
# # from Aplicaciones.RRHH.mixin import IsSuperUserMixin
# # from Apps.administration.forms import ConsultaForm, DocumentsForms
# from Apps.administration.models import *
# from Apps.administration.remove import removefiles
#
#
# class DocumentsListView(LoginRequiredMixin, ListView):
#     model = Documents
#     template_name = 'documents/list.html'
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             print(request.POST)
#             data = []
#             action = request.POST['action']
#             id = request.POST['id']
#             print(id)
#             if action == 'search_data':
#                 data = [d.toList() for d in Documents.objects.filter(pk=id)]
#                 # for d in Documents.objects.filter(pk=id):
#                 #     data.append(d.toJSON())
#                 print(data)
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data, safe=False)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Documentos'
#         context['title_query'] = 'Selecciona el documento a buscar'
#         context['create_url'] = reverse_lazy('administration:documentos_add')
#         context['entity'] = 'Documentos'
#         context['form'] = ConsultaForm()
#         context['list_url'] = reverse_lazy('administration:documentos_list')
#         return context
#
#
# class DocumentsCreateview(LoginRequiredMixin, CreateView):
#     model = Documents
#     form_class = DocumentsForms
#     template_name = 'documents/create.html'
#     success_url = reverse_lazy('administration:documentos_list')
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             print('request', request.POST)
#             action = request.POST['action']
#             if action == 'add':
#                 form = self.get_form()
#                 if form.is_valid():
#                     with transaction.atomic():
#                         detalle = json.loads(request.POST['vents'])
#
#                         file = request.FILES
#                         if 'file' in file:
#                             file = request.FILES['file']
#                         else:
#                             file = None
#
#                         exp = Documents()
#                         exp.expedients_id = int(detalle['expedientsAdministration'])
#                         exp.document_type_id = int(detalle['document_type'])
#                         exp.date = detalle['date']
#                         exp.file = file
#                         exp.save()
#                 else:
#                     data['error'] = form.errors
#         except Exception as e:
#             data['error'] = str(e)
#             print(data)
#         return JsonResponse(data)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Crear nuevo registro'
#         context['entity'] = 'Documentos'
#         context['list_url'] = self.success_url
#         context['action'] = 'add'
#         context['detail'] = []
#         return context
#
#
# class DocumentsUpdateiew(LoginRequiredMixin, UpdateView):
#     model = Documents
#     form_class = DocumentsForms
#     template_name = 'documents/create.html'
#     success_url = reverse_lazy('administration:documentos_list')
#
#     @method_decorator(login_required)
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'edit':
#                 form = self.get_form()
#                 if form.is_valid():
#                     with transaction.atomic():
#                         detalle = json.loads(request.POST['vents'])
#                         file = request.FILES
#
#                         if 'file' in file:
#                             file = request.FILES['file']
#                         elif detalle['file'] != '':
#                             if 'file-clear  ' in request.POST:
#                                 verifyfile = removefiles(detalle['file'])
#                                 if verifyfile:
#                                     file = None
#                                 else:
#                                     data = verifyfile
#                                     return JsonResponse(data)
#                             else:
#                                 file = detalle['file']
#                         else:
#                             file = None
#
#                         exp = self.get_object()
#                         exp.expedients_id = int(detalle['expedientsAdministration'])
#                         exp.document_type_id = int(detalle['document_type'])
#                         exp.date = detalle['date']
#                         exp.file = file
#                         exp.save()
#                 else:
#                     data['error'] = form.errors
#             else:
#                 data['error'] = 'No ha ingresado ninguna opcion'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Modificar Documento'
#         context['entity'] = 'Documentos'
#         context['list_url'] = self.success_url
#         context['action'] = 'edit'
#         return context
#
#
# class DocumentsDeleteview(LoginRequiredMixin, DeleteView):
#     model = Documents
#     form_class = DocumentsForms
#     template_name = 'documents/delete.html'
#     success_url = reverse_lazy('administration:documentos_list')
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             #  section for when you have to delete a file from the system
#             pathremove = os.path.join(settings.MEDIA_ROOT, str(self.object.file))
#             exitsfile = os.path.isfile(pathremove)
#             if exitsfile:
#                 os.remove(pathremove)
#             self.object.delete()
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Eliminar Documentos'
#         context['entity'] = 'Documentos'
#         context['list_url'] = self.success_url
#         context['action'] = 'delete'
#         return context
