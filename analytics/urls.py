from django.urls import path,include
from analytics.views import analytic

urlpatterns = [
  path("",analytic)  
    
]