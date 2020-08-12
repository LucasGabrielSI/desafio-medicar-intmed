from django.db import models
from django.core.validators import EmailValidator
from specialties.models import Specialties


class Doctors(models.Model):
    nome = models.CharField(max_length=80)
    crm = models.CharField(max_length=10)
    e_mail = models.EmailField(validators=[EmailValidator], null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    especialidade = models.ForeignKey(
        to=Specialties,
        on_delete=models.SET_NULL,
        related_name='doctors_specialties',
        null=True
    )

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'

    def __str__(self):
        return self.nome
