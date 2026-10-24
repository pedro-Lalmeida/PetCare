from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Ong, Pet, Consulta
from api.serializers import OngSerializer, PetSerializer, ConsultaSerializer


class OngViewSet(ModelViewSet):
    queryset = Ong.objects.all()
    serializer_class = OngSerializer
    
    # usando query_params
    def get_queryset(self):
        # Começamos pegando todas as ONGs do banco
        queryset = Ong.objects.all()
        
        # Captura os query_params da URL (?nome=... ou ?email=...)
        nome_param = self.request.query_params.get('nome')
        email_param = self.request.query_params.get('email')

        # Se o usuário passou ?nome= na URL, filtramos no banco
        if nome_param:
            queryset = queryset.filter(nome__iexact=nome_param) # iexact ignora maiúsculas/minúsculas
            
        # Se o usuário passou ?email= na URL, filtramos também
        if email_param:
            queryset = queryset.filter(email__iexact=email_param)
            
        return queryset

    # Permissões
    def get_permissions(self):

        """
        Bloqueia a criação/edição de ONGs para administradores, 
        mas permite a listagem para qualquer usuário logado.
        
        Isso diz ao Django: "Para continuar com essa operação de escrita, 
        o usuário obrigatoriamente precisa estar logado e ser um administrador no seu perfil"

        se não entrar nesse caso apenas pede uma autenticação normal
        """

        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        
        return [IsAuthenticated()]

    # cache de 5 min
    @method_decorator(cache_page(60*5))                    # define o tempo do cache
    @method_decorator(vary_on_headers("Authorization"))  # aqui varia a resposta de acordo com os diferentes tokens
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    


class PetViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    
    # query_params
    def get_queryset(self):
        queryset = Pet.objects.all()

        nome = self.request.query_params.get('nome')
        raca = self.request.query_params.get('raca')
        porte = self.request.query_params.get('porte')
        status = self.request.query_params.get('status_adocao')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        if raca:
            queryset = queryset.filter(raca__icontains=raca)

        if porte:
            queryset = queryset.filter(porte__iexact=porte)

        if status:
            queryset = queryset.filter(status_adocao__iexact=status)

        return queryset

    # config das permissões
    def get_permissions(self):
        
        """
        Bloqueia a criação/edição de ONGs para administradores, 
        mas permite a listagem para qualquer usuário logado.
        
        Para continuar com essa operação de escrita, 
        o usuário obrigatoriamente precisa estar logado e ser um administrador no seu perfil
        """

        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        
        return [IsAuthenticated()]

    # cache de 5 min
    @method_decorator(cache_page(60*5))
    @method_decorator(vary_on_headers("Authorization"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    


class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    # filtros automáticos
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['data_hora', 'veterinario', 'motivo', 'status']

    # permissões para essa viewset
    permission_classes = [IsAuthenticated]

    # cache de 5 min
    @method_decorator(cache_page(60*5))
    @method_decorator(vary_on_headers("Authorization"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)