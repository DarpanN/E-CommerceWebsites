from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def review(request):
    return JsonResponse({"message":"hello from reviews app"})
