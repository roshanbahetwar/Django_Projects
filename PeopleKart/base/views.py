from django.shortcuts import render

# Create your views here.
def index(r):
    return render(r,'base.html')

def peopleKart(r):
    return render(r,'home.html')

def homePage(r):
    return render(r,'homepage.html')