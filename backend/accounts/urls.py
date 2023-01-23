from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views


urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view()), 
    path("api/token/refresh/", TokenRefreshView.as_view()), 
    path("api/token/verify/", TokenVerifyView.as_view()), 
    path("register/", views.register), 
    path("get_user/", views.load_user)
]