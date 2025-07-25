"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


# project/urls.py

from django.urls import path, include
from relationship_app import views

urlpatterns = [
    path('', include('relationship_app.urls')),  # Adjust if your app name differs
]


from django.contrib import admin
from django.urls import path
from relationship_app.views import home  # Replace 'your_app' with your actual app name

urlpatterns = [
    path('admin/', admin.site.urls),  # <--- This handles the empty path
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]

from django.urls import path
from relationship_app import views  # import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path('', views.home, name='home'),  # Add this line

]


from django.urls import path
from django-models.views.admin_view import admin_dashboard
from django-models.views.librarian_view import librarian_dashboard
from django-models.views.member_view import member_dashboard

urlpatterns = [
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian/dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member/dashboard/', member_dashboard, name='member_dashboard'),
]
