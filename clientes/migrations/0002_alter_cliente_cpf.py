# Generated by Django 4.2.4 on 2023-08-01 23:46

import cpf_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("clientes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="cpf",
            field=cpf_field.models.CPFField(max_length=14, verbose_name="cpf"),
        ),
    ]
