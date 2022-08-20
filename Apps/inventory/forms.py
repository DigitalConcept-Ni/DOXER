from django.forms import *

from Apps.inventory.models import *


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'desc']

class ProductsForm(ModelForm):
    class Meta:
        model = Product
        fields = ['cat', 'supplier', 'name', 'brand', 'cost', 'pvp']

class SuppliersForm(ModelForm):
    class Meta:
        model = Suppliers
        fields = ['name', 'seller', 'email', 'phone_number', 'address']