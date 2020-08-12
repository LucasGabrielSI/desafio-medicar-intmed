from django.contrib import admin
from .models import Consultation


class ConsultationAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'medico', 'dia', 'horario', 'realizada']

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Consultation, ConsultationAdmin)
