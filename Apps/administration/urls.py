from django.urls import path

from Apps.administration.views.branches.view import *
from Apps.administration.views.consultas.view import ConsultasAdministrativaView
from Apps.administration.views.document_type.view import *

app_name = 'administration'

urlpatterns = [
    # Urls serie documental
    # path('serials/list/', SerialsListView.as_view(), name='serials_list'),
    # path('serials/add/', SerialsCreateview.as_view(), name='serials_add'),
    # path('serials/edit/<int:pk>/', SerialUpdateiew.as_view(), name='serials_edit'),
    # path('serials/delete/<int:pk>/', SerialsDeleteview.as_view(), name='serials_delete'),
    #
    # # Urls Sub series documentales
    # path('subserie/list/', SubSerialsListView.as_view(), name='sub_serials_list'),
    # path('subserie/add/', SubSerialsCreateview.as_view(), name='sub_serials_add'),
    # path('subserie/edit/<int:pk>/', SubSerialsUpdateiew.as_view(), name='sub_serials_edit'),
    # path('subserie/delete/<int:pk>/', SubSerialsDeleteview.as_view(), name='sub_serials_delete'),
    #
    # # Urls Tipos de documentos
    path('documentType/list/', DocumentTypeListView.as_view(), name='documents_type_list'),
    path('documentType/add/', DocumentTypeCreateview.as_view(), name='documents_type_add'),
    path('document-type/edit/<int:pk>/', DocumentTypeUpdateview.as_view(), name='documents_type_edit'),
    path('document-type/delete/<int:pk>/', DocumentTypeDeleteview.as_view(), name='documents_type_delete'),

    # URLS BRANCHES
    path('branches/list/', SucursalesListView.as_view(), name='sucursal_list'),
    path('branches/add/', SucursalesCreateView.as_view(), name='sucursal_add'),
    path('branches/edit/<int:pk>/', SucursalesupdateView.as_view(), name='sucursal_edit'),
    path('branches/delete/<int:pk>/', SucursalesDeleteView.as_view(), name='sucursal_delete'),

    # Urls de las plantillas
    # path('plantillas/list/', PlantillasListView.as_view(), name='plantilla_list'),
    # path('plantillas/add/', PlantillasCreateView.as_view(), name='plantilla_create'),
    # path('plantillas/edit/<int:pk>/', PlantillasupdateView.as_view(), name='plantilla_edit'),
    # path('plantillas/delete/<int:pk>/', PlantillasDeleteView.as_view(), name='plantilla_delete'),

    # Urls de los departamentos
    # path('departamentos/list/', DepartamentosListView.as_view(), name='departamentos_list'),
    # path('departamentos/add/', DepartamentosCreateview.as_view(), name='departamentos_add'),
    # path('departamentos/edit/<int:pk>/', DepartamentosUpdateiew.as_view(), name='departamentos_edit'),
    # path('departamentos/delete/<int:pk>/', DepartamentosDeleteview.as_view(), name='departamentos_delete'),
    #
    # # Urls de las documentacions (expedientes areas administrativas)
    # path('expedientes/list/', ExpedientsListView.as_view(), name='expedients_list'),
    # path('expedientes/add/', ExpedientsCreateview.as_view(), name='expedients_add'),
    # path('personal/', personal, name='expedients_add_personal'),
    # path('expedientes/edit/<int:pk>/', ExpedientsUpdateiew.as_view(), name='expedients_edit'),
    # path('expedientes/delete/<int:pk>/', ExpedientsDeleteview.as_view(), name='expedients_delete'),

    # urls de los documentos
    # path('documentos/list/', DocumentsListView.as_view(), name='documentos_list'),
    # path('documentos/add/', DocumentsCreateview.as_view(), name='documentos_add'),
    # path('documentos/edit/<int:pk>/', DocumentsUpdateiew.as_view(), name='documentos_edit'),
    # path('documentos/delete/<int:pk>/', DocumentsDeleteview.as_view(), name='documentos_delete'),

    # Url consulta administrativa
    # path('consultas/', ConsultasAdministrativaView.as_view(), name='consulta_administrativa'),

]
