from django.shortcuts import render, redirect
from .form import EmpDetailsForm
from .models import EmpDetailsModels
from django.http import HttpResponse

# Create your views here.
def empForm(r):
    form = EmpDetailsForm()
    if r.method == "POST":
        form = EmpDetailsForm(r.POST)
        if form.is_valid():
            form.save()
        return redirect("/emp/empform/")
    return render(r, "empinfo/emp.html", {"form": form})


def empShow(r):
    med = EmpDetailsModels.objects.all()
    md = {"med_lst": med}
    return render(r, "empinfo/empshow.html", context=md)


import datetime


def indexPage(r):
    data = datetime.datetime.date(datetime.datetime.now())
    md = {"title": "Welcome To MedPlus Facility | Nagpur |", "Date:-": data}
    return render(r, "home.html", context=md)
