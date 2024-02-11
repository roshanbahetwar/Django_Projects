from django.shortcuts import render
from .forms import LaptopModelform,MobileModelForm,TvModelForm
# Create your views here.
from django.http import HttpResponseRedirect
from .models import LaptopModel,MobileModel,TvModel
from django.contrib.auth.decorators import login_required



def laptop(r):
    form = LaptopModelform()
    if r.method == 'POST':  # if requst method is equal to is equal to POST...
        form = LaptopModelform(r.POST)  # then crteates again form come from users
        if form.is_valid():   # if form is valid then save.
            form.save()
            return HttpResponseRedirect('/index/')
    return render(r,'electronics/laptop.html',{'form':form})

def mobile(r):
    form = MobileModelForm()
    if r.method == 'POST':
        form = MobileModelForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    return render(r,'electronics/mobile.html',{'form':form})

def tv(r):
    form = TvModelForm()
    if r.method == 'POST':
        form = TvModelForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    return render(r,'electronics/tv.html',{'form':form})

@login_required()
def laptopDetails(r):
    laptop_list = LaptopModel.objects.all()   # ORM query (data come from database, it is used for save data show in frontend page)
    #laptop_list = LaptopModel.objects.filter(model_price__gt = 30000)   # for ORM query
    #laptop_list = LaptopModel.objects.filter(model_price__lt = 30000)
    #laptop_list = LaptopModel.objects.filter(model_price__exact = 25000)
    #laptop_list = LaptopModel.objects.filter(model_name__startswith="Dell")
    #laptop_list = LaptopModel.objects.all().order_by('model_qty')     # order by ascending order
    #laptop_list = LaptopModel.objects.all().order_by('-model_qty')[0:1]   # Max or top 1,  order by descending order
    #laptop_list = LaptopModel.objects.all().order_by('-model_qty')[0:5]   # top 5,  order by descending order
    return render(r,'electronics/laptopdetails.html',{'laptop_list':laptop_list})

@login_required()
def mobileDetails(r):
    mobile_list = MobileModel.objects.all()
    return render(r,'electronics/mobiledetails.html',{'mobile_list':mobile_list})

@login_required()
def tvDetails(r):
    tv_list = TvModel.objects.all()
    return render(r,'electronics/tvdetails.html',{'tv_list':tv_list})

def update(r,id):
    form = LaptopModel.objects.get(id=id)
    if r.method == "POST":
        form = LaptopModelform(r.POST,instance=form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/electronics/laptopdetails/')
    return render(r,'electronics/update.html',{'form':form})

def delete(r,id):
    obj = LaptopModel.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect('/electronics/laptopdetails/')