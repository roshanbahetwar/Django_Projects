from django.contrib import admin
from .models import TeamsModelDetails

# Register your models here.
class TeamsDetailsAdmin(admin.ModelAdmin):
    list_display = ['name','age','salary','city']

admin.site.register(TeamsModelDetails,TeamsDetailsAdmin)