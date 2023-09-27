from django.contrib import admin

# Register your models here.
from .models import Product, Traveler , LoginAttempt

# Register your models here.
admin.site.register(Product)
admin.site.register(Traveler)
admin.site.register(LoginAttempt)
