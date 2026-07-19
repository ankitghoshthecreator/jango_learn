from django.shortcuts import render
from django.http import HttpResponse
from django.views import View  # Fix: was 'Views' (no such import)

# Create your views here.
def hello(request):
    return HttpResponse("hello")

class HelloWorld(View):
    def get(self, request):
        return HttpResponse("hello world")  # Fix: must return HttpResponse, not a plain string
