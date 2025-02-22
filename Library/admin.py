from django.contrib import admin

from Library.models import Author, Book, Category, Publisher


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "no_of_books", "place_of_birth")
    search_fields = ("name",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "published_date",
        "available_copies",
        "created_at",
    )
    search_fields = ("title", "author__name")
    list_filter = ("published_date",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    search_fields = ("name",)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address")
    search_fields = ("name",)

