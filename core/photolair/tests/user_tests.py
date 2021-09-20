from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCase(TestCase):
    """
    Performs tests on the user model such as account creation and error 
    checking.
    
    We leave out test cases involving passwords as Django comes pre-built 
    with password validators (view AUTH_PASSWORD_VALIDATORS 
    in core/core/settings.py)
    """
    
    def test_create_user(self):
        """
        Test if a user can be created successfully
        """
        username = 'harmanjiggly'
        password = 'testpass123'

        User.objects.create_user(
            username=username,
            password=password
        )

        new_user = User.objects.get(
            username=username
        )

        self.assertEqual(
            new_user.username,
            username,
            msg='Unable to successfully retrieve new user'
        )

        self.assertTrue(
            new_user.check_password(password),
            msg='Password does not match'
        )
    

    def test_user_no_username(self):
        """
        Create a user without a username and catch type error
        """
        with self.assertRaises(TypeError):
            email = 'harmanjiggly@jiggly.ca'
            password = 'testpass123'

            new_user = User.objects.create_user(
                email=email,
                password=password
            )

            self.assertEqual(
                new_user.email, 
                email
            )
            
            self.assertTrue(
                new_user.check_password(password), 
            )


    def test_user_duplicate_username(self):
        """
        Attempt to make user without username and catch integrity error
        """
        with self.assertRaises(IntegrityError):
            username = 'harmanjiggly'
            password = 'testpass123'

            User.objects.create_user(
                username=username,
                password=password
            )

            new_user = User.objects.create_user(
                username=username,
                password=password,
            )

            self.assertEqual(
                new_user.username, 
                username
            )
            
            self.assertTrue(
                new_user.check_password(password), 
            )
    