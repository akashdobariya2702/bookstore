# python library

# django library
from rest_framework import serializers

from .models import *


class BooksAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAuthor
        exclude = ('id', )


class BooksBookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksBookshelf
        exclude = ('id', )


class BooksLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksLanguage
        exclude = ('id', )


class BooksSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksSubject
        exclude = ('id', )


class BooksFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksFormat
        exclude = ('id', 'book_id')


class BooksBookSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    shelves = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()
    formats = BooksFormatSerializer(read_only=True, many=True)

    def get_authors(self, obj):
        author_ids = obj.map_author.values_list('author_id', flat=True).distinct()
        authors = BooksAuthor.objects.filter(id__in=author_ids)

        return BooksAuthorSerializer(authors, many=True).data

    def get_shelves(self, obj):
        bookshelf_ids = obj.map_shelf.values_list('bookshelf_id', flat=True).distinct()
        shelves = BooksBookshelf.objects.filter(id__in=bookshelf_ids)

        # return BooksBookshelfSerializer(shelves, many=True).data
        return list(shelves.values_list('name', flat=True))

    def get_language(self, obj):
        language_ids = obj.map_language.values_list('language_id', flat=True).distinct()
        languages = BooksLanguage.objects.filter(id__in=language_ids)

        # return BooksLanguageSerializer(languages, many=True).data
        codes = list(languages.values_list('code', flat=True))
        return codes[0] if codes else None

    def get_subjects(self, obj):
        subject_ids = obj.map_subject.values_list('subject_id', flat=True).distinct()
        subjects = BooksSubject.objects.filter(id__in=subject_ids)

        return BooksSubjectSerializer(subjects, many=True).data

    class Meta:
        model = BooksBook
        # fields = '__all__'
        exclude = ('id', )
        # fields = ('id', )
