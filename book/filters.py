import django_filters.rest_framework

from django_filters.rest_framework import Filter
from django.db.models import Q

from .models import *


class BooksBookFilter(django_filters.rest_framework.FilterSet):
    book_id = django_filters.CharFilter(field_name='gutenberg_id', lookup_expr='exact')
    language = Filter(method='filter_language')
    mime_type = django_filters.CharFilter(field_name='formats__mime_type', lookup_expr='icontains')
    topic = Filter(method='filter_topic')
    author = django_filters.CharFilter(
        field_name='map_author__author_id__name',
        lookup_expr='icontains'
    )
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = BooksBook
        fields = ['book_id', 'language', 'mime_type', 'topic', 'author', 'title']

    def filter_language(self, queryset, name, value):
        values = [x.strip() for x in value.split(',')]

        qs_params = None
        for search in values:
            q = Q(map_language__language_id__code__icontains=search)
            if qs_params:
                qs_params = qs_params | q  # or & for filtering
            else:
                qs_params = q

        return queryset.filter(qs_params)

    def filter_topic(self, queryset, name, value):
        values = [x.strip() for x in value.split(',')]

        qs_params = None
        for search in values:
            q = (Q(map_subject__subject_id__name__icontains=search)
                 | Q(map_shelf__bookshelf_id__name__icontains=search))
            if qs_params:
                qs_params = qs_params | q  # or & for filtering
            else:
                qs_params = q

        return queryset.filter(qs_params)
