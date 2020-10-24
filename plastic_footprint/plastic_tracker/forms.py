from django import forms
from .models import Customer, Product


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        #fields = '__all__'
        fields = ('fullname', 'id_number')
        
    # def __init__(self, *args, **kwargs):
    #     super(EmployeeForm, self).__init__(*args, **kwargs)
    #     self.fields['position'].empty_label = "Select"
    #     self.fields['emp_code'].required = False

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

class SearchForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('id_number',)