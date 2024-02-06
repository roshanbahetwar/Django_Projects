from django.shortcuts import render
from .form import TeamDetailsForms
from .models import TeamModelDetails
from django.http import HttpResponse

# Create your views here.


def teamsForm(r):

    form = TeamDetailsForms()
    if r.method == "POST":
        form = TeamDetailsForms(r.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("<h1>Thanks for Visiting</h1>")
    return render(r, "team/reg.html", {"form": form})


def teamsShow(r):
    team = TeamModelDetails.objects.all()
    md = {"teams_lst": team}
    return render(r, "team/show.html", context=md)
