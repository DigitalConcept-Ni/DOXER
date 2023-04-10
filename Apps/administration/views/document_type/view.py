from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# from Apps.RRHH.mixin import IsSuperUserMixin
from Apps.administration.forms import *
from Apps.administration.models import *


class DocumentTypeListView(LoginRequiredMixin, ListView):
    model = Documents
    template_name = 'documents_type/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = []
            action = request.POST['action']
            if action == 'search_data':
                for d in Documents.objects.all():
                    data.append([d.id, d.name, d.id])
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tipo de Documentos'
        context['create_url'] = reverse_lazy('administration:documents_type_add')
        context['entity'] = 'Tipo de Documentos'
        context['list_url'] = reverse_lazy('administration:documents_type_list')
        return context


class DocumentTypeCreateview(LoginRequiredMixin, CreateView):
    model = Documents
    form_class = DocumentsTypeForms
    template_name = 'documents_type/create.html'
    success_url = reverse_lazy('administration:documents_type_list')

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
        context['title'] = 'Agregar tipo de documento'
        context['entity'] = 'Tipo de Documentos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class DocumentTypeUpdateview(LoginRequiredMixin, UpdateView):
    model = Documents
    form_class = DocumentsTypeForms
    template_name = 'documents_type/create.html'
    success_url = reverse_lazy('administration:documents_type_list')

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
        context['title'] = 'Modificar Tipo de Documento'
        context['entity'] = 'Tipo de Documentos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class DocumentTypeDeleteview(LoginRequiredMixin, DeleteView):
    model = Documents
    form_class = DocumentsTypeForms
    template_name = 'documents_type/delete.html'
    success_url = reverse_lazy('administration:documents_type_list')

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
        context['title'] = 'Eliminar Documento'
        context['entity'] = 'Tipo de Documentos'
        context['list_url'] = self.success_url
        context['action'] = 'delete'
        return context
