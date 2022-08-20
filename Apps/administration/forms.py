from django.forms import *

from Apps.administration.models import *


class SerialsForms(ModelForm):
    class Meta:
        model = Serials
        fields = '__all__'


class SubSerialsForms(ModelForm):
    class Meta:
        model = Sub_serial
        fields = '__all__'


class DocumentsTypeForms(ModelForm):
    class Meta:
        model = Document_type
        fields = '__all__'


class DepartamentoForms(ModelForm):
    class Meta:
        model = Departaments
        fields = 'name', 'responsable'
        # widgets = {
        #     'nombre': TextInput(
        #         attrs={
        #             'placeholder': 'Ingrese el nombre de un documento',
        #             'autofocus': True
        #         })
        # }


class CamposForms(ModelForm):
    class Meta:
        # model = Fields
        fields = 'field_name', 'data_type'
        # widgets = {
        #     'nombre': TextInput(
        #         attrs={
        #             'placeholder': 'Ingrese el nombre de un documento',
        #             'autofocus': True
        #         })
        # }


class DocumentacionForms(ModelForm):
    class Meta:
        model = Expedients
        fields = '__all__'
        widgets = {
            'date_of': DateInput(format='%Y-%m-%d',
                                 attrs={
                                     'type': 'date'
                                 }),
            'date_to': DateInput(format='%Y-%m-%d',
                                 attrs={
                                     'type': 'date'
                                 }),
            'description': Textarea(attrs={
                'rows': 3,
                'cols': 50,
            }),
            'personal_info': Select(attrs={
                'class': 'form-control',
            })
        }


class DocumentsForms(ModelForm):
    class Meta:
        model = Documents
        fields = '__all__'
        widgets = {
            'date': DateInput(format='%Y-%m-%d',
                                 attrs={
                                     'type': 'date'
                                 }),
        }


class ConsultaForm(Form):
    departamentos = ModelChoiceField(queryset=Departaments.objects.all(), widget=Select(
        attrs={'class': 'form-control'}))

    documentos = ModelChoiceField(queryset=Document_type.objects.all(), widget=Select(
        attrs={'class': 'form-control'}))

    date_range = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off'
    }))


class PersonalInfoForms(ModelForm):
    class Meta:
        model = Personals
        fields = ['names', 'surnames', 'phone_number', 'card_id', 'address']
