from django.shortcuts import render
from .form import DevDetailsForms
from .models import DevDetailsModels
from django.http import HttpResponse

# Create your views here.
def dev_form(r):
    form = DevDetailsForms()
    if r.method == "POST":
        form = DevDetailsForms(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Welcome To Dev Teams....</h1>")
    return render(r, "developer/dev_form.html", {"form": form})


def show_dev(r):
    dev = DevDetailsModels.objects.all()
    md = {"dev_list": dev}
    return render(r, "developer/show_list.html", context=md)
