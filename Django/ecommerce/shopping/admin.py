from django.contrib import admin
from .models import Product, User, BuyProduct

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(BuyProduct)