from django.contrib import admin

# Register your models here.
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django-models.views.utils import has_role

@user_passes_test(lambda u: has_role(u, 'Admin'))
@login_required
def admin_dashboard(request):
    return render(request, 'admin_view.html')


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (_('Additional Info'), {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Additional Info'), {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)