# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# import json
# from django.db import transaction
# from django.db.models import Max
# from django.http import JsonResponse
# from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from django.views.generic import CreateView, UpdateView, DeleteView, ListView
#
# # from Aplicaciones.RRHH.mixin import IsSuperUserMixin
# from Apps.administration.forms import DocumentacionForms, PersonalInfoForms, ConsultaForm
# from Apps.administration.models import *
#
#
# def personal(request):
#     data = {
#         'name': 'Bryan',
#         'surname': 'Urbina',
#         'title': 'HOME | DOXER'
#     }
#     return render(request, 'expedientsAdministration/personal.html', data)
#
#
# class ExpedientsListView(LoginRequiredMixin, ListView):
#     model = Expedients
#     template_name = 'expedientsAdministration/list.html'
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             data = []
#             action = request.POST['action']
#             id = request.POST['id']
#             print(request.POST)
#             print(action)
#             if action == 'search_data':
#                 print(id)
#                 e = Expedients.objects.filter(pk=id)
#                 data = [e.toLIST() for e in Expedients.objects.filter(pk=id)]
#                 print(data)
#             elif action == 'search_personal_info':
#                 print('busqueda de info')
#                 for u in Personals.objects.filter(expedient_id=request.POST['id']):
#                     data.append([u.id,
#                                  u.expedient_id,
#                                  u.names,
#                                  u.surnames,
#                                  u.phone_number,
#                                  u.address,
#                                  u.card_id])
#                 print(data)
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data, safe=False)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Expedientes Registrados'
#         context['title_query'] = 'Seleccione el expediente a consultar'
#         context['create_url'] = reverse_lazy('administration:expedients_add')
#         context['entity'] = 'Expedientes'
#         context['form'] = ConsultaForm
#         context['list_url'] = reverse_lazy('administration:expedients_list')
#         return context
#
#
# class ExpedientsCreateview(LoginRequiredMixin, CreateView):
#     model = Expedients
#     form_class = DocumentacionForms
#     template_name = 'expedientsAdministration/create.html'
#     success_url = reverse_lazy('administration:expedients_list')
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             # print('request', request.POST)
#             action = request.POST['action']
#             if action == 'add':
#                 with transaction.atomic():
#                     detalle = json.loads(request.POST['vents'])
#                     print(detalle)
#
#                     exp = Expedients()
#                     exp.departament_id = int(detalle['departament'])
#                     exp.personal_info = detalle['personal_info']
#                     exp.serial_id = int(detalle['serial'])
#                     exp.sub_serial_id = int(detalle['sub_serial'])
#                     exp.document_type_id = int(detalle['document_type'])
#                     exp.status = detalle['status']
#                     exp.file_code = detalle['file_code']
#                     exp.client_code = detalle['client_code']
#                     exp.description = detalle['description']
#                     exp.date_of = detalle['date_of']
#                     exp.date_to = detalle['date_to']
#                     exp.month_of = detalle['month_of']
#                     exp.month_to = detalle['month_to']
#                     exp.year_of = detalle['year_of']
#                     exp.year_to = detalle['year_to']
#                     exp.save()
#
#                     if int(detalle['personal_info']) == 1:
#                         print('Agregar info')
#                         per = Personals()
#                         per.expedient_id = exp.id
#                         per.names = detalle['det_personal_info'][0]['names']
#                         per.surnames = detalle['det_personal_info'][0]['surnames']
#                         per.address = detalle['det_personal_info'][0]['address']
#                         per.phone_number = detalle['det_personal_info'][0]['phone_number']
#                         per.card_id = detalle['det_personal_info'][0]['card_id']
#                         per.save()
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Crear nuevo registro'
#         context['entity'] = 'Expedientes'
#         context['list_url'] = self.success_url
#         context['action'] = 'add'
#         context['personalform'] = PersonalInfoForms
#         # context['rc'] = self.get_rc()
#         return context
#
#
# class ExpedientsUpdateiew(LoginRequiredMixin, UpdateView):
#     model = Expedients
#     form_class = DocumentacionForms
#     template_name = 'expedientsAdministration/create.html'
#     success_url = reverse_lazy('administration:expedients_list')
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
#                 # print(form)
#                 detalle = json.loads(request.POST['vents'])
#
#                 if form.is_valid():
#                     with transaction.atomic():
#                         detalle = json.loads(request.POST['vents'])
#                         id_personal = request.POST['id_personal']
#
#                         exp = self.get_object()
#                         exp.departament_id = int(detalle['departament'])
#                         exp.personal_info = detalle['personal_info']
#                         exp.serial_id = int(detalle['serial'])
#                         exp.sub_serial_id = int(detalle['sub_serial'])
#                         exp.document_type_id = int(detalle['document_type'])
#                         exp.status = detalle['status']
#                         exp.file_code = detalle['file_code']
#                         exp.client_code = detalle['client_code']
#                         exp.description = detalle['description']
#                         exp.date_of = detalle['date_of']
#                         exp.date_to = detalle['date_to']
#                         exp.month_of = detalle['month_of']
#                         exp.month_to = detalle['month_to']
#                         exp.year_of = detalle['year_of']
#                         exp.year_to = detalle['year_to']
#                         exp.save()
#
#                         if int(detalle['personal_info']) == 1:
#                             per = Personals()
#                             # THIS SECTION IS FOR THE MODIFICATIONS PERSONAL INFO
#                             if id_personal != '':
#                                 per.id = int(id_personal)
#                             per.expedient_id = exp.id
#                             per.names = detalle['det_personal_info'][0]['names']
#                             per.surnames = detalle['det_personal_info'][0]['surnames']
#                             per.address = detalle['det_personal_info'][0]['address']
#                             per.phone_number = detalle['det_personal_info'][0]['phone_number']
#                             per.card_id = detalle['det_personal_info'][0]['card_id']
#                             per.save()
#                         elif int(detalle['personal_info']) == 0:
#                             e = Personals.objects.filter(expedient_id=exp.id)
#                             e.delete()
#                 else:
#                     data['error'] = form.errors
#             else:
#                 data['error'] = 'No ha ingresado ninguna opcion'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)
#
#     def get_detail_personal(self):
#         data = []
#         try:
#             for i in Personals.objects.filter(expedient_id=self.get_object().id):
#                 data.append({'id': i.id, 'names': i.names, 'surnames': i.surnames, 'card_id': i.card_id,
#                              'phone_number': i.phone_number, 'address': i.address})
#         except:
#             pass
#         return data
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Modificar Expediente'
#         context['entity'] = 'Expedientes'
#         context['list_url'] = self.success_url
#         context['detail'] = json.dumps(self.get_detail_personal())
#         context['action'] = 'edit'
#         return context
#
#
# class ExpedientsDeleteview(LoginRequiredMixin, DeleteView):
#     model = Expedients
#     form_class = DocumentacionForms
#     template_name = 'expedientsAdministration/delete.html'
#     success_url = reverse_lazy('administration:expedients_list')
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             self.object.delete()
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Eliminar Departamento'
#         context['entity'] = 'Departamentos'
#         context['list_url'] = self.success_url
#         context['action'] = 'delete'
#         return context
