from django.urls import include, path
from rest_framework import routers

from auth.views import LoginViewSet, RefreshViewSet, RegisterViewSet

router = routers.SimpleRouter()
router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")
router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")

urlpatterns = [
    path("", include(router.urls)),
]
