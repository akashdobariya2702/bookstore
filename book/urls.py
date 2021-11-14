# python library

# django library
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

# project library
from .views import *

router = DefaultRouter()

# app urls
router.register(r'book', BooksBookViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
