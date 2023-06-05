from django.shortcuts import render
from .models import HomeDetailsModels

# Create your views here.
def show(r):
    prd_list = HomeDetailsModels.objects.all()
    prd_dict = {'prd_list':prd_list}

    return render(r,'home/show.html',context=prd_dict)