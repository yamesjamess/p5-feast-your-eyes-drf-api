from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Custom Admin configuration for the Post model.
    """

    list_display = ("id", "owner", "restaurant", "title", "tag", "created_at")
    list_display_links = ("restaurant", "title", "id")
    list_filter = ('created_at', 'tag', 'owner')
    search_fields = ('restaurant', 'title', 'tag', 'owner__username')
