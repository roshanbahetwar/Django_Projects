from django.contrib import admin
from .models import CopperDetailsModels

# Register your models here.
class CopperDetailsAdmin(admin.ModelAdmin):
    list_display = ['product','price','qty','date']

admin.site.register(CopperDetailsModels,CopperDetailsAdmin)