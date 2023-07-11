from django.shortcuts import render
from .form import ActressDetailsForm
from .models import ActressDetailsModels
from django.http import HttpResponse

# Create your views here.
def actress_form(r):
    form = ActressDetailsForm()
    if r.method == 'POST':
        form = ActressDetailsForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Thanks for Registrations</h1>')
    return render(r,'actress/actress_details.html',{'form':form})

def show(r):
    actress = ActressDetailsModels.objects.all()
    md = {'actress_list':actress}
    return render(r,'actress/actress_list.html',context=md)