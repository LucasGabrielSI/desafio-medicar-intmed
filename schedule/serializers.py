from rest_framework.serializers import ModelSerializer
from .models import Schedule
from doctors.serializers import DoctorsSerializer


class ScheduleSerializer(ModelSerializer):
    medico = DoctorsSerializer()

    class Meta:
        model = Schedule
        fields = ['id', 'medico', 'dia', 'horarios']
        depth = 1
