from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import DetailKey, Detail


class DetailKeyAdmin(admin.ModelAdmin):
    pass


class DetailAdmin(admin.ModelAdmin):
    pass

admin.site.register(DetailKey, DetailKeyAdmin)
admin.site.register(Detail, DetailAdmin)


class DetailInline(admin.StackedInline):
    model = Detail
    can_delete = False
    verbose_name_plural = 'details'


class UserAdmin(UserAdmin):
    inlines = (DetailInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)