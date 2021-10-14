from rest_framework import serializers

from obras.models import Obras, Autor


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['nome', ]


class ObrasSerializer(serializers.ModelSerializer):
    autores = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Obras
        fields = '__all__'
