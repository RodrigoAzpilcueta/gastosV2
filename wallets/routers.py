from .views import ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'wallets', ProfileViewSet)
urlpatterns = router.urls