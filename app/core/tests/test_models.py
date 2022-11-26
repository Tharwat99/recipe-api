from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email(self):
        """ test creation of new user is ok """
        email = "asd@gmail.com"
        password = "asd123asd"
        user = get_user_model().objects.create_user(email = email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalizer(self):
        """ test that email for new user is normalized """
        email = "asd@GMAil.com"
        user = get_user_model().objects.create_user(email, "asd")
        self.assertEqual(user.email, email.lower())

    def test_creating_user_without_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'asd123')
    def test_create_new_super_user(self):
        """ test creating new superuser """
        user = get_user_model().objects.create_superuser('asd@gmail.com', 'asd123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
    