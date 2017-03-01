from django.contrib import admin

from .models import Book, Author

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Book Details",{"fields": ["title", "authors"]}),
        ("Review", {"fields":["is_favorite","review","date_reviewed"]}),
    ]


# Register your models here.

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
