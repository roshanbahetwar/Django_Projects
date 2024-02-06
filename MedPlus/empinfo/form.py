from django import forms
from .models import EmpDetailsModels


class EmpDetailsForm(forms.ModelForm):
    class Meta:
        model = EmpDetailsModels
        fields = "__all__"
