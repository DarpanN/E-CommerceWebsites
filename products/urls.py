from django.urls import path,include
from products.views import product

urlpatterns = [
  path("",product)  
    
]