from django.shortcuts import render

# Create your views here.
def baseHome(r):

    return render(r, "base.html")


def baseIndex(r):

    return render(r, "index.html")


def homeBase(r):

    return render(r, "home.html")
