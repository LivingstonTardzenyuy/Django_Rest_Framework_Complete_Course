from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token 
from user_app import models 
@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            # serializer.save()  # Call the save method
            account = serializer.save()

            #authomatic creation of tokens during signup.
            data['response'] = "Registration Successful"
            data['username'] = account.username 
            data['email'] = account.email 

            token = Token.objects.get(user= account).key 
            data['token'] = token 
        else:
            data = serializer.errors 
    return Response(data)

