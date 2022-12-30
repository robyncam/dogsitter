from django.contrib.auth.models import User
from django.test import Client, TestCase


class SignUpTestCase(TestCase):
    def test_signup_and_login(self):
        c = Client()
        data = {
            'username': 'test_user',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test_user@example.com',
            'password': 'abcd1234',
            'confirm_password': 'abcd1234'
        }
        r = c.post('/register', data=data)

        assert User.objects.filter(
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
        ).count() == 1

        data = {
            'username': 'test_user',
            'password': 'abcd1234'
        }

        r = c.post('/login', data=data, follow=True)
        assert b'Create Your Profile' in r.content
