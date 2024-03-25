from rest_framework import viewsets
from . import models
from . import serializers
import django_filters.rest_framework
from rest_framework import filters
# Create your views here.


class ProductViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter]

class CategoryViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter]
