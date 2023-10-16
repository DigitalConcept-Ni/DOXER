# from crum import get_current_user
from django.db import models

# Create your models here.
from django.forms import model_to_dict
from Apps.administration.generic import *
from config import settings


# class Serials(models.Model):
#     name = models.CharField(max_length=50, unique=True, verbose_name='Serie Documental')
#
#     def __str__(self):
#         return self.name
#
#     def toJSON(self):
#         item = model_to_dict(self)
#         return item
#
#     class Meta:
#         verbose_name = 'Serial'
#         verbose_name_plural = 'Serials'
#         ordering = ("id",)
#
#
# class Sub_serial(models.Model):
#     serial = models.ForeignKey(Serials, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50, unique=True, verbose_name='Sub serie documental')
#
#     def __str__(self):
#         return self.name
#
#     def toJSON(self):
#         item = model_to_dict(self)
#         item['serial'] = self.serial.toJSON()
#         return item
#
#     class Meta:
#         verbose_name = 'Sub_serial'
#         verbose_name_plural = 'Sub_serials'
#         ordering = ("id",)
#
#
# class Document_type(models.Model):
#     sub_serial = models.ForeignKey(Sub_serial, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50, unique=True, verbose_name='Tipo Documento')
#
#     def __str__(self):
#         return self.name
#
#     def toJSON(self):
#         item = model_to_dict(self)
#         item['sub_serial'] = self.sub_serial.toJSON()
#         return item
#
#     class Meta:
#         verbose_name = 'Document_type'
#         verbose_name_plural = 'Documents_types'
#         ordering = ("id",)

# class Departaments(models.Model):
#     name = models.CharField(max_length=20)
#     responsable = models.CharField(max_length=20, null=True, blank=True)
#     email = models.EmailField(max_length=20, null=True, blank=True)
#     phone_number = models.CharField(max_length=8, null=False, blank=False)
#
#     def __str__(self):
#         return self.name
#
#     def toList(self):
#         item = [self.id, self.name, self.responsable, self.email, self.phone_number]
#         return item
#
#     def toJSON(self):
#         item = model_to_dict(self)
#         return item
#
#     class Meta:
#         verbose_name = 'Departament'
#         verbose_name_plural = 'Departaments'
#         ordering = ("id",)
#
#
# class Expedients(models.Model):
#     departament = models.ForeignKey(Departaments, on_delete=models.CASCADE)
#     personal_info = models.IntegerField(choices=lista_personals, default=0)
#     serial = models.ForeignKey(Serials, on_delete=models.CASCADE)
#     sub_serial = models.ForeignKey(Sub_serial, on_delete=models.CASCADE)
#     document_type = models.ForeignKey(Document_type, on_delete=models.CASCADE)
#     # template = models.ForeignKey(Template s, on_delete=models.CASCADE, null=True, blank=True)
#     status = models.CharField(max_length=10, choices=lista_resguardo, default='AREA')  # Donde se encuentra resguardado
#     file_code = models.CharField(max_length=10)  # codigo archivo
#     client_code = models.CharField(max_length=10)  # codigo cliente
#     description = models.CharField(max_length=50, null=True, blank=True)
#     # INFORMACION PERIODICA
#     date_of = models.DateField(format("YYYY-MM-DD"), null=True, blank=True)  # Fecha de
#     date_to = models.DateField(format("YYYY-MM-DD"), null=True, blank=True)  # Fecha hasta
#     month_of = models.CharField(max_length=10, choices=lista_meses, default='ENERO')
#     month_to = models.CharField(max_length=10, choices=lista_meses, default='ENERO')
#     year_of = models.CharField(max_length=4)
#     year_to = models.CharField(max_length=4)
#     file = models.FileField(upload_to='administrativos/%Y/%m/%d', null=True, blank=True)
#
#     # rc = models.CharField(max_length=10)
#
#     def __str__(self):
#         return '{} -- {} -- {}'.format(self.file_code, self.client_code, self.document_type)
#
#     def get_archivo(self):
#         if self.file:
#             return '{}{}'.format(settings.MEDIA_URL, self.file)
#         return 'No insertado'
#
#     def toLIST(self):
#         item = [self.id, self.departament.name, self.serial.name, self.document_type.name, self.status,
#                 self.file_code, self.client_code, self.id, self.personal_info]
#         return item
#
#     def toJSON(self):
#         item = model_to_dict(self)
#         item['departament_name'] = self.departament.name
#         item['serial'] = self.serial.toJSON()
#         item['sub_serial'] = self.sub_serial.toJSON()
#         item['document_type'] = self.document_type.toJSON()
#         item['file'] = self.get_archivo()
#         if self.date_of:
#             item['date_of'] = self.date_of.strftime("%Y-%m-%d")
#         if self.date_to:
#             item['date_to'] = self.date_to.strftime("%Y-%m-%d")
#         # item['date_of'] = self.date_of
#         return item
#
#     class Meta:
#         verbose_name = 'Expedient'
#         verbose_name_plural = 'Expedients'
#         ordering = ("id",)
#
#
# class Personals(models.Model):
#     expedient = models.ForeignKey(Expedients, on_delete=models.CASCADE)
#     names = models.CharField(max_length=30)
#     surnames = models.CharField(max_length=30)
#     card_id = models.CharField(max_length=16)
#     address = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=8)
#
#     # file = models.FileField(upload_to='administrativos/%Y/%m/%d', null=True, blank=True)
#
#     def __str__(self):
#         return '{} {}'.format(self.names, self.surnames)
#
#     def toJSON(self):
#         item = model_to_dict(self)
#         return item
#
#     class Meta:
#         verbose_name = 'Personal'
#         verbose_name_plural = 'Personals'
#         ordering = ("id",)
# class Documents(models.Model):
#     expedientsAdministration = models.ForeignKey(Expedients, on_delete=models.CASCADE)
#     name = models.ForeignKey(Document_type, on_delete=models.CASCADE)
#     date = models.DateField(format("YYYY-MM-DD"), null=True, blank=True)  # Date of document
#     # ARCHIVOS
#     file = models.FileField(upload_to='administrativos/%Y/%m/%d', null=True, blank=True)
#
#     def __str__(self):
#         return '{}'.format(self.expedientsAdministration)
#
#     def get_archivo(self):
#         if self.file:
#             return '{}'.format(self.file)
#         return 'No insertado'
#
#     def toList(self):
#         item = [self.id, self.expedients_id, self.document_type.name, self.date, self.file, self.expedientsAdministration.file_code,
#                 self.expedientsAdministration.client_code]
#         return item
#
#     def toJSON(self):
#         item = model_to_dict(self)
#         item['file_code'] = self.expedientsAdministration.file_code
#         item['client_code'] = self.expedientsAdministration.client_code
#         item['document_type'] = self.document_type.name
#         if self.date:
#             item['date'] = self.date.strftime("%Y-%m-%d")
#         # if self.date_to:
#         #     item['date_to'] = self.date_to.strftime("%Y-%m-%d")
#         item['file'] = self.get_archivo()
#         # item['date_of'] = self.date_of
#         return item
#
#     class Meta:
#         verbose_name = 'Document'
#         verbose_name_plural = 'Documents'
#         ordering = ("id",)

class Branches(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Nombre sucursal')
    code = models.CharField(max_length=4, unique=True, verbose_name='Codigo')
    responsable = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=8, null=False, blank=False)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'
        ordering = ['id']


class Documents(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Tipo Documento')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ("id",)
