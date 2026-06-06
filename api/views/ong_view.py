from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

from api.models import Ong
from api.serializers import OngSerializer


class OngViewSet(ModelViewSet):
    queryset = Ong.objects.all()
    serializer_class = OngSerializer
    search_fields = ['nome', 'email']
    filter_backends = [filters.SearchFilter]

    @method_decorator(cache_page(60))
    @method_decorator(vary_on_headers("Authorization"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)