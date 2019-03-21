from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into JSON formt."""
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        """Meta class to map serializer's field with the model fileds."""
        model = Book
        fields = ('id', 'title', 'author', 'copies', 'created_by', 'synopsis')
        read_only_fields = ( 'date_added','date_modified')

class UserSerializer(serializers.ModelSerializer):
    """Maps the user model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's field with the model fileds."""
        model = User
        fields = ( 'first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs ={'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name = validated_data['last_name'],
            username=validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


        