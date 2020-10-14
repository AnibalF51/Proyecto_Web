from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def myfirstview(request):
    data = {
        'name': 'William'
    }

    return JsonResponse(data)
