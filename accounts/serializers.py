from django.conf import settings
from rest_framework import serializers

from abstract.serializers import AbstractSerializer
from accounts.models import User


class UserSerializer(AbstractSerializer):
    class Meta:
        model = User
        # List of all the fields that can be included in a request or a response
        fields = [
            # "id",
            "username",
            "name",
            "first_name",
            "last_name",
            "bio",
            "avatar",
            "email",
            "is_active",
            # "created",
            # "updated",
            "posts_count",
        ]
        # List of all the fields that can only be read by the user
        read_only_field = ["is_active"]
