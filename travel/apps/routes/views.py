from django.shortcuts import render
from .forms import *
from django.contrib import messages


def dfs_paths(graph, start, goal):
    """Функция поиска всех мозможных маршрутов
    из одного города в другой. Вариант посещениея одного и того же города более одного раза,
    не рассматривается"""
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def home(request):
    form = RouteForm
    return render(request, 'routes/home.html', {'form': form})


def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            assert False
        return render(request, 'routes/home.html', {'form': form})
    else:
        messages.error(request, 'Создайте маршрут')
        form = RouteForm
        return render(request, 'routes/home.html', {'form': form})
