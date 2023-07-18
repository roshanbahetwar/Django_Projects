from django.shortcuts import render

# Create your views here.
def HomePage(r):
    return render(r,'home/home_page.html')