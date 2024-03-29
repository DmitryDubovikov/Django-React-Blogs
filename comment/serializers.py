from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from abstract.serializers import AbstractSerializer
from accounts.models import User
from accounts.serializers import UserSerializer
from post.models import Post

from .models import Comment


class CommentSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field="public_id")
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field="public_id")

    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data["edited"] = True
        instance = super().update(instance, validated_data)
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep["author"])
        rep["author"] = UserSerializer(author).data
        return rep

    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        return value

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can't create a post for another user.")
        return value

    class Meta:
        model = Comment
        # List of all the fields that can be included in a request or a response
        fields = ["id", "post", "author", "body", "edited", "created", "updated"]
        read_only_fields = ["edited"]
