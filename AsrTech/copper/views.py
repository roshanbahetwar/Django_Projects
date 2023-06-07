from django.shortcuts import render
from .models import CopperDetailsModels
from .form import FeedbackForm

# Create your views here.
def copshow(r):
    cop_list = CopperDetailsModels.objects.all()
    md = {'prd_list':cop_list}

    return render(r,'copper/cop.html',context=md)

def feedback(r):
    form = FeedbackForm()
    fd = {'form': form}
    return render(r,'copper/feedback.html',context=fd)