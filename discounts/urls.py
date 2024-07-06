from django.urls import path,include
from discounts.views import discount

urlpatterns = [
  path("",discount)  
    
]