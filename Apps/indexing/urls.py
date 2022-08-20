from django.urls import path

from Apps.indexing.views import IndexacionDoc

app_name = 'indexing'

urlpatterns = [
    # urls indexing
    # path('document/', IndexacionView, name='index_document'),
    path('document/', IndexacionDoc.as_view(), name='index_document'),
]
