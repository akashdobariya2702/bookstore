from django.shortcuts import render
from rest_framework import serializers, viewsets

from .serializers import *
from .filters import *


class BooksBookViewSet(viewsets.ModelViewSet):
    queryset = BooksBook.objects.all().order_by('-download_count')
    serializer_class = BooksBookSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = BooksBookFilter
