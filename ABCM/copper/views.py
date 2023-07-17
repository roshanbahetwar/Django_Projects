from django.shortcuts import render,redirect
from .form import CopperDetailsForms
from .models import CopperDetailsModels
from django.http import HttpResponse

# Create your views here.
def copper_form(r):
    form = CopperDetailsForms()
    if r.method == 'POST':
        form = CopperDetailsForms(r.POST)
        if form.is_valid():
            form.save()
            return redirect('/copper/copper_show/')
    return render(r,'copper/copper_form.html',{'form':form})

def copper_show(r):
    cop_show = CopperDetailsModels.objects.all()
    md = {'cop_list':cop_show}
    return render(r,'copper/cop_show.html',context=md)

def indexPage(r):
    data = {
        'title':'Welcome To ABCM | Mumbai'
    }

    return render(r,'index.html',data)