from rest_framework import serializers 
from django.contrib.auth.models import User 


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style= {'input_type': 'password'},
        write_only = True)

    class Meta:
        model = User 
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        email_user = self.validated_data['email']
        username_user = self.validated_data['username']

        if password != password2:
            raise serializers.ValidationError({'error': 'the 2 passwords should be the same'})

        if User.objects.filter(email = self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'email already in use.'})


        account = User(
            email= email_user,
            username = username_user,
            password = password2
            )

        # account.set_password(password)
        account.save()

        return account 