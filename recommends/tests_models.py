from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post
from .models import Recommend


class RecommendModelTest(TestCase):
    def setUp(self):
        # Create test users
        self.user1 = User.objects.create_user(username="user1", password="password1")
        self.user2 = User.objects.create_user(username="user2", password="password2")

        # Create test post
        self.post = Post.objects.create(
            owner=self.user1,
            restaurant="Test Restaurant",
            title="Test Post Title",
            tag="test-tag",
            content="Test post content",
        )

    def test_create_recommend(self):
        # Create a new recommend
        recommend = Recommend.objects.create(owner=self.user1, post=self.post)

        retrieved_recommend = Recommend.objects.get(pk=recommend.id)

        self.assertEqual(retrieved_recommend.owner, self.user1)
        self.assertEqual(retrieved_recommend.post, self.post)

    def test_recommend_str(self):
        recommend = Recommend.objects.create(owner=self.user1, post=self.post)

        # Ensure the __str__ method returns the correct string representation
        self.assertEqual(str(recommend), f"{self.user1} {self.post}")
