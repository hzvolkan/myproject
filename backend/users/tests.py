from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password

class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('register')
        data = {'username': 'testuser', 'password': 'testpass', 'email': 'test@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, 'testuser')

    def test_user_registration_with_existing_username(self):
        url = reverse('register')
        data = {'username': 'testuser', 'password': 'testpass', 'email': 'test@example.com'}
        self.client.post(url, data, format='json')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_token_obtain(self):
        # Kullanıcıyı oluştur ve aktif yap
        user = CustomUser.objects.create_user(username='testuser', password='testpass')
        user.is_active = True
        user.save()

        # Doğrudan Django login fonksiyonu ile oturum aç
        self.client.login(username='testuser', password='testpass')

        # Token endpointine istek gönder
        url = reverse('token_obtain_pair')
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(url, data, format='json')

        print("Response Data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_model_fields(self):
        user = CustomUser.objects.create_user(username='testuser', password='testpass', bio='Test bio')
        self.assertEqual(user.bio, 'Test bio')

    def test_api_endpoints(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)  # GET is not allowed
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password': 'newpass', 'email': 'new@example.com'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
