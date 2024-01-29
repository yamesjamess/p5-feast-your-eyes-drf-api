from django.contrib import admin
from .models import Recommend


@admin.register(Recommend)
class RecommendAdmin(admin.ModelAdmin):
    """
    Custom Admin configuration for the Recommend model.
    """

    list_display = ("owner", "post", "created_at")
    list_display_links = ("owner", "post")
    list_filter = ("created_at",)
    search_fields = ("owner", "post")
