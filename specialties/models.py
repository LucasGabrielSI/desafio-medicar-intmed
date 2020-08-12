from django.db import models


class Specialties(models.Model):
    nome = models.CharField(max_length=80)

    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return self.nome
