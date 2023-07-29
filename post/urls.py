from django.urls import include, path
from rest_framework import routers

from .views import PostViewSet

router = routers.SimpleRouter()
router.register(r"post", PostViewSet, basename="post")

urlpatterns = [
    path("", include(router.urls)),
]
