from django.urls import path
from .views import index, edit, update  # Import your views

urlpatterns = [
    path('', index, name='index'),  # Define your URL patterns
    path('edit/<int:id>/', edit, name='edit'),
    path('update/<int:id>/', update, name='update'),
]
