from django.urls import path
from .views import (home, CityDetailView, CityCreateView,
                    CityUpdateView, CityDeleteView)

app_name = 'cities'

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('add/', CityCreateView.as_view(), name='add'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),

]
