from rest_framework import serializers
from .models import User
from passlib.hash import pbkdf2_sha256


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwarg = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password2 != password:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        user.password = pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=32)
        user.save()
        return user
