import json

from django.db import models
from datetime import datetime

from django.forms import model_to_dict

# from config.settings import MEDIA_URL, STATIC_URL
from Apps.administration.generic import lista_personals
from Apps.administration.models import Documents, Branches
from Apps.user.models import *


class Boxes(models.Model):
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE, verbose_name='Sucursal')
    document = models.ForeignKey(Documents, on_delete=models.CASCADE)
    # personal_info = models.IntegerField(choices=lista_personals, default=0)
    code = models.CharField(max_length=10, unique=True, verbose_name='Caja')
    status = models.CharField(max_length=1, verbose_name='Estado')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    # DATES
    date_joined = models.DateField(format("YYYY-MM-DD"), default=datetime.now)
    start_date = models.DateField(format("YYYY-MM-DD"), default=datetime.now)
    end_date = models.DateField(format("YYYY-MM-DD"), default=datetime.now)

    def __str__(self):
        return self.branch.name + self.code

    def quantity_of_items(self):
        item = len([i for i in BoxDetailExpedients.objects.filter(box_id=self.id)])
        return item

    def toJSON(self, user, staff):
        item = model_to_dict(self)
        item['branch_name'] = self.branch.name
        item['date_joined'] = self.date_joined.strftime("%Y-%m-%d")
        item['items'] = self.quantity_of_items()
        item['user'] = self.user.username
        item['is_superuser'] = user
        item['is_staff'] = staff
        return item

    class Meta:
        verbose_name = 'Box'
        verbose_name_plural = 'Boxes'
        ordering = ['date_joined']


# REFERENCES OF PERSONALS EXPEDIENTS FOR THE BOX
class BoxDetailExpedients(models.Model):
    box = models.ForeignKey(Boxes, on_delete=models.CASCADE)
    names = models.CharField(max_length=30)
    surnames = models.CharField(max_length=30)
    card_id = models.CharField(max_length=14)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=8)
    # PART OF VALIDATION THE DOCUMENT
    exists = models.CharField(max_length=1, verbose_name='Existencia')
    joined = models.CharField(max_length=1, verbose_name='Agregado')

    # file = models.FileField(upload_to='administrativos/%Y/%m/%d', null=True, blank=True)f)

    def __str__(self):
        return '{} -- {}'.format(self.names, self.surnames)

    # def toLIST(self):
    #     item = [self.id, self.departament.name, self.serial.name, self.document_type.name, self.status,
    #             self.file_code, self.client_code, self.id, self.personal_info]
    #     return item

    def toJSON(self):
        item = model_to_dict(self)
        # item['date_of'] = self.date_of.strftime("%Y-%m-%d")
        # item['date_of'] = self.date_of
        return item

    class Meta:
        verbose_name = 'Expedient'
        verbose_name_plural = 'Expedients'
        ordering = ("id",)


# REFERENCES OF DOCUMENTS FOR THE BOX
class BoxDetailDocuments(models.Model):
    box = models.ForeignKey(Boxes, on_delete=models.CASCADE)
    document = models.ForeignKey(Documents, on_delete=models.CASCADE)
    client = models.CharField(max_length=30, verbose_name='Cliente')
    code = models.CharField(max_length=10, verbose_name='Codigo')
    date = models.DateField(default=datetime.now, verbose_name='Fecha Documento')
    # PART OF VALIDATION THE DOCUMENT
    exists = models.CharField(max_length=1, verbose_name='Existencia')
    joined = models.CharField(max_length=1, verbose_name='Agregado')

    # def __str__(self):
    #     return self.cliente

    def toJSON(self, it):
        item = model_to_dict(self)
        item['branch_name'] = self.box.branch.name
        item['branch_code'] = self.box.branch.code
        item['exists'] = int(self.exists)
        item['joined'] = int(self.joined)
        item['item'] = it
        # item['canceled_date'] = self.canceled_date.strftime("%Y-%m-%d")
        return item

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ['id']


# DETAIL FOR THE FILES OF THE EXPEDIENTS
class BoxDetailFileExpedients(models.Model):
    expedient = models.ForeignKey(BoxDetailExpedients, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # date change notification
    date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Fecha de subida')
    # FILES
    file = models.FileField(upload_to='expedientsAdministration/%Y/%m/%d', null=True, blank=True)

    def toJSON(self):
        item = model_to_dict(self)
        item['user'] = self.user.username
        item['box_number'] = self.expedient.box.code
        item['branch_name'] = self.expedient.box.branch.name
        item['date'] = self.date.strftime("%Y-%m-%d -- %H:%M:%S")
        return item

    class Meta:
        verbose_name = 'Box_Details_File'
        verbose_name_plural = 'Box_Detail_Files'
        ordering = ['date']


# DETAIL FOR THE FILES OF THE DOCUMENTS
class BoxDetailFileDocuments(models.Model):
    document = models.ForeignKey(BoxDetailDocuments, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # date change notification
    date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Fecha de subida')
    # FILES
    file = models.FileField(upload_to='documents/%Y/%m/%d', null=True, blank=True)

    def toJSON(self):
        item = model_to_dict(self)
        item['user'] = self.user.username
        item['box_number'] = self.document.box.code
        item['branch_name'] = self.document.box.branch.name
        item['date'] = self.date.strftime("%Y-%m-%d -- %H:%M:%S")
        return item

    class Meta:
        verbose_name = 'Box_Details_File'
        verbose_name_plural = 'Box_Detail_Files'
        ordering = ['date']


class BoxDetailFollow(models.Model):
    box = models.ForeignKey(Boxes, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Fecha de cambio')
    comment = models.CharField(max_length=300, null=True, blank=True, verbose_name='Comentario')

    def toJSON(self):
        item = model_to_dict(self)
        item['user'] = self.user.username
        item['box_number'] = self.box.code
        item['branch_name'] = self.box.branch.name
        item['date'] = self.date.strftime("%Y-%m-%d -- %H:%M:%S")
        return item

    class Meta:
        verbose_name = 'Box_Details_Follows'
        verbose_name_plural = 'Box_Detail_Follow'
        ordering = ['date']


class SendEmails(models.Model):
    follow = models.ForeignKey(BoxDetailFollow, on_delete=models.CASCADE)
    send = models.CharField(max_length=1, default=0, verbose_name='Enviado')

    def toJSON(self):
        item = model_to_dict(self)
        item['follow'] = self.follow.toJSON()
        return item

    class Meta:
        verbose_name = 'SendEmail'
        verbose_name_plural = 'SendEmails'
        ordering = ['send']
