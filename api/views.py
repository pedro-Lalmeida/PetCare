from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

from api.models import Ong, Pet, Consulta
from api.serializers import OngSerializer, PetSerializer, ConsultaSerializer


class OngViewSet(ModelViewSet):
    queryset = Ong.objects.all()
    serializer_class = OngSerializer
    search_fields = ['nome', 'email']
    filter_backends = [filters.SearchFilter]

    # config das permissões
    def get_permissions(self):
        """
        Bloqueia a criação/edição de ONGs para administradores, 
        mas permite a listagem para qualquer usuário logado.
        
        Isso diz ao Django: "Para continuar com essa operação de escrita, 
        o usuário obrigatoriamente precisa estar logado e ser um administrador no seu perfil"
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        
        return [IsAuthenticated()]

    # cache 
    @method_decorator(cache_page(60))                    # define o tempo do cache
    @method_decorator(vary_on_headers("Authorization"))  # aqui varia a resposta de acordo com os diferentes tokens
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    


class PetViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    search_fields = ['nome', 'raca', 'status_adocao', 'porte']
    filter_backends = [filters.SearchFilter]

    # config das permissões
    def get_permissions(self):
        
        """
        Bloqueia a criação/edição de ONGs para administradores, 
        mas permite a listagem para qualquer usuário logado.
        
        Isso diz ao Django: "Para continuar com essa operação de escrita, 
        o usuário obrigatoriamente precisa estar logado e ser um administrador no seu perfil"
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        
        return [IsAuthenticated()]

    @method_decorator(cache_page(60))
    @method_decorator(vary_on_headers("Authorization"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    


class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    search_fields = ['veterinario', 'status', 'pet__nome']
    filter_backends = [filters.SearchFilter]

    # config das permissões
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60))
    @method_decorator(vary_on_headers("Authorization"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)