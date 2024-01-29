from django.urls import path
from recommends import views

urlpatterns = [
    path("recommends/", views.RecommendList.as_view()),
    path("recommends/<int:pk>/", views.RecommendDetail.as_view()),
]
