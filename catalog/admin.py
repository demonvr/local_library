from django.contrib import admin
from .models import Author, Genre, Language, Book, BookInstance
# Register your models here.


class BookInLine(admin.TabularInline):
    extra = 0
    model = Book


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInLine]


class BookInstanceInLine(admin.TabularInline):
    extra = 0
    model = BookInstance


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id', 'borrower')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInLine]


# admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Genre)
