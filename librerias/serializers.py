from rest_framework import serializers
from .models import Persona
from .models import Producto
from rest_framework.serializers import ModelSerializer

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = (
            'id',
            'nombre',
            'apellido',
            'password',
            'mail',
        )

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = (
            'id',
            'nombre',
            'precio',
            'imagen',
            'description',
        )