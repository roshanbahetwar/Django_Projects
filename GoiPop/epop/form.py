from django import forms
from .models import EpopDetailsModels
from django.contrib.auth.models import User  # for signUp form create import user table


class EpopDetailsForm(forms.ModelForm):
    class Meta:
        model = EpopDetailsModels
        fields = "__all__"

    def clean_email(self):  # this is for field validation
        email = self.cleaned_data["email"]
        if email.endswith("@gmail.com"):
            return email
        else:
            raise forms.ValidationError("please enter correct email")


# for signUp
class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email", "first_name", "last_name"]
