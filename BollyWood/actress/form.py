from django import forms
from .models import ActressDetailsModels

class ActressDetailsForm(forms.ModelForm):
    class Meta:
        model = ActressDetailsModels
        fields = '__all__'