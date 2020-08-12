from rest_framework.serializers import ModelSerializer
from .models import Doctors


class DoctorsSerializer(ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['id', 'crm', 'nome', 'especialidade']
        depth = 1
