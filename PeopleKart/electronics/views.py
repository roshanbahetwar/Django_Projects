from django.shortcuts import render
from .models import LaptopModel,MobileModel,TvModel
from .form import LaptopModelForm,MobileModelForm,TvModelForm
# Create your views here.
from django.http import HttpResponseRedirect

def laptopNew(r):
    form = LaptopModelForm()
    if r.method == 'POST':
        form = LaptopModelForm(r.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/home/')
    return render(r,'electronics/laptopNew.html',{'form':form})

def mobile(r):
    form = MobileModelForm()
    if r.method == 'POST':
        form = MobileModelForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    return render(r,'electronics/mobile.html',{'form':form})

def tv(r):
    form = TvModelForm()
    if r.method == 'POST':
        form = TvModelForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    return render(r,'electronics/tv.html',{'form':form})

def laptopDetails(r):
    lap_list = LaptopModel.objects.all()
    return render(r,'electronics/laptopdetails.html',{'laptop_list':lap_list})
