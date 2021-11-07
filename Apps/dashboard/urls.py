from django.urls import path

from Apps.dashboard.views import dashboard

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashborad'),
]
