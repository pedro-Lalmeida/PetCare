from django.db import models
from model_utils.models import SoftDeletableModel

# Create your models here.

class BaseModel(SoftDeletableModel):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        abstract = True