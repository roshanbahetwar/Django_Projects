from django.shortcuts import render

# Create your views here.
def personal(r):
    return render(r, "loan/personal_loan.html")
