from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import RequestsClient
from .models import Post
from .serializers import PostSerializer

class PostAPITestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test post
        self.post_data = {
            'owner': self.user,
            'restaurant': 'Test Restaurant',
            'title': 'Test Post',
            'tag': 'testtag',
            'content': 'Test Content',
            'image_filter': '1977',
        }
        self.post = Post.objects.create(**self.post_data)

    def test_post_list_create(self):
        # Login the user
        self.client.login(username='testuser', password='testpassword')
        
        # Test creating a new post
        response = self.client.post('/posts/', self.post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test retrieving the list of posts
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_post_detail(self):
        # Test retrieving a specific post
        response = self.client.get(f'/posts/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)