from django.db import models
import uuid
from django.core.validators import MinValueValidator

class Venda(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    data = models.DateField()
    quantidade = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
    )
    valor = models.DecimalField(max_digits=15, decimal_places=2)

    produto = models.ForeignKey("produtos.Produto", on_delete=models.CASCADE)
    cliente = models.ForeignKey("clientes.Cliente", on_delete=models.CASCADE)