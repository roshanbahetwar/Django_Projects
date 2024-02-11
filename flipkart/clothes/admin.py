from django.contrib import admin
from .models import MensModel,WomenModel,KidesModel
# Register your models here.

class MensModelAdmin(admin.ModelAdmin):
    list_display = ['cloth_category','cloth_price','cloth_qty']


class WomenModelAdmin(admin.ModelAdmin):
    list_display = ['cloth_category','cloth_price','cloth_qty']

class KidsModelAdmin(admin.ModelAdmin):
    list_display = ['cloth_category','cloth_price','cloth_qty']

admin.site.register(MensModel,MensModelAdmin)
admin.site.register(WomenModel,WomenModelAdmin)
admin.site.register(KidesModel,KidsModelAdmin)