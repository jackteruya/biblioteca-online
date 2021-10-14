from rest_framework.serializers import ModelSerializer

from obras.models import Obras


class ObrasSerializer(ModelSerializer):

    class Meta:
        model = Obras
        fields = '__all__'
