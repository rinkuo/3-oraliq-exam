from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ('name', 'email', 'comment', 'created_at')
    readonly_fields = ('created_at',)

@admin.action(description='Publish selected posts')
def make_published(modeladmin, request, queryset):
    queryset.update(status='published')

@admin.action(description='Unpublish selected posts')
def make_draft(modeladmin, request, queryset):
    queryset.update(status='draft')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'category', 'created_at', 'updated_at', 'status')
    list_filter = ('status', 'category', 'created_at')
    search_fields = ('name', 'description', 'author__user__username')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)
    inlines = [CommentInline]
    actions = [make_published, make_draft]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created_at')
    list_filter = ('created_at', 'post')
    search_fields = ('name', 'email', 'comment', 'post__name')
    ordering = ('-created_at',)
