from django.contrib import admin

# Register your models here.
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django-models.views.utils import has_role

@user_passes_test(lambda u: has_role(u, 'Admin'))
@login_required
def admin_dashboard(request):
    return render(request, 'admin_view.html')