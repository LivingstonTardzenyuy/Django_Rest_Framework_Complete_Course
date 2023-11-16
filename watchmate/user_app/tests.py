from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse                 #allows me to direct to a particular endpoint.
from rest_framework import status

from rest_framework.authtoken.models import Token 


class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            "username": "testcase",
            "email": "testcase@example.com",
            "password": "NewPassword@123",
            "password2": "NewPassword@123"
        }

        response = self.client.post(reverse('register'), data)      
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)     #matching our response with our status code to see if they are the same.
        # self



class LoginLogOutTestCase(APITestCase):
    def setUp(self):                # a method that creates a user for testing purpose.
        self.user = User.objects.create_user(username = "example", password = "NewPassword@123")

    
    def test_login(self):
        data = {
            "username": "example",
            "password": "NewPassword@123"
        }

        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



    def test_logout(self):
        self.token = Token.objects.get(
            user__username = "example")
        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)      #login in the user     #passing our data in our headers to login
        response = self.client.post(reverse('logout_view'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)