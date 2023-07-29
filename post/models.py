from django.db import models

from abstract.models import AbstractManager, AbstractModel

# from accounts.models import User


class PostManager(AbstractManager):
    pass


class Post(AbstractModel):
    author = models.ForeignKey(to="accounts.User", on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)
    objects = PostManager()

    def __str__(self):
        return f"{self.author.name}: {self.public_id}"
