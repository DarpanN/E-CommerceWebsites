from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def inventory(request):
    return JsonResponse({"message":"hello from inventory app"})
