from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post
from .models import Comment


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        # Create a test post
        self.post = Post.objects.create(
            owner=self.user,
            restaurant="Test Restaurant",
            title="Test Post Title",
            tag="test-tag",
            content="Test post content",
        )

        # Create a test comment
        self.comment = Comment.objects.create(
            owner=self.user, post=self.post, content="Test comment content"
        )

    def test_comment_str(self):
        # Ensure the __str__ method returns the correct string representation
        self.assertEqual(str(self.comment), "Test comment content")

    def test_comment_ordering(self):
        # Create comments with different created_at values
        comment1 = Comment.objects.create(
            owner=self.user,
            post=self.post,
            content="Comment 1",
        )

        comment2 = Comment.objects.create(
            owner=self.user,
            post=self.post,
            content="Comment 2",
        )

        comment3 = Comment.objects.create(
            owner=self.user,
            post=self.post,
            content="Comment 3",
        )

        ordered_comments = Comment.objects.all()

        self.assertEqual(ordered_comments[0], comment3)
        self.assertEqual(ordered_comments[1], comment2)
        self.assertEqual(ordered_comments[2], comment1)
