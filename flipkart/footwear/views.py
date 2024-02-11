from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ShoesModel,SportsModel,SlipperModel

# Create your views here.
from .forms import ShoesModelForm,SportsModelForm,SlipperModelForm    # for form class


# for forms create code
def shoes(r):
    form = ShoesModelForm()    # for create form
    if r.method == 'POST':     # if method is post, data came from user,then create form
        form = ShoesModelForm(r.POST)   # creating form
        if form.is_valid():               # data from user validate here,if data is valid then save
            form.save()                    # if data is valid then save
            return HttpResponseRedirect('/index/')
    return render(r,'footwear/shoes.html',{'form':form})

def sports(r):
    form = SportsModelForm()
    if r.method=="POST":
        form = SportsModelForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    return render(r,'footwear/sports.html',{'form':form})


def slipper(r):
    form = SlipperModelForm()
    if r.method=="POST":
        form = SlipperModelForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    return render(r,'footwear/slipper.html',{'form':form})

# for view details code
def shoesdetails(r):
    shoes_list = ShoesModel.objects.all()
    return render(r,'footwear/shoesdetails.html',{'shoes_list':shoes_list})

def sportsshoesdetails(r):
    sports_list = SportsModel.objects.all()
    return render(r,'footwear/sportsdetails.html',{'sports_list':sports_list})


def slipperdetails(r):
    slipper_list = SlipperModel.objects.all()
    return render(r,'footwear/slipperdetails.html',{'slipper_list':slipper_list})