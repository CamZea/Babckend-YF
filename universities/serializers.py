from rest_framework.serializers import ModelSerializer
from .models import Carrier

class CarrierSerializer(ModelSerializer):
    class Meta:
        
        model = Carrier
        fields= '__all__'