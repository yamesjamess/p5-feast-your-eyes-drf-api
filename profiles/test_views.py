from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Profile

class ProfileAPITestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Check if a profile already exists for the user
        existing_profile = Profile.objects.filter(owner=self.user).first()

        # Create an API client and authenticate the user
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Create a test profile only if it doesn't exist
        if not existing_profile:
            self.profile_data = {
                'name': 'Test Name',
                'content': 'Test Content',
            }
            self.profile = Profile.objects.create(owner=self.user, **self.profile_data)

    def test_profile_list(self):
        # Test retrieving the list of profiles
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_profile_detail(self):
        # Test retrieving a specific profile
        response = self.client.get(f'/profiles/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_update(self):
        # Test updating a specific profile
        updated_data = {'name': 'Updated Test Name'}
        response = self.client.put(f'/profiles/{self.user.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Test Name')
