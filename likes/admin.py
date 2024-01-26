from django.contrib import admin
from .models import Like

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """
    Custom Admin configuration for the Like model.
    """
    list_display = ('owner', 'post', 'created_at')
    list_display_links = ('owner', 'post')
    list_filter = ('created_at',)
    search_fields = ('owner', 'post')
