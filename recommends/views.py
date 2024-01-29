from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from recommends.models import Recommend
from recommends.serializers import RecommendSerializer


class RecommendList(generics.ListCreateAPIView):
    """
    List recommendations or create a recommendation if logged in.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RecommendSerializer
    queryset = Recommend.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecommendDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a recommendation or delete it by id if you own it.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RecommendSerializer
    queryset = Recommend.objects.all()
