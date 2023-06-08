from django.shortcuts import render
from .models import SilverDetailsModels
from .form import FeedbackForm

# Create your views here.
def silshow(r):
    sil_list = SilverDetailsModels.objects.all()
    sd = {'sil_list':sil_list}

    return render(r,'silver/sil.html',context=sd)

def feedback(r):
    form = FeedbackForm()
    fd = {'form':form}
    return render(r, 'silver/feedback.html',context=fd)