from datetime import datetime

from django.db import models
from django.forms import model_to_dict

from Apps.user.models import User


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=100, null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Suppliers(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nombre')
    seller = models.CharField(max_length=30, verbose_name='Vendedor')
    address = models.CharField(max_length=150, verbose_name='Direccion')
    email = models.EmailField(max_length=30, verbose_name='Correo')
    phone_number = models.CharField(max_length=8, verbose_name='Numero de telefono')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['id']


class Product(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE, verbose_name='Proveedor')
    name = models.CharField(max_length=150, verbose_name='Nombre')
    brand = models.CharField(max_length=30, verbose_name='Marca')
    # image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    cost = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de compra')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cat'] = self.cat.toJSON()
        # item['image'] = self.get_image()
        item['pvp'] = format(self.pvp, '.2f')
        return item

    # def get_image(self):
    #     if self.image:
    #         return '{}{}'.format(MEDIA_URL, self.image)
    #     return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    email = models.EmailField(max_length=30, verbose_name='Correo')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Cedula')
    phone_number = models.CharField(max_length=8, verbose_name='Numero de telefono')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    gender_choices = (['M', 'MASCULINO'],
                      ['F', 'FEMENINO'])
    gender = models.CharField(max_length=10, choices=gender_choices, default='M', verbose_name='Sexo')

    def __str__(self):
        return self.names

    def toJSON(self):
        item = model_to_dict(self)
        item['gender'] = {'id': self.gender, 'name': self.get_gender_display()}
        # item['date_birthday'] = self.date_birthday.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE,  verbose_name='Cliente')
    user = models.ForeignKey(User, on_delete=models.CASCADE,  verbose_name='Usuario')
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names

    def toJSON(self):
        item = model_to_dict(self)
        item['cli'] = self.cli.toJSON()
        item['subtotal'] = format(self.subtotal, '.2f')
        item['iva'] = format(self.iva, '.2f')
        item['total'] = format(self.total, '.2f')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['det'] = [i.toJSON() for i in self.detsale_set.all()]
        return item

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    def toJSON(self):
        item = model_to_dict(self, exclude=['sale'])
        item['prod'] = self.prod.toJSON()
        item['price'] = format(self.price, '.2f')
        item['subtotal'] = format(self.subtotal, '.2f')
        return item

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']
