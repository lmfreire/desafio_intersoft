from django.db import models
import uuid
from cpf_field.models import CPFField

class Cliente(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    nome = models.TextField(max_length=100)
    telefone = models.CharField(max_length=20)
    cpf = CPFField('cpf')

    endereco = models.OneToOneField("enderecos.endereco", on_delete=models.CASCADE)