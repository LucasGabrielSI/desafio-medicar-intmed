from django.contrib.postgres.fields import ArrayField
from django.db import models

from doctors.models import Doctors
from validators import validate_date_schedule


class Schedule(models.Model):
    medico = models.ForeignKey(
        to=Doctors,
        on_delete=models.SET_NULL,
        related_name='doctors_schedule',
        null=True
    )
    dia = models.DateField(validators=[validate_date_schedule])
    horarios = ArrayField(
        models.TimeField(),
        size=10,
        help_text="Adicione as horas separadas por vírgula, ex: 10:00,11:00,12:00"
    )
    agenda_completa = models.BooleanField(verbose_name='Agenda Completa', default=False)

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

    def __str__(self):
        return f'Agenda do médico(a): { self.medico.nome }'
