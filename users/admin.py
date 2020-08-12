from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from users.models import User


class UserAdmin (DjangoUserAdmin):
    search_fields = ['nome', 'email', ]
    list_display = ['nome', 'email', ]
    fieldsets = (
        (None, {'fields': ("nome", "email",), }
         ),
    )


admin.site.register(User, UserAdmin)
