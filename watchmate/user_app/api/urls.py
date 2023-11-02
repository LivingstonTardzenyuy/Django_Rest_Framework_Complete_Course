from rest_framework.urls import path 
from rest_framework.authtoken.views import obtain_auth_token 
from user_app.api.views import *

urlpatterns = [
    path('login/', obtain_auth_token, name = 'login'),           #allow use to login for generating new token.add()
    path('register/', registration_view, name = 'register'),
    path('logout_view/',  logout_view, name = 'logout_view'),
]