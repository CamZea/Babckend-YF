from .views import CarrierViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'carriers',CarrierViewSet)

urlpatterns = router.urls


