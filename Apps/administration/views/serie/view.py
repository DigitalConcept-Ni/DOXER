# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import JsonResponse
# from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from django.views.generic import CreateView, UpdateView, DeleteView, ListView
#
# # from Apps.RRHH.mixin import IsSuperUserMixin
# from Apps.administration.forms import *
# from Apps.administration.models import *
#
#
# class SerialsListView(LoginRequiredMixin, ListView):
#     model = Serials
#     template_name = 'serial/list.html'
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
#                 for d in Serials.objects.all():
#                     data.append(d.toJSON())
#                 # print(data)
#             # if action == 'search_history':
#             #     data = []
#             #     for d in Secciones.objects.filter(pk=request.POST['id']):
#             #         data.append(d.toJSON())
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data, safe=False)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Series Documentales'
#         context['create_url'] = reverse_lazy('administration:serials_add')
#         context['entity'] = 'Series'
#         context['list_url'] = reverse_lazy('administration:departamentos_list')
#         return context
#
#
# class SerialsCreateview(LoginRequiredMixin, CreateView):
#     model = Serials
#     form_class = SerialsForms
#     template_name = 'serial/create.html'
#     success_url = reverse_lazy('administration:serials_list')
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'add':
#                 form = self.get_form()
#                 if form.is_valid():
#                     form.save()
#                 else:
#                     data['error'] = form.errors
#             else:
#                 data['error'] = 'Algunos de los datos no son validos'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Crear una nueva serie'
#         context['entity'] = 'Series'
#         context['list_url'] = self.success_url
#         context['action'] = 'add'
#         return context
#
#
# class SerialUpdateiew(LoginRequiredMixin, UpdateView):
#     model = Serials
#     form_class = SerialsForms
#     template_name = 'serial/create.html'
#     success_url = reverse_lazy('administration:serials_list')
#
#     @method_decorator(login_required)
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
#                     form.save()
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
#         context['title'] = 'Modificar Serie'
#         context['entity'] = 'Series'
#         context['list_url'] = self.success_url
#         context['action'] = 'edit'
#         return context
#
#
# class SerialsDeleteview(LoginRequiredMixin, DeleteView):
#     model = Serials
#     form_class = SerialsForms
#     template_name = 'serial/delete.html'
#     success_url = reverse_lazy('administration:serials_list')
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
#         context['title'] = 'Eliminar serie documenta'
#         context['entity'] = 'Serie'
#         context['list_url'] = self.success_url
#         context['action'] = 'delete'
#         return context