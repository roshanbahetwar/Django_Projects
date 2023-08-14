from django.shortcuts import render
from .form import EpopDetailsForm,SignUpForm
from .models import EpopDetailsModels
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def epopform(r):
    form = EpopDetailsForm()
    if r.method == 'POST':
        form = EpopDetailsForm(r.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/epop/show/')
    return render(r,'epop/registration.html',{'form':form})

@login_required()
def epopshow(r):
    pop_list = EpopDetailsModels.objects.all()
    md = {'erd_list':pop_list}

    return render(r,'epop/edetail.html',context=md)

def signUp(r):
    form = SignUpForm()
    if r.method == 'POST':
        form = SignUpForm(r.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/home/')
    return render(r,'signup.html',{'form':form})