from django.forms import *
from Apps.administration.models import Documents


class IndexingDocumentsForm(ModelForm):
    class Meta:
        model = Documents
        fields = ['expedients']

        widgets = {
            # 'description': Select(
            #     attrs={
            #         'class': 'select2',
            #     }
            # ),
            'expedients': Select(
                attrs={
                    'class': 'select2',
                }
            ),
        }
