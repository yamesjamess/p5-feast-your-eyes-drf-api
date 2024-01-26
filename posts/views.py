from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from rest_framework.views import APIView
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count("likes", distinct=True),
        recommends_count=Count("recommends", distinct=True),
        comments_count=Count("comment", distinct=True),
    ).order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["owner__username", "title", "content", "tag", "restaurant"]
    filterset_fields = [
        "owner__profile",
        "owner__followed__owner__profile",
        "likes__owner__profile",
        "recommends__owner__profile",
        "tag",
    ]
    ordering_fields = [
        "likes_count",
        "recommends_count",
        "comments_count",
        "likes__created_at",
        "recommends__created_at",
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count("likes", distinct=True),
        recommends_count=Count("recommends", distinct=True),
        comments_count=Count("comment", distinct=True),
    ).order_by("-created_at")


class TagList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        tag = self.kwargs["tag"]
        return Post.objects.filter(tag__iexact=tag)  # Case-insensitive match

