from django.shortcuts import render, redirect
from .forms import CustomerForm

# Create your views here.


def landing_page(request):
    return render(request, "plastic_tracker/landing_page.html")


def customer_registration(request):
    form = CustomerForm(request.POST)
    if form.is_valid():
        form.save()
    #     return redirect('tracker/')
    return render(request, "plastic_tracker/customer_registration.html", {'form': form})
