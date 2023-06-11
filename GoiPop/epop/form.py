from django import forms
from .models import EpopDetailsModels

class EpopDetailsForm(forms.ModelForm):
    class Meta:
        model = EpopDetailsModels
        fields = '__all__'