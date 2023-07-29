from django.urls import path, include
from rest_framework import routers

from auth.views.register import RegisterViewSet

router = routers.SimpleRouter()
router.register(r"auth/register", RegisterViewSet, basename="auth-register")

urlpatterns = [
    path("", include(router.urls)),
]
