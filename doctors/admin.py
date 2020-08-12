from django.contrib import admin
from .models import Doctors


class DoctorsAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'crm']
    list_display = ['nome', 'crm', 'e_mail', 'telefone', 'especialidade']


admin.site.register(Doctors, DoctorsAdmin)
