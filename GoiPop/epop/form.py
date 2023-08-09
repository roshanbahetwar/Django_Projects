import re

from django import forms
from .models import EpopDetailsModels

class EpopDetailsForm(forms.ModelForm):
    class Meta:
        model = EpopDetailsModels
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data['email']
        if email.endswith('@gmail.com'):
            return email
        else:
            raise forms.ValidationError('please enter correct email')