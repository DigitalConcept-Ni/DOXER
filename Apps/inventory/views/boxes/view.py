from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Apps.inventory.forms import BoxesForms
from Apps.inventory.models import *


class BoxesListView(LoginRequiredMixin, ListView):
    model = Boxes
    template_name = 'boxes/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = []
            action = request.POST['action']
            if action == 'search_data':
                u = request.user.is_superuser
                s = request.user.is_staff
                query = json.loads(request.POST['data'])
                print(query)
                if 'boxNumber' in query:
                    print('buscar por numero de caja')
                    search = Boxes.objects.filter(code__exact=query['boxNumber'])
                    for i in search:
                        data.append([i.id, i.branch.name, i.document.name,
                                     i.code, i.status, i.user.username, i.date_joined, i.status,
                                     i.end_date, i.id])
                if 'boxDate' in query:
                    print('buscar por fecha de la caja')
                    search = Boxes.objects.filter(start_date__exact=query['boxDate'])
                    for i in search:
                        data.append([i.id, i.branch.name, i.document.name,
                                     i.code, i.status, i.user.username, i.date_joined, i.status,
                                     i.end_date, i.id])

                #
            elif action == 'search_expedients':
                data = []
                item = 0
                search = BoxDetailExpedients.objects.filter(box_id=request.POST['boxNumber'])
                for d in search:
                    item += 1
                    data.append([item, d.id, d.box.code, d.names, d.surnames,
                                 d.card_id, d.phone_number, d.address,
                                 d.joined, d.exists, d.id])
            # elif action == 'search_history':
            #     id_box = request.POST['id']
            #     data = [i.toJSON() for i in Box_Detail_Follow.objects.filter(box_id=id_box)]
        except Exception as e:
            # data['error'] = str(e)
            data['error'] = e
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Cajas'
        context['title_query'] = 'Introdusca los datos de la caja que necesita encontrar'
        context['create_expedients'] = reverse_lazy('inventory:boxes_expedients_add')
        context['entity'] = 'Cajas'
        # context['list_url'] = reverse_lazy('inventory:listados_list')
        return context


class BoxesCreateExpedientsView(LoginRequiredMixin, CreateView):
    model = Boxes
    form_class = BoxesForms
    template_name = 'expedients/create.html'
    success_url = reverse_lazy('inventory:boxes_list')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                # print('Entro')
                # print(request.POST)

                with transaction.atomic():
                    detalle = json.loads(request.POST['box'])

                    box = Boxes()
                    box.branch_id = int(detalle['branch'])
                    box.document_id = int(detalle['document'])
                    box.code = detalle['code']
                    box.status = int(detalle['status'])
                    box.user_id = int(detalle['user'])
                    box.date_joined = detalle['date_joined']
                    box.start_date = detalle['start_date']
                    box.end_date = detalle['end_date']
                    box.save()

                    # print(detalle['expedientInfo'])

                    for i in detalle['expedientInfo']:
                        detail = BoxDetailExpedients()
                        detail.box_id = box.id
                        detail.names = i['names']
                        detail.surnames = i['surnames']
                        detail.card_id = i['card_id']
                        detail.address = i['address']
                        detail.phone_number = i['phone_number']
                        detail.exists = i['exists']
                        detail.joined = i['joined']
                        detail.save()
            else:
                data['error'] = 'No ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar detalle de Expedientes de la caja'
        context['entity'] = 'Listado'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['detail'] = []
        return context


class BoxesCreateView(LoginRequiredMixin, CreateView):
    model = Boxes
    form_class = BoxesForms
    template_name = 'boxes/create.html'
    success_url = reverse_lazy('inventory:listados_list')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                with transaction.atomic():
                    detalle = json.loads(request.POST['box'])

                    box = Boxes()
                    box.branch_id = int(detalle['branch'])
                    box.box = detalle['box']
                    box.status = int(detalle['status'])
                    box.user_id = int(detalle['user'])
                    box.date_joined = detalle['date_joined']
                    box.save()

                    print(detalle['credit'])

                    for i in detalle['credit']:
                        detail = Box_detail()
                        detail.box_id = box.id
                        detail.client = i['client']
                        detail.credit = i['credit']
                        detail.canceled_date = i['canceled_date']
                        detail.year = i['year']
                        detail.exists = i['exists']
                        detail.joined = i['joined']
                        detail.save()
            else:
                data['erro'] = 'No ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar detalle de lista'
        context['entity'] = 'Listado'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['detail'] = []
        return context


class BoxesUpdateView(LoginRequiredMixin, UpdateView):
    model = Boxes
    # form_class = BoxesForms
    template_name = 'boxes/create.html'
    success_url = reverse_lazy('inventory:listados_list')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                with transaction.atomic():
                    detalle = json.loads(request.POST['box'])
                    follow = json.loads(request.POST['follow'])

                    box = self.get_object()
                    box.branch_id = int(detalle['branch'])
                    box.box = detalle['box']
                    box.status = int(detalle['status'])
                    box.user_id = int(detalle['user'])
                    box.date_joined = detalle['date_joined']
                    box.save()

                    for i in Box_detail.objects.filter(box_id=box):
                        i.delete()

                    for i in detalle['credit']:
                        detail = Box_detail()
                        detail.box_id = box.id
                        detail.client = i['client']
                        detail.credit = i['credit']
                        detail.canceled_date = i['canceled_date']
                        detail.year = i['year']
                        detail.exists = i['exists']
                        detail.joined = i['joined']
                        detail.save()

                    if follow['add'] >= 1 and follow['del'] >= 1:
                        for i in follow:
                            fw = Box_Detail_Follow()
                            fw.box_id = box.id
                            fw.user_id = int(request.user.id)
                            if i == 'add':
                                fw.comment = '{}, ha ingresado  {} expedientes'.format(request.user.username,
                                                                                       int(follow['add']))
                            elif i == 'del':
                                fw.comment = '{}, ha Eliminado {} expedientes'.format(request.user.username,
                                                                                      int(follow['add']))
                            fw.save()

                            email = SendEmails()
                            email.follow_id = fw.id
                            email.save()
                    else:
                        fw = Box_Detail_Follow()
                        fw.box_id = box.id
                        fw.user_id = int(request.user.id)
                        if int(follow['add']) >= 1 and int(follow['del']) == 0:
                            fw.comment = '{}, ha ingresado  {} expedientes'.format(request.user.username,
                                                                                   int(follow['add']))
                        elif int(follow['add']) == 0 and int(follow['del']) >= 0:
                            fw.comment = '{}, ha Eliminado {} expedientes'.format(request.user.username,
                                                                                  int(follow['del']))
                        fw.save()

                        email = SendEmails()
                        email.follow_id = fw.id
                        email.save()
            else:
                data['error'] = 'No ha ingresado ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_detail_list(self):
        data = []
        try:
            item = 0
            for i in Box_detail.objects.filter(box_id=self.get_object().id):
                item += 1
                data.append(i.toJSON(item))
                # data.append({'id': i.id, 'client': i.client, 'credit': i.credit, 'canceled_date': i.canceled_date.strftime("%Y-%m-%d"),
                #        'year': i.year, 'status': i.status,'update': 'true'})
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modificar Caja y Expedientes'
        context['entity'] = 'Cajas'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['detail'] = json.dumps(self.get_detail_list())
        return context


class BoxesDeleteView(LoginRequiredMixin, DeleteView):
    model = Boxes
    # form_class = BoxesForms
    template_name = 'boxes/delete.html'
    success_url = reverse_lazy('inventory:listados_list')

    @method_decorator(csrf_exempt)
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
        context['title'] = 'Eliminar Caja'
        context['entity'] = 'Cajas'
        context['list_url'] = self.success_url
        context['action'] = 'delete'
        return context
