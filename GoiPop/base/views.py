from django.shortcuts import render

# Create your views here.
def home(r):
    return render(r,'base.html')

def indexHome(r):
    return render(r,'home.html')

def homePage(r):
    return render(r,'homepage.html')