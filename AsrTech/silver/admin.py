from django.contrib import admin
from .models import SilverDetailsModels

# Register your models here.
class SilverDetailsAdmin(admin.ModelAdmin):
    list_display = ["product", "price", "qty", "date"]


admin.site.register(SilverDetailsModels, SilverDetailsAdmin)
