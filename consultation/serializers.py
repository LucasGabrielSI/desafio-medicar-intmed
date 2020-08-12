from rest_framework.serializers import ModelSerializer

from doctors.serializers import DoctorsSerializer
from .models import Consultation


class ConsultationSerializer(ModelSerializer):
    medico = DoctorsSerializer()

    class Meta:
        model = Consultation
        fields = ['id', 'dia', 'horario', 'data_agendamento', 'medico']
        depth = 2
