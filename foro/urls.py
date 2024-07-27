from rest_framework.routers import DefaultRouter
from .views import ComunityViewSet, ForoViewSet

router = DefaultRouter()
router.register(r'comunidades', ComunityViewSet)
router.register(r'foro', ForoViewSet)
#con include traemos todas las r
urlpatterns = router.urls