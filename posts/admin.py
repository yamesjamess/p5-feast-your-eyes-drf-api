from django.contrib import admin
from .model import Post

@admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('owner', 'created_at', 'restaurant', 'title', 'tag', 'content', 'image')
    list_display_links = ('id', 'title')
