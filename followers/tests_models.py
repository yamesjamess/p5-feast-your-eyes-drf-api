from django.test import TestCase
from django.contrib.auth.models import User
from .models import Follower


class FollowerModelTest(TestCase):
    def setUp(self):
        # Create two test users
        self.user1 = User.objects.create_user(username="user1", password="password1")
        self.user2 = User.objects.create_user(username="user2", password="password2")

    def test_create_follower(self):
        # Create a follower relationshipF
        follower = Follower.objects.create(owner=self.user1, followed=self.user2)

        retrieved_follower = Follower.objects.get(pk=follower.id)

        self.assertEqual(retrieved_follower.owner, self.user1)
        self.assertEqual(retrieved_follower.followed, self.user2)

    def test_follower_str(self):
        follower = Follower.objects.create(owner=self.user1, followed=self.user2)

        # Ensure the __str__ method returns the correct string representation
        self.assertEqual(str(follower), f"{self.user1} {self.user2}")
