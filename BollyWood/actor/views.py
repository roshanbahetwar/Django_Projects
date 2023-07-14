from django.shortcuts import render
from .form import ActorDetailsForm
from .models import ActorDetailsModel
from django.http import HttpResponse
# Create your views here.
def actor_form(r):
    form = ActorDetailsForm()
    if r.method == 'POST':
        form = ActorDetailsForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Thanks for visiting...</h1>')
    return render(r,'actor/dev_form.html',{'form':form})

def show(r):
    actor = ActorDetailsModel.objects.all()
    md = {'actor_list':actor}
    return render(r,'actor/actor_list.html',context=md)