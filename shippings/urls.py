from django.urls import path,include
from shippings.views import shipping

urlpatterns = [
  path("",shipping)  
    
]