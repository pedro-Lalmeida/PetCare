from rest_framework.routers import DefaultRouter
from api.views import OngViewSet, PetViewSet, ConsultaViewSet

router = DefaultRouter()

router.register('ongs', OngViewSet, basename='ong')
router.register('pets', PetViewSet, basename='pet')
router.register('consultas', ConsultaViewSet, basename='consulta')