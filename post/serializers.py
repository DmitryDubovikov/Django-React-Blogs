from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from abstract.serializers import AbstractSerializer
from accounts.models import User
from post.models import Post


class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field="public_id")

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can't create a post for another user.")
        return value

    class Meta:
        model = Post
        # List of all the fields that can be included in a request or a response
        fields = ["id", "author", "body", "edited", "created", "updated"]
        read_only_fields = ["edited"]
