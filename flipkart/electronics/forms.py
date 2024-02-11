from django import forms
from .models import LaptopModel,MobileModel,TvModel

class LaptopModelform(forms.ModelForm):       # from line no. 4 to 7 is form import from model.py for laptop.
    class Meta:
        model = LaptopModel
        fields = '__all__'

    # def clean_model_name(self):        # from line 9 to 14 is validation code for laptop model name.
    #     inputname = self.cleaned_data['model_name']
    #     if inputname.lower() in ['asus','samsung','hp','dell']:
    #         return inputname
    #     else:
    #         raise forms.ValidationError('Model should be either Asus, Samsung, Hp, Dell')


    def clean_model_price(self):        # from line 17 to 22 is validation code for laptop model price.
        price = self.cleaned_data['model_price']
        if price>15000:
            return price
        else:
            raise forms.ValidationError('Price should be greater than 15000')

class MobileModelForm(forms.ModelForm):        # from line no. 24 to 27 is form code import from model.py for mobile.
    class Meta:
        model = MobileModel
        fields = '__all__'

    # validation for model name
    def clean_model_name(self):
        name = self.cleaned_data['model_name']
        if len(name) <= 10:
            return name
        else:
            raise forms.ValidationError('model name should be less than or equal to 10')

    # validation for model price
    def clean_model_price(self):
        price = self.cleaned_data['model_price']
        if price > 30000:
            raise forms.ValidationError('price should be less than 30000')
        else:
            return price

    def clean_model_qty(self):
        qty = self.cleaned_data['model_qty']
        if qty <= 10:
            return qty
        else:
            raise forms.ValidationError('quantity of model should be less than or equal to 10 nos.')




class TvModelForm(forms.ModelForm):             # from line no. 24 to 27 is form code import from model.py for Tv.
    class Meta:
        model = TvModel
        fields = '__all__'