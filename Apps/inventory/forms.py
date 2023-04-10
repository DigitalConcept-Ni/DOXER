# from django.forms import *
# from django import forms
#
# from Apps.inventory.models import *
#
#
# class BranchesForms(ModelForm):
#     class Meta:
#         model = Branches
#         fields = 'name', 'code'
#
#         # widgets = {
#         #     'nombre': TextInput(
#         #         attrs={
#         #             'placeholder': 'Ingrese el nombre de un documento',
#         #             'autofocus': True
#         #         })
#         # }
#         # exclude = ['user_update', 'user_creation']
#
#
# class BoxesForms(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # for form in self.visible_fields():
#         #     form.field.widget.attrs['class'] = 'form-control'
#         #     form.field.widget.attrs['autocomplete'] = 'off'
#         # self.fields['sucursal'].widget.attrs['autofocus'] = True
#
#     class Meta:
#         model = Boxes
#         fields = ['user', 'box', 'status', 'branch', 'date_joined']
#         widgets = {
#             'branch': Select(
#                 attrs={
#                     'class': 'form-control select2',
#                     'autofocus': True,
#                 }),
#             'box': TextInput(
#                 attrs={
#                     'class': 'form-control',
#                 }),
#             'status': TextInput(
#                 attrs={
#                     'class': 'form-control'
#                 }),
#             'user': TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'readonly': True,
#                 }),
#             'date_joined': DateInput(
#                 attrs={
#                     'class': 'form-control',
#                     'readonly': True
#                 }),
#
#         }
#         # exclude = ['user_update', 'user_creation']
