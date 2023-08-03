from rest_framework import serializers

from .models import Cliente
from enderecos.models import Endereco
from django.shortcuts import get_object_or_404

from enderecos.serializers import EnderecoSerializer

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

    endereco = EnderecoSerializer()

    def create(self, validated_data):

        endereco = validated_data.pop("endereco")
        endereco = Endereco.objects.create(**endereco)
        return Cliente.objects.create(**validated_data, endereco=endereco)


class ClienteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
        read_only_fields = ["id"]

    endereco = EnderecoSerializer()

    def update(self, instance, validated_data):
        
        data = validated_data.copy()
        for key, value in data.items():
            if key == 'endereco':
                endereco = validated_data.pop("endereco")
                enderecoid = get_object_or_404(Endereco, id=instance.endereco.id)
                for key, value in endereco.items():
                    setattr(instance.endereco, key, value)
            else: 
                setattr(instance, key, value)
        
        instance.save()
        
        return instance
