from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Ong, Pet, Consulta
from .serializers import OngSerializer, PetSerializer, ConsultaSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
# Create your views here.

class OngViewSet(ModelViewSet):
    queryset = Ong.objects.all()
    serializer_class = OngSerializer
    search_fields = ['nome', 'email']
    
    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    

class PetViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    search_fields = ['nome', 'raca', 'status_adocao', 'porte']

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    search_fields = ['veterinario', 'status', 'pet__nome']

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)