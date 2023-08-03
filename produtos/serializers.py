from rest_framework import serializers

from .models import Produto

from enderecos.serializers import EnderecoSerializer

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        read_only_fields = ["id"]


class ProdutoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        read_only_fields = ["id"]
