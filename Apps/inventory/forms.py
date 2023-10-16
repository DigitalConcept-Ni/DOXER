from django.forms import *
from django import forms

from Apps.inventory.models import *


class BoxesForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        # self.fields['sucursal'].widget.attrs['autofocus'] = True

    class Meta:
        model = Boxes
        fields = '__all__'
        # fields = ['user', 'box', 'status', 'branch', 'date_joined']
        widgets = {
            'branch': Select(
                attrs={
                    'class': 'form-control select2',
                    'autofocus': True,
                }),
            'document': Select(
                attrs={
                    'class': 'form-control select2',
                }),
            'code': TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'user': TextInput(
                attrs={
                    'class': 'form-control',
                    'readonly': True,
                }),
            'date_joined': DateInput(
                attrs={
                    'class': 'form-control',
                    'readonly': True
                }),
            'start_date': DateInput(
                attrs={
                    'class': 'form-control',
                }),
            'end_date': DateInput(
                attrs={
                    'class': 'form-control',
                }),

        }
        exclude = ['user_update', 'user_creation', 'status']
