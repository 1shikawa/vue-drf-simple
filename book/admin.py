from django.contrib import admin

from .models import Book, Author

# Register your models here.
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', )
    readonly_fields = ('id',)


class BookModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'id', 'created_at')
    ordering = ('-created_at', )
    readonly_fields = ('id', 'created_at')


admin.site.register(Author, AuthorModelAdmin)
admin.site.register(Book, BookModelAdmin)