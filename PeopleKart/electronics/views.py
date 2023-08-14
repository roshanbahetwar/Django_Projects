from django.shortcuts import render
from .models import LaptopModel,MobileModel,TvModel
from .form import LaptopModelForm,MobileModelForm,TvModelForm
# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def laptopNew(r):
    form = LaptopModelForm()
    if r.method == 'POST':
        form = LaptopModelForm(r.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/electronics/laptopdetails/')
    return render(r,'electronics/laptopNew.html',{'form':form})

def mobile(r):
    form = MobileModelForm()
    if r.method == 'POST':
        form = MobileModelForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/electronics/mobiledetails/')
    return render(r,'electronics/mobile.html',{'form':form})

def tv(r):
    form = TvModelForm()
    if r.method == 'POST':
        form = TvModelForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/electronics/tvdetails')
    return render(r,'electronics/tv.html',{'form':form})

@login_required()
def laptopDetails(r):
    lap_list = LaptopModel.objects.all()
    return render(r,'electronics/laptopdetails.html',{'laptop_list':lap_list})

@login_required()
def mobileDetails(r):
    mob_list = MobileModel.objects.all()
    return render(r,'electronics/mobiledetails.html',{'mobile_list':mob_list})

@login_required()
def tvDetails(r):
    tv_list = TvModel.objects.all()
    return render(r,'electronics/tvdetails.html',{'tv_list':tv_list})