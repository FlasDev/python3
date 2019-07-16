from django.urls import path
from . import views

urlpatterns = [
    path('calculator/', views.get_data),
]

