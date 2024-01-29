from django.urls import path
from posts import views


urlpatterns = [
    path("posts/", views.PostList.as_view()),
    path("posts/<int:pk>/", views.PostDetail.as_view()),
    path("posts/tag/<str:tag>/", views.TagList.as_view()),
]
