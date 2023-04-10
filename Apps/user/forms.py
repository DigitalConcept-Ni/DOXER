from django.forms import *

from Apps.user.models import *


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'is_superuser', 'is_staff']
        widgets = {
            'first_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre',
                    'autofocus': True
                }),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese Apellidos ',
                    'autofocus': True
                }),
            'username': TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre de usuario ',
                    'autofocus': True
                }),

            'password': PasswordInput(render_value=True,
                                      attrs={
                                          'placeholder': 'Ingrese contrasenia',
                                          'autofocus': True
                                      }),
            'email': EmailInput(
                attrs={
                    'placeholder': 'Ingrese correo electronico',
                    'autofocus': True
                }),
        }
        exclude = ['last_login', 'date_joined']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


# class EnterpriseForm(ModelForm):
#     class Meta:
#         model = Enterprises
#         fields = ['name', 'manager', 'address', 'phone_number', 'email']
#         widgets = {
#             'email': EmailInput(),
#         }
