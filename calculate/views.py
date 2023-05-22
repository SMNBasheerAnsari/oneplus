from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def addition(request):
    return HttpResponse("Addition is done")
def multiplication(request):
    return HttpResponse("Multiplication is done")