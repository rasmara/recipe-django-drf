"""
Test for models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        email = "test@example.com"
        password = "testpass123"

        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_normalize_email(self):
        """Test emails for normalize"""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.com", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_email_empty_raises_value_error(self):
        """Test creation for user without an email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "sample@123")

    def test_create_superuser(self):
        """create a superuser"""
        user = get_user_model().objects.create_superuser(
            "test@123.com", "superUser@123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
