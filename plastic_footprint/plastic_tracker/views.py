from django.shortcuts import render, redirect

# Create your views here.


def landing_page(request):
    return render(request, "plastic_tracker/landing_page.html")


def customer_registration(request):
    return render(request, "plastic_tracker/customer_registration.html")
