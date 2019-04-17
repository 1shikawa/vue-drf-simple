from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    class Meta:
        db_table = 'author'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='著者名', max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        db_table = 'book'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル', max_length=20)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    authors = models.ManyToManyField(Author, verbose_name='著者名', null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title