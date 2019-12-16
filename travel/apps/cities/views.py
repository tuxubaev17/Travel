from django.shortcuts import render
from .models import City
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .forms import CityForm
from django.urls import reverse_lazy


def home(request):
    if request.method == 'POST':
        form = CityForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
    form = CityForm()
    cities = City.objects.all()
    return render(request, 'cities/home.html', {'objects_list': cities, 'form': form})


class CityDetailView(DetailView):
    model = City
    queryset = model.objects.all()
    context_object_name = 'object'
    template_name = 'cities/detail.html'


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')
