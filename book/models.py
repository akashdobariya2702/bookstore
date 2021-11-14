from django.db import models

# Create your models here.


class BooksAuthor(models.Model):
    id = models.IntegerField(primary_key=True)
    birth_year = models.SmallIntegerField(blank=True, null=True)
    death_year = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'books_author'


class BooksBook(models.Model):
    id = models.IntegerField(primary_key=True)
    download_count = models.IntegerField(blank=True, null=True)
    gutenberg_id = models.IntegerField()
    media_type = models.CharField(max_length=16)
    title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books_book'


class BooksBookAuthors(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey('BooksBook', on_delete=models.CASCADE,
                                related_name='map_author', db_column='book_id')
    author_id = models.ForeignKey('BooksAuthor', on_delete=models.CASCADE, db_column='author_id')

    class Meta:
        managed = False
        db_table = 'books_book_authors'


class BooksBookBookshelves(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey('BooksBook', on_delete=models.CASCADE,
                                related_name='map_shelf', db_column='book_id')
    bookshelf_id = models.ForeignKey(
        'BooksBookshelf', on_delete=models.CASCADE, db_column='bookshelf_id')

    class Meta:
        managed = False
        db_table = 'books_book_bookshelves'


class BooksBookLanguages(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey('BooksBook', on_delete=models.CASCADE,
                                related_name='map_language', db_column='book_id')
    language_id = models.ForeignKey(
        'BooksLanguage', on_delete=models.CASCADE, db_column='language_id')

    class Meta:
        managed = False
        db_table = 'books_book_languages'


class BooksBookSubjects(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey('BooksBook', on_delete=models.CASCADE,
                                related_name='map_subject', db_column='book_id')
    subject_id = models.ForeignKey('BooksSubject', on_delete=models.CASCADE, db_column='subject_id')

    class Meta:
        managed = False
        db_table = 'books_book_subjects'


class BooksBookshelf(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'books_bookshelf'


class BooksFormat(models.Model):
    id = models.IntegerField(primary_key=True)
    mime_type = models.CharField(max_length=32)
    url = models.TextField()
    book_id = models.ForeignKey('BooksBook', on_delete=models.CASCADE,
                                related_name='formats', db_column='book_id')

    class Meta:
        managed = False
        db_table = 'books_format'


class BooksLanguage(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'books_language'


class BooksSubject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'books_subject'
