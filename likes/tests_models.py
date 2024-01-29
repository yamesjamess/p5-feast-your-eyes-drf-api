from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post
from .models import Like


class LikeModelTest(TestCase):
    def setUp(self):
        # Create test users
        self.user1 = User.objects.create_user(username="user1",
                                              password="password1")
        self.user2 = User.objects.create_user(username="user2",
                                              password="password2")

        # Create test post
        self.post = Post.objects.create(
            owner=self.user1,
            restaurant="Test Restaurant",
            title="Test Post Title",
            tag="test-tag",
            content="Test post content",
        )

    def test_create_like(self):
        # Create a new like
        like = Like.objects.create(owner=self.user1, post=self.post)

        retrieved_like = Like.objects.get(pk=like.id)

        self.assertEqual(retrieved_like.owner, self.user1)
        self.assertEqual(retrieved_like.post, self.post)

    def test_like_str(self):
        like = Like.objects.create(owner=self.user1, post=self.post)

        # Ensure the __str__ method returns the correct string representation
        self.assertEqual(str(like), f"{self.user1} {self.post}")
