from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('register/', views.customer_registration,
         name='customer_registration'),
    path('client/<int:id>/', views.customer_info, name='customer_info'),
    path('registerproduct/', views.product_registration,
         name='product_registration'),
    path('productlist/', views.product_list, name='product_list'),
    path('shoppinglist/', views.shopping_list, name='shopping_list'),
    path('', views.process_payment, name='process_payment')
]
