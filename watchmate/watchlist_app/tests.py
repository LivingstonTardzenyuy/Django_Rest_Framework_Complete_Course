from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse                 #allows me to direct to a particular endpoint.
from rest_framework import status

from rest_framework.authtoken.models import Token 
from watchlist_app.api import serializers 
from watchlist_app import models 


class StreamPlatFormTestCase(APITestCase):

    def setUp(self):                #creating a user and passing the token in our headers. 
        self.user = User.objects.create_user(
            username = "example",
            password = "Password@123"
        )
        self.token = Token.objects.get(user__username = self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)   #allow data to be pass in my header.


        self.stream = models.StreamPlatForm.objects.create(
            name ="Netflix",
            about = "1 streaming platform",
            website = "https://netflix.com"
        )

    def test_streamplatform_create(self):
        data = {
            "name": "Netflix",
            "about": "1 streaming platform",
            "website": "https://netflix.com"
        }


        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



    def test_streamplatform_ind(self):
        response = self.client.get(reverse('streamplatform-detail', args = (self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_streamplatform_list(self):
    #     response = self.client.get(reverse('streamplatform-list'))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)