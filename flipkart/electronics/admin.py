from django.contrib import admin
from .models import LaptopModel,MobileModel,TvModel

# Register your models here.

class LaptopModelAdmin(admin.ModelAdmin):
    list_display = ['model_name','model_price','model_qty']


class MobileModelAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'model_price', 'model_qty']


class TvModelAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'model_price', 'model_qty']

admin.site.register(LaptopModel,LaptopModelAdmin)
admin.site.register(MobileModel, MobileModelAdmin)
admin.site.register(TvModel, TvModelAdmin)