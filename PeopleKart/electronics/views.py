from django.shortcuts import render
from .models import LaptopModel,MobileModel,TvModel
from .form import LaptopModelForm,MobileModelForm,TvModelForm
# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .form import SignUpForm

from django.db.models import Q,Max,Min,Count,Sum,Avg


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
    '''ORM Queries'''

    lap_list = LaptopModel.objects.all()
    # lap_list = LaptopModel.objects.filter(mqty__gt = 5)  # ORM query model qty greater than 5
    # lap_list = LaptopModel.objects.filter(mqty__gte = 10)  # ORM query model qty greater than and equal to 10
    # lap_list = LaptopModel.objects.filter(mqty__lt = 10) # ORM Query model qty less than 5
    # lap_list = LaptopModel.objects.filter(mqty__lte = 10)  # ORM query model qty less than equal to 10
    # lap_list = LaptopModel.objects.filter(mqty__exact = 10)
    # lap_list = LaptopModel.objects.filter(mname__exact = 'AsusN50')
    # lap_list = LaptopModel.objects.filter(mname__iexact = 'AsusN50')
    # lap_list = LaptopModel.objects.filter(mname__contains = 'asus')
    # lap_list = LaptopModel.objects.filter(mname__icontains = 'asus')
    # lap_list = LaptopModel.objects.filter(mname__contains = 'A') | LaptopModel.objects.filter(mname__contains = 'D')
    # lap_list = LaptopModel.objects.filter(id__in = [2,6,4,10])
    # lap_list = LaptopModel.objects.filter(mname__startswith = 'D')
    # lap_list = LaptopModel.objects.filter(mname__istartswith = 'A')
    # lap_list = LaptopModel.objects.filter(mname__istartswith = 'D') | LaptopModel.objects.filter(mname__istartswith = 'I') # OR operator
    # lap_list = LaptopModel.objects.filter(mname__startswith = 'A') & LaptopModel.objects.filter(mqty__gt = 10) # AND operator
    # lap_list = LaptopModel.objects.exclude(mname__istartswith = 'AsusN50')
    # lap_list= LaptopModel.objects.all().order_by('-id')
    # lap_list = LaptopModel.objects.all().values('id','mname','mprice')
    # lap_list = LaptopModel.objects.all().order_by('mqty')[0:5]  # ascending order to mqty row with 5 record
    # lap_list = LaptopModel.objects.all().order_by('-id')[0:5]    # descending order to id and 5 records
    # lap_list = LaptopModel.objects.all().order_by('-mprice')[0:5]
    # lap_list = LaptopModel.objects.all().order_by('-mprice')[6:10]
    # lap_list = LaptopModel.objects.all().order_by('-mprice')[2:10:2]

    # avg = LaptopModel.objects.all().aggregate(Avg('mqty'))  # for avg of mqty
    # print(avg)    # it will show output in terminal
    # max = LaptopModel.objects.all().aggregate(Max('mqty'))
    # min = LaptopModel.objects.all().aggregate(Min('mqty'))
    # count = LaptopModel.objects.all().aggregate(Count('mqty'))
    # sum = LaptopModel.objects.all().aggregate(Sum('mqty'))
    # print(max)
    # print(min)
    # print(count)
    # print(sum)

    return render(r,'electronics/laptopdetails.html',{'laptop_list':lap_list})

@login_required()
def mobileDetails(r):
    mob_list = MobileModel.objects.all()
    return render(r,'electronics/mobiledetails.html',{'mobile_list':mob_list})

@login_required()
def tvDetails(r):
    tv_list = TvModel.objects.all()
    return render(r,'electronics/tvdetails.html',{'tv_list':tv_list})

def signUp(r):
    form = SignUpForm()
    if r.method == 'POST':
        form = SignUpForm(r.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/home/')
    return render(r,'signup.html',{'form':form})

def update(r,id):
    form = LaptopModel.objects.get(id=id)
    if r.method == 'POST':
        form = LaptopModelForm(r.POST,instance=form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/electronics/laptopdetails/')
    return render(r,'electronics/update.html',{'form':form})

def delete(r,id):
    obj = LaptopModel.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect('/electronics/laptopdetails/')