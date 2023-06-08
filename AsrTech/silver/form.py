from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=20)
    age = forms.IntegerField()
    email = forms.EmailField()
    city = forms.CharField(max_length=20)
