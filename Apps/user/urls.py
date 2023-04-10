from django.urls import path

from Apps.user.views.users.views import *

app_name = 'panel'
urlpatterns = [
    # urls users
    path('user/list/', UsersListview.as_view(), name='user_list'),
    path('user/add/', UserCreateview.as_view(), name='user_create'),
    path('user/update/<int:pk>/', UserUpdateview.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]
