from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# from Aplicaciones.RRHH.mixin import IsSuperUserMixin
from Apps.administration.forms import *
from Apps.administration.models import *


class SubSerialsListView(LoginRequiredMixin, ListView):
    model = Sub_serial
    template_name = 'sub_serial/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = []
            action = request.POST['action']
            if action == 'search_data':
                for d in Sub_serial.objects.all():
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
        context['title'] = 'Sub Series Documentales'
        context['create_url'] = reverse_lazy('administration:sub_serials_add')
        context['entity'] = 'Sub Series'
        context['list_url'] = reverse_lazy('administration:sub_serials_list')
        return context


class SubSerialsCreateview(LoginRequiredMixin, CreateView):
    model = Serials
    form_class = SubSerialsForms
    template_name = 'sub_serial/create.html'
    success_url = reverse_lazy('administration:sub_serials_list')

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
                data['error'] = 'Algunos de los datos no son validos'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear una nueva sub serie'
        context['entity'] = 'Sub Series'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class SubSerialsUpdateiew(LoginRequiredMixin, UpdateView):
    model = Sub_serial
    form_class = SubSerialsForms
    template_name = 'sub_serial/create.html'
    success_url = reverse_lazy('administration:sub_serials_list')

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
                data['error'] = 'Algunos valores no son validos'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modificar SUb Serie'
        context['entity'] = 'Sub Serie'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class SubSerialsDeleteview(LoginRequiredMixin, DeleteView):
    model = Sub_serial
    form_class = SubSerialsForms
    template_name = 'sub_serial/delete.html'
    success_url = reverse_lazy('administration:sub_serials_list')

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
        context['title'] = 'Eliminar Sub Serie Documental'
        context['entity'] = 'Sub Serie'
        context['list_url'] = self.success_url
        context['action'] = 'delete'
        return context