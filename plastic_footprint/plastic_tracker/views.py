from django.shortcuts import render, redirect
from .forms import CustomerForm, ProductForm
from .models import Customer, Product

# Create your views here.


def landing_page(request):
    if request.method == "GET":    
        form = CustomerForm()
        return render(request, "plastic_tracker/landing_page.html", {'form': form})
    else:
        id = request.POST['id_number']
        return redirect('/client/' + id)


def client_registration(request):
    if request.method == "GET":
        form = CustomerForm()
        return render(request, "plastic_tracker/client_registration.html", {'form': form})
    else:
        # if it is a POST, save the POST data
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

def client_info(request, id):
    context = {'client_info': Customer.objects.get(id_number=id)}
    return render(request, "plastic_tracker/client_info.html", context)

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

def shopping_list(request, id=0):
    data = {'client_info': Customer.objects.get(id_number=id)}
    client = data['client_info']
    if request.method == "GET":
        form = ProductForm()
        return render(request, "plastic_tracker/shopping_list.html", {'form': form, 'client': client})
    elif 'register' in request.POST:
        product_id = request.POST['product_id']
        the_shopping_list.append(product_id)
        return redirect('/shoppinglist/'+str(client.id_number))
    elif 'payment' in request.POST:
        process_payment(the_shopping_list, client.id_number)
        the_shopping_list.clear()
        return redirect('../client/' + id)

def process_payment(a_shopping_list, client_id):
    client = Customer.objects.get(id_number=client_id)
    for id in a_shopping_list:
        product = Product.objects.get(product_id=id)
        client.monthly_balance -= product.plastic_weight
    client.save()

the_shopping_list = []