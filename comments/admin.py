from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Custom Admin configuration for the Comment model.
    """
    list_display = ('owner', 'post', 'created_at', 'updated_at', 'content')
    list_display_links = ('owner', 'post')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('owner', 'post')
