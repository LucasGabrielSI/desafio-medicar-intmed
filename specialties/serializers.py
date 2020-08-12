from rest_framework.serializers import ModelSerializer
from .models import Specialties


class SpecialtiesSerializer(ModelSerializer):
    class Meta:
        model = Specialties
        fields = '__all__'
