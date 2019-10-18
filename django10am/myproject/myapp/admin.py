from django.contrib import admin

from .models import Register,Custom_User
# Register your models here.

admin.site.register(Register)
admin.site.register(Custom_User)