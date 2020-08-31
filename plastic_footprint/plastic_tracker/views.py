from django.shortcuts import render

# Create your views here.


def landing_page(request):
    return render(request, "plastic_tracker/landing_page.html")
