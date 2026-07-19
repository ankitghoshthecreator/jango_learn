from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from .models import MenueItem, Reservation
from .forms import ResForm

def hello(request):
    return HttpResponse("hello")

class HelloWorld(View):
    def get(self, request):
        return HttpResponse("hello world")

def home(request):
    if request.method == 'POST':
        form = ResForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your reservation has been confirmed successfully!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ResForm()
        
    menu_items = MenueItem.objects.all()
    return render(request, 'firstapp/home.html', {
        'form': form,
        'menu_items': menu_items
    })

def seed_menu(request):
    if request.method == 'POST':
        # Create some premium menu items if none exist
        if not MenueItem.objects.exists():
            items = [
                {"name": "Seared Wagyu Ribeye", "price": 85},
                {"name": "White Truffle Tagliolini", "price": 64},
                {"name": "Caviar & Oyster Platter", "price": 95},
                {"name": "Saffron Lobster Thermidor", "price": 78},
                {"name": "Valrhona Chocolate Soufflé", "price": 22}
            ]
            for item in items:
                MenueItem.objects.create(name=item["name"], price=item["price"])
            messages.success(request, "Sample menu seeded successfully!")
    return redirect('home')

