from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Custom Admin configuration for the Profile model.
    """

    list_display = ("owner", "created_at", "updated_at", "name")
    list_display_links = ("owner", "name")
    list_filter = ("created_at", "updated_at")
    search_fields = ("owner", "name")
