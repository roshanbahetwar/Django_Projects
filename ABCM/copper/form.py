from django import forms
from .models import CopperDetailsModels


class CopperDetailsForms(forms.ModelForm):
    class Meta:
        model = CopperDetailsModels
        fields = "__all__"
