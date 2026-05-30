from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import OngViewSet, PetViewSet, ConsultaViewSet

router = DefaultRouter()
router.register('ongs', OngViewSet)
router.register('pets', PetViewSet)
router.register('consultas', ConsultaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]