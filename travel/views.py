from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    name = "Bob"
    context = {"name":name}
    return render(request, "home.html", context)
