from django.urls import include, path
# from rest_framework import routers
from rest_framework_nested import routers

from comment.views import CommentViewSet

from .views import PostViewSet

router = routers.SimpleRouter()
router.register(r"post", PostViewSet, basename="post")

posts_router = routers.NestedSimpleRouter(router, r"post", lookup="post")
posts_router.register(r"comment", CommentViewSet, basename="post-comment")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(posts_router.urls)),
]
