from django.urls import path
from . import views

urlpatterns = [
    # Example route, add yours here
    path('', views.home, name='home'),  # Assuming you have a `home` view
]