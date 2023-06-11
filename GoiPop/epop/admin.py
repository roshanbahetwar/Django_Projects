from django.contrib import admin
from .models import EpopDetailsModels

# Register your models here.
class EpopDetailsAdmin(admin.ModelAdmin):
    list_display = ['name','address','pan','email','mobile']

admin.site.register(EpopDetailsModels,EpopDetailsAdmin)