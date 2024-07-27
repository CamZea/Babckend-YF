from .models import Carrier
from .serializers import CarrierSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class CarrierViewSet(ModelViewSet):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer