from django.urls import path
from Apps.user.views import *

app_name = 'user'

urlpatterns = [
    # urls Secciones
    path('list/', UsersListview.as_view(), name='user_list'),
    path('add/', UserCreateview.as_view(), name='user_create'),
    path('update/<int:pk>/', UserUpdateview.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]