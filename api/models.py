from django.db import models
from model_utils.models import SoftDeletableModel, SoftDeletableManager

# Create your models here.

class BaseModel(SoftDeletableModel):
    objects = SoftDeletableManager
    objects = models.Manager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Ong(BaseModel):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14, unique=True)
    endereco = models.TextField()
    email = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.nome} - {self.email} - {self.endereco}"

class Pet(BaseModel):

    class Status_adocao(models.TextChoices):
        DISPONIVEL = "disponível", "Disponível"
        ADOTADO =  "adotado", "Adotado"
    
    class Porte_choices(models.TextChoices):
        GRANDE = "grande", "Grande"
        MEDIO = "médio", "Médio"
        PEQUENO = "pequeno", "Pequeno"

    nome = models.CharField(max_length=200)
    raca = models.CharField(max_length=50)
    porte = models.CharField(max_length=10, choices=Porte_choices.choices, default="pequeno")
    idade = models.IntegerField()
    status_adocao = models.CharField(max_length=30, choices=Status_adocao.choices, default=Status_adocao.DISPONIVEL)
    ong_associado = models.ForeignKey(Ong, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.raca} - {self.porte} - {self.idade} - {self.status_adocao} - {self.ong_associado}"
    

class Consulta(BaseModel):

    class StatusChoices(models.TextChoices):
        AGENDADO = "AGENDADO", "Agendado"
        CONCLUIDO = "CONCLUIDO", "Concluído"
        CANCELADO = "CANCELADO", "Cancelado"


    pet = models.ForeignKey(
        "Pet",
        on_delete=models.CASCADE,
        related_name="consultas"
    )

    data_hora = models.DateTimeField()

    veterinario = models.CharField(max_length=150)

    motivo = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.AGENDADO
    )

    def __str__(self):
        return f"{self.pet} - {self.data_hora} - {self.status}"