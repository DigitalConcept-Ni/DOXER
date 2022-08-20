from django.urls import path

from Apps.inventory.views.products.view import *
from Apps.inventory.views.category.view import *
from Apps.inventory.views.suppliers.view import *

app_name = 'inventory'

urlpatterns = [
    # urls Category
    path('category/list/', CategoryListview.as_view(), name='category_list'),
    path('category/create/', CategoryCreateview.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateview.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    # url suppliers
    path('proveedores/list/', SuppliersListview.as_view(), name='supplier_list'),
    path('proveedores/create/', SuppliersCreateview.as_view(), name='supplier_create'),

    # urls Products
    path('product/list/', ProductsListview.as_view(), name='products_list'),
    path('product/create/', ProductsCreateview.as_view(), name='products_create'),

]
