from rest_framework.routers import DefaultRouter
from .views import OngViewSet, PetViewSet, ConsultaViewSet

router = DefaultRouter()
router.register('ongs', OngViewSet)
router.register('pets', PetViewSet)
router.register('consultas', ConsultaViewSet)