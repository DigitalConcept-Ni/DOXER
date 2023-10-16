# from django.forms import *
# from Apps.administration.models import Documents
#
#
# class IndexingDocumentsForm(ModelForm):
#     class Meta:
#         model = Documents
#         fields = ['expedientsAdministration', 'document_type', 'date']
#
#         widgets = {
#             'date': DateInput(format='%Y-%m-%d',
#                               attrs={
#                                   'type': 'date'
#                               }),
#             'expedientsAdministration': Select(
#                 attrs={
#                     'class': 'select2',
#                 }
#             ),
#         }
