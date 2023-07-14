from django.shortcuts import render,redirect
from .form import PersonForm
from .models import Person

# Create your views here.
def create_person(r):
    if r.method == 'POST':
        form = PersonForm(r.POST)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = PersonForm()
        return render(r,'c_person.html',{'form':form})

def display(r):
    per = Person.objects.all()
    return render(r,'display.html',{'per':per})