from django.contrib import admin
from book.models import *


admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Review)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'author', 'date')
    list_filter = ('genre', 'author', 'date')
    list_select_related = ('genre', 'author',)
    readonly_fields = ('date', )
    ordering = ('-pk', )
    prepopulated_fields = {'slug': ('name',)}
