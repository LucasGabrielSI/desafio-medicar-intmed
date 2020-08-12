import time
from datetime import date

from django.db.models import Q
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from doctors.models import Doctors
from .models import Schedule
from .serializers import ScheduleSerializer


class ScheduleList(generics.ListAPIView):
    queryset = Schedule.objects.all().filter(agenda_completa=False).order_by('dia')
    serializer_class = ScheduleSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Schedule.objects.all().filter(agenda_completa=False)

        medico = self.request.query_params.get('medico', None)
        especialidade = self.request.query_params.get('especialidade', None)
        data_inicio = self.request.query_params.get('data_inicio', None)
        data_final = self.request.query_params.get('data_final', None)

        if not ((medico and especialidade and data_inicio and data_final) is None):
            queryset = queryset.filter(
                Q(medico__in=Doctors.objects.filter(especialidade=especialidade)) |
                Q(medico__id=medico), Q(agenda_completa=False)).filter(dia__gte=data_inicio, dia__lte=data_final)
        return queryset

    def get(self, request, *args, **kwargs):
        for schedule in self.get_queryset():
            for horario in schedule.horarios:
                if time.strftime("%H:%M:%S") > str(horario) and date.today() >= schedule.dia:
                    schedule.horarios.remove(horario)
                    schedule.save()

            if date.today() > schedule.dia or len(schedule.horarios) is 0 and schedule.agenda_completa is False:
                obj_schedule = Schedule.objects.get(id=schedule.id)
                obj_schedule.agenda_completa = True
                obj_schedule.save()
        schedules = self.get_queryset()
        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data)
