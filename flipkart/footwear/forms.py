from django import forms
from .models import ShoesModel,SportsModel,SlipperModel

class ShoesModelForm(forms.ModelForm):
    class Meta:
        model = ShoesModel
        fields = '__all__'

class SportsModelForm(forms.ModelForm):
    class Meta:
        model = SportsModel
        fields = '__all__'

class SlipperModelForm(forms.ModelForm):
    class Meta:
        model = SlipperModel
        fields = '__all__'