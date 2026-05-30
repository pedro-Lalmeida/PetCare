from rest_framework import serializers
from .models import Ong, Pet, Consulta

class OngSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ong
        fields = ['id', 'nome', 'cnpj', 'endereco', 'email', 'created_at', 'updated_at']

class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = ['id', 'nome', 'raca', 'porte', 'idade', 'status_adocao', 'ong_associado', 'created_at', 'updated_at']

class ConsultaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consulta
        fields = ['id', 'pet', 'data_hora', 'veterinario', 'motivo', 'status', 'created_at', 'updated_at']