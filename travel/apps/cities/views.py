from django.shortcuts import render
from .models import City

def home(request):
    city = City.objects.all()
    return render(request, 'cities/home.html', {'objects_list': city})
