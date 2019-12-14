from django.urls import path
from .views import home

app_name = 'cities'

urlpatterns = [
    path('', home, name='home'),

]
