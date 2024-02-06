from django import forms
from .models import TeamModelDetails


class TeamDetailsForms(forms.ModelForm):
    class Meta:
        model = TeamModelDetails
        fields = "__all__"
