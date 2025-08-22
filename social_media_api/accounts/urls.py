from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]


from django.urls import path
from .views import UserListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
]