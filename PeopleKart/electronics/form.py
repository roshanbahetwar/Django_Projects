from .models import LaptopModel,MobileModel,TvModel
from django import forms


class LaptopModelForm(forms.ModelForm):
    class Meta:
        model = LaptopModel
        fields = '__all__'

class MobileModelForm(forms.ModelForm):
    class Meta:
        model = MobileModel
        fields = '__all__'

class TvModelForm(forms.ModelForm):
    class Meta:
        model = TvModel
        fields = '__all__'