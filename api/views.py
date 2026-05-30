from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Ong, Pet, Consulta
from .serializers import OngSerializer, PetSerializer, ConsultaSerializer

# Create your views here.

class OngViewSet(ModelViewSet):
    queryset = Ong.objects.all()
    serializer_class = OngSerializer

class PetViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer