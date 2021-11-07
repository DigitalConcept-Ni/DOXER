from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict


class Enterprises(models.Model):
    name = models.CharField(max_length=15, verbose_name='Nombre')
    manager = models.CharField(max_length=15, verbose_name='Gerente')
    address = models.CharField(max_length=15, verbose_name='Direccion')
    phone_number = models.CharField(max_length=15, verbose_name='Telefono')
    email = models.EmailField(max_length=30, verbose_name='Correo')

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['id']


class User(AbstractUser):
    enterprise = models.ForeignKey(Enterprises, on_delete=models.CASCADE, verbose_name='Empresa')

    def __str__(self):
        return self.username

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'groups', 'user_permissions', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime("%Y-%m-%d %H:%M:%S")
        return item