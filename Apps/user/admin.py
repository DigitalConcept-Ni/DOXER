from django.contrib import admin

# Register your models here.
from Apps.user.models import User

admin.site.register(User)
