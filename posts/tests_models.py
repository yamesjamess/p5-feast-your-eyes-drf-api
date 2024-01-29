from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_create_post(self):
        # Create a new post
        post = Post.objects.create(
            owner=self.user,
            restaurant="Test Restaurant",
            title="Test Post Title",
            tag="test-tag",
            content="Test post content",
        )

        retrieved_post = Post.objects.get(pk=post.id)

        self.assertEqual(retrieved_post.owner, self.user)
        self.assertEqual(retrieved_post.restaurant, "Test Restaurant")
        self.assertEqual(retrieved_post.title, "Test Post Title")
        self.assertEqual(retrieved_post.tag, "test-tag")
        self.assertEqual(retrieved_post.content, "Test post content")

    def test_post_str(self):
        post = Post.objects.create(
            owner=self.user,
            restaurant="Test Restaurant",
            title="Test Post Title",
            tag="test-tag",
            content="Test post content",
        )

        # Ensure the __str__ method returns the correct string representation
        expected_str = f"{post.id} Test Restaurant's Test Post Title"
        self.assertEqual(str(post), expected_str)

    def test_ordering(self):
        # Create multiple posts with different created_at values
        post1 = Post.objects.create(
            owner=self.user, restaurant="Restaurant 1", title="Title 1",
            tag="tag1"
        )
        post2 = Post.objects.create(
            owner=self.user, restaurant="Restaurant 2", title="Title 2",
            tag="tag2"
        )
        post3 = Post.objects.create(
            owner=self.user, restaurant="Restaurant 3", title="Title 3",
            tag="tag3"
        )

        ordered_posts = Post.objects.all()

        self.assertEqual(ordered_posts[0], post3)
        self.assertEqual(ordered_posts[1], post2)
        self.assertEqual(ordered_posts[2], post1)
