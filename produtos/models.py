from django.db import models
import uuid
from django.core.validators import MinValueValidator

class Produto(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    nome = models.TextField(max_length=100)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    quantidade = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
    )
