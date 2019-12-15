from django.shortcuts import render
from .models import City
from django.views.generic.detail import DetailView


def home(request):
    city = City.objects.all()
    return render(request, 'cities/home.html', {'objects_list': city})


class CityDetailView(DetailView):
    model = City
    queryset = model.objects.all()
    context_object_name = 'object'
    template_name = 'cities/detail.html'
