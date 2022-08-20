from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# from Aplicaciones.RRHH.mixin import IsSuperUserMixin
from Apps.administration.forms import DocumentsForms
from Apps.administration.models import *
from Apps.administration.remove import removeFIles


class DocumentsListView(LoginRequiredMixin, ListView):
    model = Documents
    template_name = 'documents/list.html'

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
                    data.append(d.toJSON())
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Documentos'
        context['create_url'] = reverse_lazy('administration:documentos_add')
        context['entity'] = 'Documentos'
        context['list_url'] = reverse_lazy('administration:documentos_list')
        return context


class DocumentsCreateview(LoginRequiredMixin, CreateView):
    model = Documents
    form_class = DocumentsForms
    template_name = 'documents/create.html'
    success_url = reverse_lazy('administration:documentos_list')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # print('request',request.POST)
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                # print(request.POST['ve nts'])
                if form.is_valid():
                    with transaction.atomic():
                        detalle = json.loads(request.POST['vents'])
                        file = request.FILES
                        print(detalle)
                        print(file)
                        if 'file' in file:
                            file = request.FILES['file']
                        else:
                            file = None

                        exp = Documents()
                        exp.expedients_id = int(detalle['expedients'])
                        exp.document_type_id = int(detalle['document_type'])
                        exp.date = detalle['date']
                        exp.file = file
                        exp.save()
                else:
                    data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear nuevo registro'
        context['entity'] = 'Documentos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['detail'] = []
        return context


class DocumentsUpdateiew(LoginRequiredMixin, UpdateView):
    model = Documents
    form_class = DocumentsForms
    template_name = 'documents/create.html'
    success_url = reverse_lazy('administration:documentos_list')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
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
                    with transaction.atomic():
                        detalle = json.loads(request.POST['vents'])
                        file = request.FILES

                        if 'file' in file:
                            file = request.FILES['file']
                        elif detalle['file'] != '':
                            if 'file-clear' in request.POST:
                                removeFIles(detalle['file'])
                                file = None
                            else:
                                file = detalle['file']
                        else:
                            file = None

                        exp = self.get_object()
                        exp.expedients_id = int(detalle['expedients'])
                        exp.document_type_id = int(detalle['document_type'])
                        exp.date = detalle['date']
                        exp.file = file
                        exp.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modificar Documento'
        context['entity'] = 'Documentos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class DocumentsDeleteview(LoginRequiredMixin, DeleteView):
    model = Documents
    form_class = DocumentsForms
    template_name = 'documents/delete.html'
    success_url = reverse_lazy('administration:documentos_list')

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
        context['title'] = 'Eliminar Documentos'
        context['entity'] = 'Documentos'
        context['list_url'] = self.success_url
        context['action'] = 'delete'
        return context
