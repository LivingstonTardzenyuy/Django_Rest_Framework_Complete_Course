from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializer
from rest_framework.response import Response

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # Call the save method
            return Response(serializer.data)

    return Response(serializer.errors, status=400)