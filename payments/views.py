from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def payment(request):
    return JsonResponse({"message":"hello from payments app"})
