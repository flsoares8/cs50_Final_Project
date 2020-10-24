from django import forms
from .models import Customer, Product


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('fullname', 'id_number')

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

class SearchForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('id_number',)