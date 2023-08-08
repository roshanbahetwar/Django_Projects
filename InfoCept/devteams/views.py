from django.shortcuts import render,redirect
from .models import TeamsModelDetails

# Create your views here.
def show(r):
    team_show = TeamsModelDetails.objects.all()
    md = {'teams_list':team_show}

    return render(r,'devteams/teams.html',context=md)

def indexPage(r):

    data = {
        'title': 'WelCome to InfoCept | Pune, 441014'
    }
    return render(r,'index.html',context=data)