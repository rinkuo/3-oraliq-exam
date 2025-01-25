from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'slug')
    search_fields = ('user__username', 'bio')
    prepopulated_fields = {'slug': ('user',)}
    ordering = ('user',)
