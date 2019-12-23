from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import TrainForm
from .models import Train
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


def home(request):
    trains = Train.objects.all()
    paginator = Paginator(trains, 10)
    page = request.GET.get('page')
    trains = paginator.get_page(page)
    return render(request, 'trains/home.html', {'objects_list': trains})


class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('train:home')
    success_message = 'Поезд успешно создан!'


class TrainDetailView(DetailView):
    model = Train
    queryset = model.objects.all()
    context_object_name = 'object'
    template_name = 'trains/detail.html'


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('train:home')
    success_message = 'Поезд успешно изменен!'


class TrainDeleteView(DeleteView):
    model = Train
    template_name = 'trains/delete.html'
    success_url = reverse_lazy('train:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Поезд успешно удален!')
        return self.post(request, *args, **kwargs)
