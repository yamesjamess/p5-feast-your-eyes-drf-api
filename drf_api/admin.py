from django.contrib import admin
from posts.models import Post
from comments.models import Comment
from likes.models import Like
from followers.models import Follower
from profiles.models import Profile
from recommends.models import Recommend


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follower)
admin.site.register(Recommend)
admin.site.register(Profile)

