from django.shortcuts import render
from .models import CopperDetailsModels

# Create your views here.
def copshow(r):

    cop_list = CopperDetailsModels.objects.all()
    md = {'prd_list':cop_list}


    return render(r,'copper/cop.html',context=md)