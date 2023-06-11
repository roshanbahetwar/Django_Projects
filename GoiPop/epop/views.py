from django.shortcuts import render
from .form import EpopDetailsForm
from .models import EpopDetailsModels
from django.http import HttpResponse
# Create your views here.
def epopform(r):
    form = EpopDetailsForm()
    if r.method == 'POST':
        form = EpopDetailsForm(r.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('<h1> Thanks For Registration</h1>')
    return render(r,'epop/registration.html',{'form':form})

def epopshow(r):
    pop_list = EpopDetailsModels.objects.all()
    md = {'erd_list':pop_list}

    return render(r,'epop/edetail.html',context=md)