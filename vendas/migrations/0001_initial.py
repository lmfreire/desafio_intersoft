# Generated by Django 4.2.4 on 2023-08-02 23:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("clientes", "0002_alter_cliente_cpf"),
        ("produtos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Venda",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("data", models.DateField()),
                (
                    "quantidade",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                ("valor", models.DecimalField(decimal_places=2, max_digits=15)),
                ("cliente", models.ManyToManyField(to="clientes.cliente")),
                (
                    "produto",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="produtos.produto",
                    ),
                ),
            ],
        ),
    ]
