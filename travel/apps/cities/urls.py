from django.urls import path
from .views import home, CityDetailView, CityCreateView


app_name = 'cities'

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('add/', CityCreateView.as_view(), name='add'),

]
