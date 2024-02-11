from django import forms
from .models import MensModel,WomenModel,KidesModel


class MensModelForm(forms.ModelForm):
    class Meta:
        model = MensModel
        fields = '__all__'

class WomenModelForm(forms.ModelForm):
    class Meta:
        model = WomenModel
        fields = '__all__'

class KidsModelForm(forms.ModelForm):
    class Meta:
        model = KidesModel
        fields = '__all__'