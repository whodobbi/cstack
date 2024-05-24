from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from myauth.models import CstackUser


class CstackUserAdmin(UserAdmin):
    pass


admin.site.register(CstackUser, CstackUserAdmin)
