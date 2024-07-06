from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def shipping(request):
    return JsonResponse({"message":"hello from shipping app"})
