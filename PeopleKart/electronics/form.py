from .models import LaptopModel, MobileModel, TvModel
from django import forms
from django.contrib.auth.models import User


class LaptopModelForm(forms.ModelForm):
    class Meta:
        model = LaptopModel
        fields = "__all__"


class MobileModelForm(forms.ModelForm):
    class Meta:
        model = MobileModel
        fields = "__all__"

    def clean_mprice(self):
        price = self.cleaned_data["mprice"]
        if price <= 30000:
            return price
        else:
            raise forms.ValidationError("Model price should not more than 30000")

    def clean_mqty(self):
        qty = self.cleaned_data["mqty"]
        if qty <= 10:
            return qty
        else:
            raise forms.ValidationError("model qty should not be more than.")


class TvModelForm(forms.ModelForm):
    class Meta:
        model = TvModel
        fields = "__all__"

    def clean_mprice(self):
        price = self.cleaned_data["mprice"]
        if price <= 30000:
            return price
        else:
            raise forms.ValidationError("Model price should not more than 30000")


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email", "first_name", "last_name"]
