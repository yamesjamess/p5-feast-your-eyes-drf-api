from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.db import transaction
from .models import Follower


class FollowerModelTest(APITestCase):
    def setUp(self):
        # Create test users
        self.user1 = User.objects.create_user(username="user1", password="password1")
        self.user2 = User.objects.create_user(username="user2", password="password2")

    def tearDown(self):
        # Clean up the database after each test
        Follower.objects.all().delete()

    def test_follower_creation_and_deletion(self):
        # Log in user1
        self.client.force_authenticate(user=self.user1)

        # Follow user2
        with transaction.atomic():
            response = self.client.post("/followers/", {"followed": self.user2.id})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Follower.objects.count(), 1)
        self.assertEqual(Follower.objects.first().owner, self.user1)
        self.assertEqual(Follower.objects.first().followed, self.user2)

        # Unfollow user2
        with transaction.atomic():
            response = self.client.delete(f"/followers/{Follower.objects.first().id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Follower.objects.count(), 0)

    def test_double_follow_prevention(self):
        # Log in user1
        self.client.force_authenticate(user=self.user1)

        # Follow user2 for the first time
        with transaction.atomic():
            self.client.post("/followers/", {"followed": self.user2.id})
        self.assertEqual(Follower.objects.count(), 1)

        # Try to follow user2 again (should fail due to unique_together constraint)
        with transaction.atomic():
            response = self.client.post("/followers/", {"followed": self.user2.id})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Follower.objects.count(), 1)
