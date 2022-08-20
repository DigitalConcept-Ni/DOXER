from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# from Apps.RRHH.forms import SeccionesForms
# from Apps.RRHH.mixin import IsSuperUserMixin
# from Apps.RRHH.models import Secciones
from Apps.administration.forms import DepartamentoForms
from Apps.administration.models import *


class DepartamentosListView(LoginRequiredMixin, ListView):
    model = Departaments
    template_name = 'departamento/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = []
            action = request.POST['action']
            if action == 'search_data':
                for d in Departaments.objects.all():
                    data.append(d.toJSON())
                # print(data)
            # if action == 'search_history':
            #     data = []
            #     for d in Secciones.objects.filter(pk=request.POST['id']):
            #         data.append(d.toJSON())
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Departamentos Registrados'
        context['create_url'] = reverse_lazy('administration:departamentos_add')
        context['entity'] = 'Departamentos'
        context['list_url'] = reverse_lazy('administration:departamentos_list')
        return context


class DepartamentosCreateview(LoginRequiredMixin, CreateView):
    model = Departaments
    form_class = DepartamentoForms
    template_name = 'departamento/create.html'
    success_url = reverse_lazy('administration:departamentos_list')

    @method_decorator(login_required)
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
                data['error'] = 'No ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear un nuevo departamento'
        context['entity'] = 'Departamentos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class DepartamentosUpdateiew(LoginRequiredMixin, UpdateView):
    model = Departaments
    form_class = DepartamentoForms
    template_name = 'departamento/create.html'
    success_url = reverse_lazy('administration:departamentos_list')

    @method_decorator(login_required)
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
        context['title'] = 'Modificar Departamento'
        context['entity'] = 'Departamentos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class DepartamentosDeleteview(LoginRequiredMixin, DeleteView):
    model = Departaments
    form_class = DepartamentoForms
    template_name = 'departamento/delete.html'
    success_url = reverse_lazy('administration:departamentos_list')

    @method_decorator(login_required)
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
        context['title'] = 'Eliminar Departamento'
        context['entity'] = 'Departamentos'
        context['list_url'] = self.success_url
        context['action'] = 'delete'
        return context
