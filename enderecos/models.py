from django.db import models
import uuid


class Endereco(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    cidade = models.TextField(max_length=100)
    uf = models.TextField(max_length=2)
    rua = models.TextField(max_length=100)
    numero = models.PositiveIntegerField()