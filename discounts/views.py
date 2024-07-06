from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def discount(request):
    return JsonResponse({"message":"hello from discount app"})
