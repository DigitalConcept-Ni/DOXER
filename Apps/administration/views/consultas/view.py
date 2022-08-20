from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from django.db.models.functions import Coalesce
from django.db.models import Sum

# from Aplicaciones.administracion.forms import ConsultaForm
# from Aplicaciones.administracion.models import *


class ConsultasAdministrativaView(TemplateView):
    template_name = 'consulta/consulta.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            # REPORTES POR FECHAS 'DESDE'
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Expedients.objects.all()
                # print(request.POST)
                if len(start_date) and len(end_date):
                    search = search.filter(date_of__range=[start_date, end_date])
                for s in search:
                    # print(s.toJSON())
                    data.append([
                        s.id,
                        s.departament.name,
                        s.serial.name,
                        s.sub_serial.name,
                        s.document_type.name,
                        s.status,
                        s.codigo_archivo,
                        s.codigo_cliente,
                        str(s.file),
                    ]) # #
            # REPORTES POR DEPARTAMENTO
            elif action == 'search_departament':
                data = []
                # print(request.POST)
                for s in Expedients.objects.filter(departament_id=request.POST['id_departament']):
                    # print(s.toJSON())
                    data.append([
                        s.id,
                        s.departament.name,
                        s.serial.name,
                        s.sub_serial.name,
                        s.document_type.name,
                        s.status,
                        s.codigo_archivo,
                        s.codigo_cliente,
                        str(s.file),
                    ])
            # REPORTE POR TIPO DE DOCUMENTO
            elif action == 'search_document':
                data = []
                # print(request.POST)
                for s in Expedients.objects.filter(document_type_id=request.POST['id_departament']):
                    # print(s.toJSON())
                    data.append([
                        s.id,
                        s.departament.name,
                        s.serial.name,
                        s.sub_serial.name,
                        s.document_type.name,
                        s.status,
                        s.codigo_archivo,
                        s.codigo_cliente,
                        str(s.file),
                    ])
            # INFORMACION ADICIONAL MODAL (INFORMACION PERIODICA
            elif action == 'search_dates':
                data = []
                for s in Expedients.objects.filter(pk=request.POST['id']):
                    # print(s.toJSON())
                    data.append([
                        s.id,
                        s.date_of,
                        s.date_to,
                        s.month_of,
                        s.month_to,
                        s.year_of,
                        s.year_to,
                    ])
            # INFORMACION ADICIONAL MODAL (INFORMACION DE LOS TEMPLATES)
            elif action == 'search_modal':
                data = []
                search = Detail_Field.objects.all()
                search = search.filter(expedients_id=request.POST['id'])
                for i in search:
                    data.append([
                        i.field.field_name,
                        i.detail,
                    ])
            # INFORMACION DE DOCUMENTOS EN ESE EXPEDIENTE
            elif action == 'search_document_in':
                data = []
                for s in Documents.objects.filter(expedients_id=request.POST['id']):
                    print(s.file)
                    data.append([
                        s.id,
                        s.expedients.codigo_cliente,
                        s.document_type.name,
                        s.date_of,
                        s.date_to,
                        s.month_of,
                        s.month_to,
                        s.year_of,
                        s.year_to,
                        str(s.file),
                    ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consultas'
        context['entity'] = 'Consultas'
        # context['list_url'] = reverse_lazy('sale_report')
        context['form'] = ConsultaForm()
        return context