from django.shortcuts import render

# Create your views here.
def homeBase(r):

    return render(r, "developer/home.html")
