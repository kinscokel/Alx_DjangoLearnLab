from django.urls import path
from . import views

urlpatterns = [
    # Example route, add yours here
    path('', views.home, name='home'),  # Assuming you have a `home` view
]



from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Authentication URLs
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),

    # Built-in auth views for login/logout with custom templates
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]