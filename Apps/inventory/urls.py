from Apps.inventory.views.boxes.view import *
from django.urls import path

app_name = 'inventory'
urlpatterns = [
    # urls Sucursales
    # path('list/', oneView, name='listas_list'),

    # urls inventory
    path('boxes/list/', BoxesListView.as_view(), name='boxes_list'),
    path('boxes/expedients/add/', BoxesCreateExpedientsView.as_view(), name='boxes_expedients_add'),
    # path('listado/edit/<int:pk>/', BoxesUpdateView.as_view(), name='listados_edit'),
    # path('listado/delete/<int:pk>/', BoxesDeleteView.as_view(), name='listados_delete'),

]
