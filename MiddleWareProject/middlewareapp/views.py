from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(r):
    print('Logic')
    return HttpResponse('<h1><center>This is Test for MiddleWare</center></h1>')