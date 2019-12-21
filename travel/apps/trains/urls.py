from django.urls import path
from .views import (home, TrainCreateView, TrainDetailView, TrainUpdateView, TrainDeleteView)

app_name = "train"

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='detail'),
    path('add/', TrainCreateView.as_view(), name='add'),
    path('update/<int:pk>/', TrainUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='delete'),

]
