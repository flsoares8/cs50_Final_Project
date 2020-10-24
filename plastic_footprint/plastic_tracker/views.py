from django.shortcuts import render, redirect
from .forms import CustomerForm, ProductForm
from .models import Customer, Product

# Create your views here.


def landing_page(request, id=0):
    if request.method == "GET":    
        form = CustomerForm()
        return render(request, "plastic_tracker/landing_page.html", {'form': form})
    else:
        id = request.POST['id_number']
        return redirect('/client/' + id)


def customer_registration(request):
    if request.method == "GET":
        form = CustomerForm()
        return render(request, "plastic_tracker/customer_registration.html", {'form': form})
    else:
        # if it is a POST, save the POST data
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

def customer_info(request, id):
    context = {'customer_info': Customer.objects.get(id_number=id)}
    return render(request, "plastic_tracker/customer_info.html", context)

def product_registration(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, "plastic_tracker/product_registration.html", {'form': form})
    else:
        # if it is a POST, save the POST data
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/productlist')

def product_list(request):
    context = {'product_list': Product.objects.all()}
    return render(request, "plastic_tracker/product_list.html", context)

def shopping_list(request):
    print(request)
    if request.method == "GET":
        form = ProductForm()
        return render(request, "plastic_tracker/shopping_list.html", {'form': form})
    elif 'register' in request.POST:
        print("REGISTER")

        return redirect('/shoppinglist')
    elif 'payment' in request.POST:
        print("PAYMENT")
        return redirect('/')

def process_payment(request):
    return redirect('/')
