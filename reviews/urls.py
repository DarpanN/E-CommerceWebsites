from django.urls import path,include
from reviews.views import review

urlpatterns = [
  path("",review)  
    
]