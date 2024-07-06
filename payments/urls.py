from django.urls import path,include
from payments.views import payment

urlpatterns = [
  path("",payment)  
    
]