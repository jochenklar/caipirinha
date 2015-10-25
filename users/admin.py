from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import DetailKey, Profile


class DetailKeyAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(DetailKey, DetailKeyAdmin)
admin.site.register(Profile, ProfileAdmin)
