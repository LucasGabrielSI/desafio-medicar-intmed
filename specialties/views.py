from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Specialties
from .serializers import SpecialtiesSerializer


class SpecialtiesList(generics.ListAPIView):
    queryset = Specialties.objects.all()
    serializer_class = SpecialtiesSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['nome', ]
