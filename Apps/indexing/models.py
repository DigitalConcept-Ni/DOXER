# from django.db import models
#
# # Create your models here.
# # from crum import get_current_user
# from django.db import models
#
# # Create your models here.
# from django.forms import model_to_dict
#
# # from Aplicaciones.RRHH.models import Expedientes
# from config import settings
#
# class Serials(models.Model):
#     name = models.CharField(max_length=50, unique=True, verbose_name='Serie Documental')
#
#     def __str__(self):
#         return  self.name
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
# class Document_type(models.Model):
#     sub_serial = models.ForeignKey(Sub_serial, on_delete= models.CASCADE)
#     name = models.CharField(max_length=50, unique=True,  verbose_name='Tipo Documento')
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
#
# class Departaments(models.Model):
#     name = models.CharField(max_length=20)
#     responsable = models.CharField(max_length=20, null=True, blank=True)
#
#     def __str__(self):
#         return self.name
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
# class Templates(models.Model):
#     template_name = models.CharField(max_length=20)
#     departament = models.ForeignKey(
#         Departaments, on_delete=models.CASCADE)
#
#     # archivo = models.FileField(upload_to='pdf/%Y/%m/%d', null=True, blank=True)
#
#     def __str__(self):
#         return self.template_name
#
#     # def save(self, *args, **kwargs):
#     #     user = get_current_user()
#     #     if user is not None:
#     #         if not self.pk:
#     #             self.user_creation = user
#     #         else:
#     #             self.user_updated = user
#     #     super(Plantillas, self).save(*args, **kwargs)
#
#     def toJSON(self):
#         item = model_to_dict(self)
#         item['departament'] = self.departament.toJSON()
#         return item
#
#     class Meta:
#         verbose_name = 'Template'
#         verbose_name_plural = 'Templates'
#         ordering = ("id",)
#
#
# class Fields(models.Model):
#     template = models.ForeignKey(
#         Templates, on_delete=models.CASCADE)
#     field_name = models.CharField(max_length=20)
#     data_type = models.CharField(
#         max_length=30, default='TEXTO')
#     status = models.CharField(max_length=1, default='0')
#
#     def __str__(self):
#         return self.field_name
#
#     # def save(self, *args, **kwargs):
#     #     user = get_current_user()
#     #     if user is not None:
#     #         if not self.pk:
#     #             self.user_creation = user
#     #         else:
#     #             self.user_updated = user
#     #     super(Documentos, self).save(*args, **kwargs)
#
#     def toJSON(self):
#         item = model_to_dict(self)
#         item['template'] = self.template.toJSON()
#         return item
#
#     class Meta:
#         verbose_name = 'Field'
#         verbose_name_plural = 'Fields'
#         ordering = ("id",)
#
#
# class Expedients(models.Model):
#     departament = models.ForeignKey(Departaments, on_delete=models.CASCADE)
#     serial = models.ForeignKey(Serials, on_delete=models.CASCADE)
#     sub_serial = models.ForeignKey(Sub_serial, on_delete=models.CASCADE)
#     document_type = models.ForeignKey(Document_type, on_delete=models.CASCADE)
#     template = models.ForeignKey(Templates, on_delete=models.CASCADE, null=True, blank=True)
#     lista_resguardo = [('AREA', 'Area'),
#                        ('ARCHIVO', 'Archivo'),
#                        ('LOGICSA', 'Logicsa')]
#     lista_meses = [('ENERO', 'Enero'),
#                    ('FEBRERO', 'Febrero'),
#                    ('MARZO', 'Marzo'),
#                    ('ABRIL', 'Abril'),
#                    ('MAYO', 'Mayo'),
#                    ('JUNIO', 'Junio'),
#                    ('JULIO', 'Julio'),
#                    ('AGOSTO', 'Agosto'),
#                    ('SEPTIEMBRE', 'Septiembre'),
#                    ('OCTUBRE', 'Octubre'),
#                    ('NOVIEMBRE', 'Noviembre'),
#                    ('DICIEMBRE', 'Diciembre')]
#     status = models.CharField(max_length=10, choices=lista_resguardo, default='AREA') # Donde se encuentra resguardado
#     codigo_archivo = models.CharField(max_length=10)
#     codigo_cliente = models.CharField(max_length=10)
#     description = models.CharField(max_length=50, null=True, blank=True)
#     # INFORMACION PERIODICA
#     date_of = models.DateField(format("YYYY-MM-DD"),null=True, blank=True)  # Fecha de
#     date_to = models.DateField(format("YYYY-MM-DD"),null=True, blank=True)  # Fecha hasta
#     month_of = models.CharField(max_length=10, choices=lista_meses, default='ENERO')
#     month_to = models.CharField(max_length=10, choices=lista_meses, default='ENERO')
#     year_of = models.CharField(max_length=4)
#     year_to = models.CharField(max_length=4)
#     file = models.FileField(upload_to='administrativos/%Y/%m/%d', null=True, blank=True)
#     # rc = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.codigo_cliente
#
#     def get_archivo(self):
#         if self.file:
#             return '{}{}'.format(settings.MEDIA_URL, self.file)
#         return 'No insertado'
#
#     def toJSON(self):
#         item = model_to_dict(self)
#         item['departament'] = self.departament.toJSON()
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
# class Documents(models.Model):
#     expedients = models.ForeignKey(Expedients, on_delete=models.CASCADE)
#     document_type = models.ForeignKey(Document_type, on_delete=models.CASCADE)
#     template = models.ForeignKey(Templates, on_delete=models.CASCADE, null=True, blank=True)
#     # INFORMACION PERIODICA
#     lista_resguardo = [('AREA', 'Area'),
#                        ('ARCHIVO', 'Archivo'),
#                        ('LOGICSA', 'Logicsa')]
#     lista_meses = [('ENERO', 'Enero'),
#                    ('FEBRERO', 'Febrero'),
#                    ('MARZO', 'Marzo'),
#                    ('ABRIL', 'Abril'),
#                    ('MAYO', 'Mayo'),
#                    ('JUNIO', 'Junio'),
#                    ('JULIO', 'Julio'),
#                    ('AGOSTO', 'Agosto'),
#                    ('SEPTIEMBRE', 'Septiembre'),
#                    ('OCTUBRE', 'Octubre'),
#                    ('NOVIEMBRE', 'Noviembre'),
#                    ('DICIEMBRE', 'Diciembre')]
#     date_of = models.DateField(format("YYYY-MM-DD"), null=True, blank=True)  # Fecha de
#     date_to = models.DateField(format("YYYY-MM-DD"), null=True, blank=True)  # Fecha hasta
#     month_of = models.CharField(max_length=10, choices=lista_meses, default='ENERO')
#     month_to = models.CharField(max_length=10, choices=lista_meses, default='ENERO')
#     year_of = models.CharField(max_length=4)
#     year_to = models.CharField(max_length=4)
#     # ARCHIVOS
#     file = models.FileField(upload_to='administrativos/%Y/%m/%d', null=True, blank=True)
#
#     def get_archivo(self):
#         if self.file:
#             return '{}{}'.format(settings.MEDIA_URL, self.file)
#         return 'No insertado'
#
#     def toJSON(self):
#         item = model_to_dict(self)
#         item['expedients'] = self.expedients.toJSON()
#         item['document_type'] = self.document_type.toJSON()
#         if self.date_of:
#             item['date_of'] = self.date_of.strftime("%Y-%m-%d")
#         if self.date_to:
#             item['date_to'] = self.date_to.strftime("%Y-%m-%d")
#         item['file'] = self.get_archivo()
#         # item['date_of'] = self.date_of
#         return item
#
#     class Meta:
#         verbose_name = 'Document'
#         verbose_name_plural = 'Documents'
#         ordering = ("id",)
#
# class Detail_Field(models.Model):
#     expedients = models.ForeignKey(Expedients, on_delete=models.CASCADE, null=True, blank=True)
#     document = models.ForeignKey(Documents, on_delete=models.CASCADE, null=True, blank=True)
#     field = models.ForeignKey(Fields, on_delete=models.CASCADE)
#     detail = models.CharField(max_length=300)
#     data_type = models.CharField(max_length=15)
#
#     def toJSON(self):
#         item = model_to_dict(self)
#         item['field'] = self.field.toJSON()
#         return item
#
#     class Meta:
#         verbose_name = 'Detail_Field'
#         verbose_name_plural = 'Detail_Fiels'
#         ordering = ("id",)
#
# # class other2(models.Model):
# #     name = models.CharField(max_length=10)
