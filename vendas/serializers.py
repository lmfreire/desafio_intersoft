from rest_framework import serializers

from .models import Venda
from produtos.models import Produto
from django.shortcuts import get_object_or_404

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = "__all__"
        read_only_fields = ["id","valor"]

    def create(self, validated_data):

        produto = validated_data.pop("produto")
        cliente = validated_data.pop("cliente")

        validated_data["valor"] = produto.valor * validated_data["quantidade"]  

        produto.quantidade -= validated_data["quantidade"]
        produto.save()

        return Venda.objects.create(**validated_data, produto=produto, cliente=cliente)


class VendaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = "__all__"

