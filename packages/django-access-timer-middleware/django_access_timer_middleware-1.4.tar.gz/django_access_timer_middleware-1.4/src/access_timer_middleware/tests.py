from time import sleep

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

# Create your tests here.


User = get_user_model()


class AccessTimerMiddlewareTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.password = 'testuser@123Com'
        self.login_url = reverse("login")
        self.signup_url = reverse("signup")
        self.card_url = reverse("card-list")
        self.card_number1 = "4188202145836985"
        self.card_data = {
            'card_number': self.card_number1,
            'card_holder_name': "PABLO BARBADO",
            'month': "01",
            'year': "2020",
            'cvv': "111",
            'user': 1
        }
        settings.DEBUG = True

    def test_access_timer_middleware_with_login(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@localhost.com',
            'password': self.password,
        }

        response = self.client.post(self.signup_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('refresh', response.json())
        self.assertIn('access', response.json())

        data = {
            'username': 'testuser',
            'password': self.password
        }

        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertIn('refresh', response.json())
        self.assertIn('access', response.json())

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.json()['access'])
        user = User.objects.get(pk=1)

        print(user.id)

        response = self.client.post(self.card_url, self.card_data, format='json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_access_timer_middleware_with_login_with_default_duration1(self):
        user = User.objects.create_user(
            username='testuser',
            email='testuser@localhost.com',
            password=self.password
        )

        data = {
            'username': 'testuser',
            'password': self.password
        }

        settings.DEFAULT_DURATION = timezone.timedelta(seconds=1).total_seconds()

        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertIn('refresh', response.json())
        self.assertIn('access', response.json())

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.json()['access'])

        sleep(5)

        response = self.client.post(self.card_url, self.card_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn('error', response.json())

    def test_access_timer_middleware_without_login_with_default_duration10(self):
        user = User.objects.create_user(
            username='testuser',
            email='testuser@localhost.com',
            password=self.password
        )

        data = {
            'username': 'testuser',
            'password': self.password
        }

        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertIn('refresh', response.json())
        self.assertIn('access', response.json())

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.json()['access'])

        settings.DEFAULT_DURATION = timezone.timedelta(seconds=10).total_seconds()

        sleep(5)

        response = self.client.post(self.card_url, self.card_data, format='json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('card_number', response.json())
