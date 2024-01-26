from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_create_profile_signal(self):
        # Ensure a user profile is created when a new user is saved
        self.assertEqual(
            Profile.objects.count(), 1
        )  # Check that there are 1 profiles initially from setup

        new_user = User.objects.create_user(username="newuser", password="newpassword")

        created_profile = Profile.objects.get(owner=new_user)

        self.assertEqual(
            Profile.objects.count(), 2
        )  # Check that a profile has been created
        self.assertEqual(created_profile.owner, new_user)
        self.assertEqual(created_profile.name, "")
        self.assertEqual(created_profile.content, "")
