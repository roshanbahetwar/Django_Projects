from django.contrib import admin
from .models import HomeDetailsModels

# Register your models here.
class HomeDetailsAdmin(admin.ModelAdmin):
    list_display = ["name", "movie", "price", "date", "email", "mobile"]


admin.site.register(HomeDetailsModels, HomeDetailsAdmin)
