from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def jan(request):
    return HttpResponse("eat no meat for the month")

def feb(request):
    return HttpResponse("walk for 20min every day")
