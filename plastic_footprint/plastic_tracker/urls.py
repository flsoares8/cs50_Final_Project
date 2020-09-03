from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('register/', views.customer_registration,
         name='customer_registration'),
    path('client/<int:id>/', views.customer_info, name='customer_info')
]
