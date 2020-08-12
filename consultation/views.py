import time
from datetime import date

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Consultation
from .serializers import ConsultationSerializer
from schedule.models import Schedule


class ConsultationList(generics.ListCreateAPIView):
    queryset = Consultation.objects.all().filter(realizada=False).order_by('dia', 'horario')
    serializer_class = ConsultationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        for consultation in Consultation.objects.filter(paciente__id=request.user.id).all():
            if date.today() >= consultation.dia:
                if time.strftime("%H:%M:%S") > str(consultation.horario) \
                        and not consultation.realizada:
                    obj_consultation = Consultation.objects.get(id=consultation.id)
                    obj_consultation.realizada = True
                    obj_consultation.save()
        consultations = Consultation.objects.filter(realizada=False, paciente__id=request.user.id)
        serializer = ConsultationSerializer(consultations, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        agenda_id = request.data['agenda_id']
        horario = request.data['horario'] + ':00'

        try:
            agenda = Schedule.objects.get(id=agenda_id)
        except Schedule.DoesNotExist:
            return Response({
                'msg': 'Nenhuma agenda encontrada com esse id',
                'status': status.HTTP_404_NOT_FOUND
            })
        else:
            for horario_agenda in agenda.horarios:
                if horario == str(horario_agenda):
                    if Consultation.objects.filter(dia=agenda.dia, horario=horario, paciente=request.user).exists():
                        return Response({'msg': 'Já existe uma consulta marcada para esse dia e horário!'})
                    else:
                        consultation = Consultation.objects.create(
                            dia=agenda.dia,
                            horario=horario_agenda,
                            medico=agenda.medico,
                            paciente=request.user
                        )
                        schedule = Schedule.objects.filter(horarios__contains=[horario], id=agenda_id)
                        if schedule.exists():
                            schedule_object = schedule.first()
                            schedule_object.horarios.remove(horario_agenda)
                            schedule_object.save()
                        serializer = ConsultationSerializer(consultation)
                        return Response(serializer.data)
        return Response({'msg': 'O horário selecionado não está disponível'})


class ConsultationDestroy(generics.DestroyAPIView):
    queryset = Consultation.objects.all().filter(realizada=False)
    serializer_class = ConsultationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        if Consultation.objects.filter(id=kwargs['pk'], paciente=request.user, realizada=False).exists():
            return self.destroy(request, *args, **kwargs)
        else:
            return Response({
                'msg': 'Não é possível desmarcar uma consulta de outro paciente ou que não existe',
                'status': status.HTTP_204_NO_CONTENT
            })
