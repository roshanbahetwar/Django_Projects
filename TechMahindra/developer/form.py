from django import forms
from .models import DevDetailsModels

class DevDetailsForms(forms.ModelForm):
    class Meta:
        model = DevDetailsModels
        fields = '__all__'