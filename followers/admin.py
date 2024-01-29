from django.contrib import admin
from .models import Follower


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    """
    Custom Admin configuration for the Follower model.
    """

    list_display = ("owner", "followed", "created_at")
    list_display_links = ("owner", "followed")
    list_filter = ("created_at",)
    search_fields = ("owner", "followed")
