# LIST OF MONTH OF YEAR
from django.db import models

lista_personals = [(1, 'Si'),
                   (0, 'No')]

lista_resguardo = [('AREA', 'Area'),
                   ('ARCHIVO', 'Archivo'),
                   ('EMPRESA', 'Empresa')]

lista_meses = [('ENERO', 'Enero'),
               ('FEBRERO', 'Febrero'),
               ('MARZO', 'Marzo'),
               ('ABRIL', 'Abril'),
               ('MAYO', 'Mayo'),
               ('JUNIO', 'Junio'),
               ('JULIO', 'Julio'),
               ('AGOSTO', 'Agosto'),
               ('SEPTIEMBRE', 'Septiembre'),
               ('OCTUBRE', 'Octubre'),
               ('NOVIEMBRE', 'Noviembre'),
               ('DICIEMBRE', 'Diciembre')]


class periodic_information():
    # INFORMACION PERIODICA
    date_of = models.DateField(format("YYYY-MM-DD"), null=True, blank=True)  # Fecha de
    date_to = models.DateField(format("YYYY-MM-DD"), null=True, blank=True)  # Fecha hasta
    month_of = models.CharField(max_length=10, choices=lista_meses, default='ENERO')
    month_to = models.CharField(max_length=10, choices=lista_meses, default='ENERO')
    year_of = models.CharField(max_length=4)
    year_to = models.CharField(max_length=4)
