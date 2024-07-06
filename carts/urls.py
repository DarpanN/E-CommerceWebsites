from django.urls import path,include
from carts.views import cart

urlpatterns = [
  path("",cart)  
    
]