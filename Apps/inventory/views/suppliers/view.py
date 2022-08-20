from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView

from Apps.inventory.forms import SuppliersForm
from Apps.inventory.models import Suppliers

list_url = reverse_lazy('inventory:supplier_list')
create_url = reverse_lazy('inventory:supplier_create')
entity = 'Productos'

class SuppliersListview(LoginRequiredMixin, TemplateView):
    template_name = 'supplier/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_supplier':
                data = []
                for e in Suppliers.objects.all():
                    data.append([e.id, e.name, e.seller, e.address, e.email,
                                 e.phone_number, e.id])
        except Exception as e:
            print(e)
            data['error'] = 'Ha ocurrido un error, verificar datos'
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Proveedores Registrados'
        context['create_url'] = create_url
        context['entity'] = 'proveedores'
        context['list_url'] = list_url
        return context


class SuppliersCreateview(LoginRequiredMixin, CreateView):
    model = Suppliers
    form_class = SuppliersForm
    template_name = 'supplier/create.html'
    success_url = list_url
    url_redirect = success_url

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                form.save()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            print(e)
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Proveedor'
        context['entity'] = entity
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


# class CategoryUpdateview(LoginRequiredMixin, UpdateView):
#     model = Category
#     form_class = CategoryForm
#     template_name = 'category/create.html'
#     success_url = list_url
#     url_redirect = success_url
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
#                 form.save()
#             else:
#                 data['error'] = 'No ha ingresado ninguna opcion'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Editar Categoria'
#         context['entity'] = entity
#         context['action'] = 'edit'
#         context['list_url'] = self.success_url
#         return context
#
#
# class CategoryDeleteView(LoginRequiredMixin, DeleteView):
#     model = Category
#     template_name = 'category/delete.html'
#     success_url = list_url
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
#         context['title'] = 'Eliminar categoria'
#         context['entity'] = entity
#         context['list_url'] = self.success_url
#         return context