from rest_framework.urls import path 
from rest_framework.authtoken.views import obtain_auth_token 
from user_app.api.views import *

#jwt authentification
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('login/', obtain_auth_token, name = 'login'),           #allow use to login for generating new token.add()
    path('register/', registration_view, name = 'register'),
    path('logout_view/',  logout_view, name = 'logout_view'),

    
    #jwt authentification.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

