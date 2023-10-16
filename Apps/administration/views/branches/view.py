from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Apps.administration.forms import BranchesForms
from Apps.inventory.models import Branches


class SucursalesListView(LoginRequiredMixin, ListView):
    model = Branches
    template_name = 'branches/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = []
            action = request.POST['action']
            if action == 'search_data':
                for i in Branches.objects.all():
                    data.append([i.id, i.name, i.code, i.responsable, i.email, i.phone_number, i.id])
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Sucursales'
        context['create_url'] = reverse_lazy('administration:sucursal_add')
        context['entity'] = 'Sucursales'
        context['list_url'] = reverse_lazy('administration:sucursal_list')
        return context


class SucursalesCreateView(LoginRequiredMixin, CreateView):
    model = Branches
    form_class = BranchesForms
    template_name = 'branches/create.html'
    success_url = reverse_lazy('administration:sucursal_list')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'Hay errores de validacion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar sucursal'
        context['entity'] = 'Sucursales'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class SucursalesupdateView(LoginRequiredMixin, UpdateView):
    model = Branches
    form_class = BranchesForms
    template_name = 'branches/create.html'
    success_url = reverse_lazy('administration:sucursal_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modificar sucursal'
        context['entity'] = 'Sucursales'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class SucursalesDeleteView(LoginRequiredMixin, DeleteView):
    model = Branches
    form_class = BranchesForms
    template_name = 'branches/delete.html'
    success_url = reverse_lazy('inventory:sucursal_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar sucursal'
        context['entity'] = 'Sucursales'
        context['list_url'] = self.success_url
        context['action'] = 'delete'
        return context
