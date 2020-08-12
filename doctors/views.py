from rest_framework import generics, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Doctors
from .serializers import DoctorsSerializer


class DoctorsList(generics.ListAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'especialidade__id']
