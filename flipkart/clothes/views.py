from django.shortcuts import render
from .forms import MensModelForm,WomenModelForm,KidsModelForm
# Create your views here.
from django.http import HttpResponseRedirect
from .models import MensModel,WomenModel,KidesModel


def mens(r):
    form = MensModelForm        # from line no. 9 and 15 used to create form and line no. 2 for import form.
    if r.method == "POST":      # from line 10 to 14 use for post data from form and return to homepage.
        form = MensModelForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    return render(r,'clothes/mens.html',{'form':form})

def women(r):
    form = WomenModelForm
    if r.method == "POST":
        form = WomenModelForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    return render(r,'clothes/women.html',{'form':form})

def kids(r):
    form = KidsModelForm
    if r.method == "POST":
        form = KidsModelForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    return render(r,'clothes/kids.html',{'form':form})

def mensDetails(r):
    mens_list = MensModel.objects.all()
    return render(r,'clothes/mensdetails.html',{'mens_list':mens_list})

def womenDetails(r):
    women_list = WomenModel.objects.all()
    return render(r,'clothes/womendetails.html',{'women_list':women_list})

def kidsDetails(r):
    kids_list = KidesModel.objects.all()
    return render(r,'clothes/kidsdetails.html',{'kids_list':kids_list})