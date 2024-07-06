from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def cart(request):
    return JsonResponse({"message":"hello from cart app"})
