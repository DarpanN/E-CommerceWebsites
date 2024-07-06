from django.urls import path,include
from inventory.views import inventory

urlpatterns = [
  path("",inventory)  
    
]