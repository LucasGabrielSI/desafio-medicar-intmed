from django.contrib import admin, messages
from .models import Schedule


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['medico', 'dia', 'horarios', 'agenda_completa']

    def save_model(self, request, obj, form, change):
        if Schedule.objects.filter(medico__id=obj.medico.id, dia__exact=obj.dia).exists():
            messages.set_level(request, messages.ERROR)
            messages.error(request, 'Só deve existir uma agenda por dia para cada médico!')
        else:
            super(ScheduleAdmin, self).save_model(request, obj, form, change)


admin.site.register(Schedule, ScheduleAdmin)
