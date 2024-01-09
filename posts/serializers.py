from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from recommends.models import Recommend


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    like_id = serializers.SerializerMethodField()
    recommend_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    recommends_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    def get_recommend_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            recommend = Recommend.objects.filter(owner=user, post=obj).first()
            return recommend.id if recommend else None
        return None

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError("Image size larger than 2MB!")
        if value.image.width > 4096:
            raise serializers.ValidationError("Image width larger than 4096px")
        if value.image.height > 4096:
            raise serializers.ValidationError("Image height larger than 4096px")
        return value

    class Meta:
        model = Post
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "title",
            "content",
            "image",
            "image_filter",
            "like_id",
            "recommend_id",
            "likes_count ",
            "recommends_count",
            "comments_count",
        ]
