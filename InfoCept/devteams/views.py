from django.shortcuts import render,redirect
from .models import TeamsModelDetails
from .form import TeamsDetailsForm

# Create your views here.
def show(r):
    team_show = TeamsModelDetails.objects.all()
    md = {'teams_list':team_show}

    return render(r,'devteams/teams.html',context=md)

import datetime
def indexPage(r):

    date = datetime.datetime.now()

    data = {
        'title': 'WelCome to InfoCept | Pune, 441014 |' ,'date':str(date)
    }
    return render(r,'home.html',context=data)


def teamsForm(r):
    form = TeamsDetailsForm()
    if r.method == 'POST':
        form = TeamsDetailsForm(r.POST)
        if form.is_valid():
            form.save()
            return redirect('/devteams/teams/')
    return render(r,'devteams/teamsform.html',{'form':form})
