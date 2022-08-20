from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from Apps.user.forms import EnterpriseForm
from Apps.user.models import Enterprises


class EnterpriseListview(LoginRequiredMixin, TemplateView):
    template_name = 'enterprises/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_enterprise':
                data = []
                for e in Enterprises.objects.all():
                    data.append([e.id, e.name, e.manager, e.address, e.phone_number,
                                 e.email, e.id])
        except Exception as e:
            print(e)
            data['error'] = 'Ha ocurrido un error, verificar datos'
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Empresas registradas'
        context['create_url'] = reverse_lazy('panel:enterprise_create')
        context['entity'] = 'Usuarios'
        context['list_url'] = reverse_lazy('panel:enterprise_list')
        return context


class EnterpriseCreateview(LoginRequiredMixin, CreateView):
    model = Enterprises
    form_class = EnterpriseForm
    template_name = 'enterprises/create.html'
    success_url = reverse_lazy('panel:enterprise_list')
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
        context['title'] = 'Agregar empresa'
        context['entity'] = 'Empresas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class EnterpriseUpdateview(LoginRequiredMixin, UpdateView):
    model = Enterprises
    form_class = EnterpriseForm
    template_name = 'enterprises/create.html'
    success_url = reverse_lazy('panel:enterprise_list')
    url_redirect = success_url

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
                form.save()
            else:
                data['error'] = 'No ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Empresa'
        context['entity'] = 'Empresas'
        context['action'] = 'edit'
        context['list_url'] = self.success_url
        return context


class EnterpriseDeleteView(LoginRequiredMixin, DeleteView):
    model = Enterprises
    template_name = 'enterprises/delete.html'
    success_url = reverse_lazy('panel:enterprise_list')

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
        context['title'] = 'Eliminar empresa'
        context['entity'] = 'Empresas'
        context['list_url'] = self.success_url
        return context