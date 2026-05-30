from rest_framework import serializers
from .models import Ong, Pet, Consulta

class OngSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ong
        fields = ['id', 'nome', 'cnpj', 'telefone', 'cidade', 'created_at', 'updated_at']

class PetSerializer(serializers.ModelSerializer):

    ong_detalhes = OngSerializer(source='ong', read_only=True)

    class Meta:
        model = Pet
        fields = ['id', 'ong', 'ong_detalhes', 'nome', 'especie', 'idade', 'status', 'created_at', 'updated_at']

class ConsultaSerializer(serializers.ModelSerializer):

    pet_detalhes = PetSerializer(source='pet', read_only=True)

    class Meta:
        model = Consulta
        fields = ['id', 'pet', 'pet_detalhes', 'data_hora', 'veterinario', 'motivo', 'status', 'created_at', 'updated_at']