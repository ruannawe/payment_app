from django.urls import path
from .views import index  # Import your views

urlpatterns = [
    path('', index, name='index'),  # Define your URL patterns
]
