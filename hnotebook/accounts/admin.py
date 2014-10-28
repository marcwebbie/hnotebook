from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User

from .models import Profile

class ProfileInline(admin.StackedInline):
    """Define an inline admin descriptor for Employee model
    which acts a bit like a singleton"""
    model = Profile
    can_delete = False

class UserAdmin(UserAdmin):
    """Defines a new user admin"""
    inlines = (ProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# Uregister group
admin.site.unregister(Group)
