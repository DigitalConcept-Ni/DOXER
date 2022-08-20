# from django.shortcuts import render
# import json
#
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.db import transaction
# from django.http import JsonResponse
# from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#
# # Create your views here.
# from django.urls import reverse_lazy
#
# # from Apps.RRHH.mixin import IsSuperUserMixin
# from Apps.administration.forms import PlantillasForms
# from Apps.administration.models import *
#
#
# class PlantillasListView(LoginRequiredMixin, ListView):
#     model = Templates
#     template_name = 'plantillas/list.html'
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
#             if action == 'search_data':
#                 for d in Templates.objects.all():
#                     data.append(d.toJSON())
#                 # print(data)
#             if action == 'search_history':
#                 data = []
#                 for d in Fields.objects.filter(template_id=request.POST['id']):
#                     data.append(d.toJSON())
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data, safe=False)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Plantillas Registradas'
#         context['create_url'] = reverse_lazy('administration:plantilla_create')
#         context['entity'] = 'Departamentos'
#         context['list_url'] = reverse_lazy('administration:plantilla_list')
#         return context
#
# class PlantillasCreateView(CreateView):
#     model = Templates
#     form_class = PlantillasForms
#     template_name = 'plantillas/create.html'
#     success_url = reverse_lazy('administration:plantilla_list')
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'add':
#                 # print(request.POST)
#                 with transaction.atomic():
#                     detalle = json.loads(request.POST['vents'])
#
#                     tem = Templates()
#                     tem.template_name = detalle['template_name']
#                     tem.departament_id = int(detalle['departament'])
#                     tem.save()
#
#                     for i in detalle['campos']:
#                         # print(i)
#                         campo = Fields()
#                         campo.template_id = tem.id
#                         campo.field_name = i['field_name']
#                         campo.data_type = i['data_type']
#                         campo.save()
#             else:
#                 data['erro'] = 'No ha ingresado ninguna opcion'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Agregar plantilla'
#         context['entity'] = 'Plantillas'
#         context['list_url'] = self.success_url
#         context['action'] = 'add'
#         # context['detail'] = []
#         # context['Cform'] = CamposForms() # Formulario de los campos
#         return context
#
# class PlantillasupdateView(UpdateView):
#     model = Templates
#     form_class = PlantillasForms
#     template_name = 'plantillas/create.html'
#     success_url = reverse_lazy('administration:plantilla_list')
#
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
#                 with transaction.atomic():
#                     detalle = json.loads(request.POST['vents'])
#                     # print(request.POST)
#
#                     tem = self.get_object()
#                     tem.template_name = detalle['template_name']
#                     tem.departament_id = int(detalle['departament'])
#                     tem.save()
#
#                     for i in Fields.objects.filter(template_id=tem):
#                         i.delete()
#
#                     for i in detalle['campos']:
#                         campo = Fields()
#                         campo.template_id = tem.id
#                         campo.field_name = i['field_name']
#                         campo.data_type = i['data_type']
#                         campo.save()
#             else:
#                 data['error'] = 'No ha ingresado ninguna opcion'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)
#
#     def get_detail_list(self):
#         data = []
#         try:
#             for i in Fields.objects.filter(template_id=self.get_object().id):
#                 data.append(i.toJSON())
#             print(data)
#         except:
#             pass
#         return data
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Modificacion de plantilla'
#         context['entity'] = 'Plantillas'
#         context['list_url'] = self.success_url
#         context['action'] = 'edit'
#         context['detail'] = json.dumps(self.get_detail_list())
#         return context
#
# class PlantillasDeleteView(DeleteView):
#     model = Templates
#     form_class = PlantillasForms
#     template_name = 'plantillas/delete.html'
#     success_url = reverse_lazy('administration:plantilla_list')
#
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
#         context['title'] = 'Eliminar Plantilla'
#         context['entity'] = 'PLantillas'
#         context['list_url'] = self.success_url
#         context['action'] = 'delete'
#         return context
