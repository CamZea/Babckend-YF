from rest_framework.serializers import ModelSerializer
from .models import Comunity, Foro

class ComunitySerializer(ModelSerializer):
    class Meta:
        model= Comunity
        fields= (
            'id',
            'name',
        )

class ForoSerializer(ModelSerializer):
    class Meta:
        model= Foro
        fields= '__all__'
    
  