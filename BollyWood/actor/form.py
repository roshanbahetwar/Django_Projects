from django import forms
from .models import ActorDetailsModel


class ActorDetailsForm(forms.ModelForm):
    class Meta:
        model = ActorDetailsModel
        fields = "__all__"
