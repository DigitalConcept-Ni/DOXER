from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict


# class Branches(models.Model):
#     name = models.CharField(max_length=150, unique=True, verbose_name='Nombre sucursal')
#     code = models.CharField(max_length=4, unique=True, verbose_name='Codigo')
#     responsable = models.CharField(max_length=20, null=True, blank=True)
#     email = models.EmailField(max_length=20, null=True, blank=True)
#     phone_number = models.CharField(max_length=8, null=False, blank=False)
#
#     def __str__(self):
#         return self.name
#
#     def toJSON(self):
#         item = model_to_dict(self)
#         return item
#
#     class Meta:
#         verbose_name = 'Branch'
#         verbose_name_plural = 'Branches'
#         ordering = ['id']


class User(AbstractUser):
    # branch = models.ForeignKey(Branches, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Sucursal')

    def __str__(self):
        return self.username

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'groups', 'user_permissions', 'last_login'])
        # item['branch'] = "" if self.branch is None else self.branch.name
        if self.last_login:
            item['last_login'] = self.last_login.strftime("%Y-%m-%d %H:%M:%S")
        return item
