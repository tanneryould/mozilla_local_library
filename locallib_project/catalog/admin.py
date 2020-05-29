from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

class BooksInline(admin.TabularInline):
    model = Book

# Register ModelAdmin classes METHOD ONE

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register ModelAdmin classes METHOD TWO
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInsanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'is_overdue')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

admin.site.register(Genre)
admin.site.register(Language)