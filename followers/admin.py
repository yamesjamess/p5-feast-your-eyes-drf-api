from django.contrib import admin
from .models import Follower

@admin.register(Follower)
class RecommendAdmin(admin.ModelAdmin):
    """
    Custom Admin configuration for the Follower model.
    """
    list_display = ('owner', 'post', 'created_at')
    list_display_links = ('owner', 'post')
    list_filter = ('created_at',)
    search_fields = ('owner', 'post')
