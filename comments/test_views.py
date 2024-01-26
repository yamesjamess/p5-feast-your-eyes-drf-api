from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from posts.models import Post
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentViewsTest(APITestCase):
    def setUp(self):
        # Create a test user
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

        # Set up authentication for the test user
        self.client.force_authenticate(user=self.user)

    def test_comment_list(self):
        # Test CommentList view (GET request)
        response = self.client.get("/comments/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_create(self):
        # Test CommentList view (POST request)
        data = {"post": self.post.id, "content": "New comment content"}

        response = self.client.post("/comments/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["owner"], self.user.username)
        self.assertEqual(response.data["post"], self.post.id)
        self.assertEqual(response.data["content"], "New comment content")

    def test_comment_detail(self):
        # Test CommentDetail view (GET request)
        response = self.client.get(f"/comments/{self.comment.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["owner"], self.user.username)
        self.assertEqual(response.data["post"], self.post.id)
        self.assertEqual(response.data["content"], "Test comment content")

    def test_comment_update(self):
        # Test CommentDetail view (PUT request)
        updated_content = "Updated comment content"
        data = {"content": updated_content}

        response = self.client.put(f"/comments/{self.comment.id}/", data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["content"], updated_content)

    def test_comment_delete(self):
        # Test CommentDetail view (DELETE request)
        response = self.client.delete(f"/comments/{self.comment.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.filter(id=self.comment.id).exists(), False)
