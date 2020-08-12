from django.db import models
from doctors.models import Doctors
from users.models import User


class Consultation(models.Model):
    dia = models.DateField()
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(auto_now_add=True)
    medico = models.ForeignKey(
        to=Doctors,
        on_delete=models.SET_NULL,
        null=True)
    paciente = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='paciente_consulta')
    realizada = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

    def __str__(self):
        return f'Consulta com o(a) médico(a): { self.medico.nome }'
