from django import forms
from .models import TeamsModelDetails

class TeamsDetailsForm(forms.ModelForm):
    class Meta:
        model = TeamsModelDetails
        fields = "__all__"

    # validation for name
    def clean_name(self):
        name = self.cleaned_data["name"]
        if name == name.capitalize():
            return name
        else:
            raise forms.ValidationError("first character of name should be Capital.")

    # validation for age
    def clean_age(self):
        age = self.cleaned_data["age"]
        if age <= 30:
            return age
        else:
            raise forms.ValidationError("age should be less than or equal to 30 years.")

    # validation for salary
    def clean_salary(self):
        salary = self.cleaned_data["salary"]
        if salary < 50000:
            raise forms.ValidationError("Salary Should not be less than 50000.")
        else:
            return salary
