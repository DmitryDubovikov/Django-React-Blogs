from django.urls import include, path
from rest_framework import routers

from auth.views import LoginViewSet, RegisterViewSet

router = routers.SimpleRouter()
router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")

urlpatterns = [
    path("", include(router.urls)),
]
