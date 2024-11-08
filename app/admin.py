from django.contrib import admin
from .models import Pet,Petsitter,Service
# Register your models here.
admin.site.register(Pet)
admin.site.register(Petsitter)
admin.site.register(Service)